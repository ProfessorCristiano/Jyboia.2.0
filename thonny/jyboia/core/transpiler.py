"""
Transpilador Jybóia: Converte Português Estruturado (.jy) em Python (.py).
Utiliza análise léxica em nível de tokens (módulo tokenize do Python)
para garantir preservação de indentação, comentários, strings e correspondência de linhas.
"""

import io
import os
import token
import tokenize
from typing import List, Optional, Tuple

from jyboia.core.keywords import (
    PALAVRAS_CHAVE,
    PALAVRAS_COMPOSTAS,
    FUNCOES_EMBUTIDAS,
)
from jyboia.core.builtins_runtime import RUNTIME_HEADER
from jyboia.core.sourcemap import SourceMap


def _tokenizar(codigo: str) -> List[tokenize.TokenInfo]:
    """Converte o código fonte em uma lista de TokenInfo."""
    bytes_io = io.BytesIO(codigo.encode("utf-8"))
    tokens = []
    try:
        for tok in tokenize.tokenize(bytes_io.readline):
            tokens.append(tok)
    except tokenize.TokenError:
        # Em caso de código incompleto ou com erro léxico no final
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

    Args:
        codigo_jy: String com o código em Português Estruturado.
        incluir_runtime: Se True, inclui funções utilitárias (ex: leia_inteiro) no topo do .py.
        caminho_jy: Caminho do arquivo .jy (opcional).
        caminho_py: Caminho de destino do arquivo .py (opcional).

    Returns:
        Tupla (codigo_py: str, sourcemap: SourceMap)
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
    
    # Lista de tokens transformados: (srow, scol, erow, ecol, string_substituida)
    tokens_modificados = []
    
    i = 0
    total = len(tokens)
    
    precisa_runtime = False
    runtime_helpers = {"leia_inteiro", "leia_real", "leia_int", "leia_float", "leia_texto"}

    while i < total:
        tok = tokens[i]
        
        # Ignorar token inicial ENCODING (utf-8)
        if tok.type == tokenize.ENCODING:
            i += 1
            continue

        # Verificar uso de helpers do runtime
        if tok.type == tokenize.NAME and tok.string in runtime_helpers:
            precisa_runtime = True

        # Verificar se é palavra composta de 2 tokens consecutivos
        # Ex: "senao se", "senão se", "nao em", "não em", "eh nao", "é não"
        if i + 1 < total and tok.type == tokenize.NAME:
            tok_prox = tokens[i + 1]
            if tok_prox.type == tokenize.NAME:
                par = (tok.string.lower(), tok_prox.string.lower())
                if par in PALAVRAS_COMPOSTAS:
                    substituicao = PALAVRAS_COMPOSTAS[par]
                    # Substitui o par pelo equivalente Python
                    tokens_modificados.append(
                        (tok.start, tok_prox.end, substituicao)
                    )
                    i += 2
                    continue

        # Verificar substituição de token simples
        if tok.type == tokenize.NAME:
            # Verificar se o token anterior não era um ponto de acesso a atributo (ex: obj.se)
            eh_atributo = False
            if len(tokens_modificados) > 0 and i > 0:
                # buscar token anterior não-espaço
                prev_tok = tokens[i - 1]
                if prev_tok.exact_type == token.DOT:
                    eh_atributo = True

            if not eh_atributo:
                # Palavras-chave
                if tok.string in PALAVRAS_CHAVE:
                    subst = PALAVRAS_CHAVE[tok.string]
                    tokens_modificados.append((tok.start, tok.end, subst))
                    i += 1
                    continue
                elif tok.string.lower() in PALAVRAS_CHAVE and tok.string not in ("Verdadeiro", "Falso", "Nulo", "Vazio"):
                    # Caso de keywords com casing variado (ex: SE -> if, ENQUANTO -> while)
                    subst = PALAVRAS_CHAVE[tok.string.lower()]
                    tokens_modificados.append((tok.start, tok.end, subst))
                    i += 1
                    continue

                # Funções embutidas
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

        # Manter token original (strings, comentários, indentação, operadores, etc.)
        tokens_modificados.append((tok.start, tok.end, tok.string))
        i += 1

    # Reconstrução fiel do código preservando posicionamento exato
    linhas_originais = codigo_jy.splitlines(keepends=True)
    resultado_linhas = []
    
    # Agrupar tokens modificados por linha de início
    from collections import defaultdict
    tokens_por_linha = defaultdict(list)
    for s_pos, e_pos, texto in tokens_modificados:
        tokens_por_linha[s_pos[0]].append((s_pos[1], e_pos[1], texto))

    for num_linha in range(1, len(linhas_originais) + 1):
        linha_orig = linhas_originais[num_linha - 1]
        
        if num_linha not in tokens_por_linha:
            # Linha vazia ou apenas quebra
            resultado_linhas.append(linha_orig)
            continue

        tokens_linha = sorted(tokens_por_linha[num_linha], key=lambda x: x[0])
        
        nova_linha = ""
        col_atual = 0
        
        for s_col, e_col, texto in tokens_linha:
            if s_col > col_atual:
                # Preencher espaços/indentação exata original
                nova_linha += linha_orig[col_atual:s_col]
            nova_linha += texto
            col_atual = max(col_atual, e_col)
            
        if col_atual < len(linha_orig):
            # Adicionar final da linha original (ex: \n ou comentários no fim)
            nova_linha += linha_orig[col_atual:]

        resultado_linhas.append(nova_linha)

    codigo_py = "".join(resultado_linhas)

    # Inclusão opcional do cabeçalho de runtime
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
    Lê um arquivo .jy, transpila para Python e opcionalmente grava o .py correspondente.
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
