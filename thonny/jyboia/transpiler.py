"""
Transpilador Jybóia: Converte Português Estruturado (.jy) em Python (.py).
"""

import io
import os
import token
import tokenize
from collections import defaultdict
from typing import List, Optional, Tuple

from thonny.jyboia.keywords import (
    PALAVRAS_CHAVE,
    PALAVRAS_COMPOSTAS,
    FUNCOES_EMBUTIDAS,
)
from thonny.jyboia.builtins_runtime import RUNTIME_HEADER
from thonny.jyboia.sourcemap import SourceMap


def _tokenizar(codigo: str) -> List[tokenize.TokenInfo]:
    """Converte o código fonte em uma lista de TokenInfo."""
    bytes_io = io.BytesIO(codigo.encode("utf-8"))
    tokens = []
    try:
        for tok in tokenize.tokenize(bytes_io.readline):
            tokens.append(tok)
    except tokenize.TokenError:
        pass
    return tokens


def transpilar(
    codigo_jy: str,
    incluir_runtime: bool = False,
    caminho_jy: Optional[str] = None,
    caminho_py: Optional[str] = None,
) -> Tuple[str, SourceMap]:
    """
    Transpila o código Jybóia (.jy) em código Python (.py) equivalente.
    """
    if not codigo_jy.strip():
        sm = SourceMap(
            jy_code=codigo_jy,
            py_code="",
            jy_filepath=caminho_jy,
            py_filepath=caminho_py,
        )
        return "", sm

    tokens = _tokenizar(codigo_jy)
    tokens_modificados = []
    
    i = 0
    total = len(tokens)
    
    precisa_runtime = False
    runtime_helpers = {"leia_inteiro", "leia_real", "leia_int", "leia_float", "leia_texto"}

    while i < total:
        tok = tokens[i]
        
        if tok.type == tokenize.ENCODING:
            i += 1
            continue

        if tok.type == tokenize.NAME and tok.string in runtime_helpers:
            precisa_runtime = True

        # Palavras compostas (ex: "senao se", "nao em", "eh nao")
        if i + 1 < total and tok.type == tokenize.NAME:
            tok_prox = tokens[i + 1]
            if tok_prox.type == tokenize.NAME:
                par = (tok.string.lower(), tok_prox.string.lower())
                if par in PALAVRAS_COMPOSTAS:
                    substituicao = PALAVRAS_COMPOSTAS[par]
                    tokens_modificados.append(
                        (tok.start, tok_prox.end, substituicao)
                    )
                    i += 2
                    continue

        # Palavras simples
        if tok.type == tokenize.NAME:
            eh_atributo = False
            if len(tokens_modificados) > 0 and i > 0:
                prev_tok = tokens[i - 1]
                if prev_tok.exact_type == token.DOT:
                    eh_atributo = True

            if not eh_atributo:
                if tok.string in PALAVRAS_CHAVE:
                    subst = PALAVRAS_CHAVE[tok.string]
                    tokens_modificados.append((tok.start, tok.end, subst))
                    i += 1
                    continue
                elif tok.string.lower() in PALAVRAS_CHAVE and tok.string not in ("Verdadeiro", "Falso", "Nulo", "Vazio"):
                    subst = PALAVRAS_CHAVE[tok.string.lower()]
                    tokens_modificados.append((tok.start, tok.end, subst))
                    i += 1
                    continue

                if tok.string in FUNCOES_EMBUTIDAS:
                    subst = FUNCOES_EMBUTIDAS[tok.string]
                    tokens_modificados.append((tok.start, tok.end, subst))
                    i += 1
                    continue
                elif tok.string.lower() in FUNCOES_EMBUTIDAS:
                    subst = FUNCOES_EMBUTIDAS[tok.string.lower()]
                    tokens_modificados.append((tok.start, tok.end, subst))
                    i += 1
                    continue

        tokens_modificados.append((tok.start, tok.end, tok.string))
        i += 1

    linhas_originais = codigo_jy.splitlines(keepends=True)
    resultado_linhas = []
    tokens_por_linha = defaultdict(list)
    
    for s_pos, e_pos, texto in tokens_modificados:
        tokens_por_linha[s_pos[0]].append((s_pos[1], e_pos[1], texto))

    for num_linha in range(1, len(linhas_originais) + 1):
        linha_orig = linhas_originais[num_linha - 1]
        
        if num_linha not in tokens_por_linha:
            resultado_linhas.append(linha_orig)
            continue

        tokens_linha = sorted(tokens_por_linha[num_linha], key=lambda x: x[0])
        nova_linha = ""
        col_atual = 0
        
        for s_col, e_col, texto in tokens_linha:
            if s_col > col_atual:
                nova_linha += linha_orig[col_atual:s_col]
            nova_linha += texto
            col_atual = max(col_atual, e_col)
            
        if col_atual < len(linha_orig):
            nova_linha += linha_orig[col_atual:]

        resultado_linhas.append(nova_linha)

    codigo_py = "".join(resultado_linhas)

    header_count = 0
    if incluir_runtime and precisa_runtime:
        header_count = len(RUNTIME_HEADER.splitlines())
        codigo_py = RUNTIME_HEADER + "\n" + codigo_py

    sourcemap = SourceMap(
        jy_code=codigo_jy,
        py_code=codigo_py,
        jy_filepath=caminho_jy,
        py_filepath=caminho_py,
        header_lines_count=header_count,
    )

    return codigo_py, sourcemap


def transpilar_arquivo(
    caminho_jy: str,
    caminho_py: Optional[str] = None,
    incluir_runtime: bool = True,
) -> Tuple[str, SourceMap]:
    """
    Lê um arquivo .jy, transpila para Python e grava o .py correspondente.
    """
    if not os.path.exists(caminho_jy):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_jy}")

    with open(caminho_jy, "r", encoding="utf-8") as f:
        codigo_jy = f.read()

    if caminho_py is None:
        base, _ = os.path.splitext(caminho_jy)
        caminho_py = base + ".py"

    codigo_py, sourcemap = transpilar(
        codigo_jy,
        incluir_runtime=incluir_runtime,
        caminho_jy=caminho_jy,
        caminho_py=caminho_py,
    )

    with open(caminho_py, "w", encoding="utf-8") as f:
        f.write(codigo_py)

    return codigo_py, sourcemap
