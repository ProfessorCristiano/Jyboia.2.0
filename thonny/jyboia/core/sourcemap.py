"""
Módulo de mapeamento de fontes (SourceMap) e remapeamento de erros/tracebacks.
Converte mensagens de erro do Python para apontar as linhas e termos no arquivo .jy original.
"""

import re
import traceback
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple


@dataclass
class SourceMap:
    """Mapeamento entre o código Jybóia (.jy) e o código Python gerado (.py)."""
    jy_code: str
    py_code: str
    jy_filepath: Optional[str] = None
    py_filepath: Optional[str] = None
    header_lines_count: int = 0
    # Mapeamento de linha py (1-indexed) -> linha jy (1-indexed)
    line_map_py_to_jy: Dict[int, int] = field(default_factory=dict)
    line_map_jy_to_py: Dict[int, int] = field(default_factory=dict)

    def get_jy_line(self, py_line: int) -> int:
        """Obtém a linha no arquivo .jy correspondente à linha do arquivo .py."""
        if py_line in self.line_map_py_to_jy:
            return self.line_map_py_to_jy[py_line]
        # Se houver cabeçalho inserido
        ajustada = py_line - self.header_lines_count
        return max(1, ajustada)

    def get_py_line(self, jy_line: int) -> int:
        """Obtém a linha no arquivo .py correspondente à linha do arquivo .jy."""
        if jy_line in self.line_map_jy_to_py:
            return self.line_map_jy_to_py[jy_line]
        return jy_line + self.header_lines_count


# Dicionário de tradução amigável de tipos de erro em Python
ERROS_TRADUZIDOS: Dict[str, Tuple[str, str]] = {
    "SyntaxError": (
        "Erro de Sintaxe",
        "A estrutura do comando não foi compreendida pelo Jybóia/Python. Verifique se esqueceu dois-pontos (:), parênteses ou aspas.",
    ),
    "IndentationError": (
        "Erro de Indentação",
        "O alinhamento dos espaços no início da linha está incorreto. Verifique os blocos após os dois-pontos (:).",
    ),
    "TabError": (
        "Erro de Tabulação",
        "Mistura de espaços e tabulações na indentação.",
    ),
    "NameError": (
        "Nome Não Reconhecido",
        "Você tentou usar uma variável ou função que ainda não foi definida ou escrita corretamente.",
    ),
    "TypeError": (
        "Erro de Tipo",
        "Operação inválida entre tipos de dados incompatíveis (ex: somar texto com número).",
    ),
    "ValueError": (
        "Erro de Valor",
        "O valor fornecido é inválido para a operação solicitada (ex: converter letras em número).",
    ),
    "ZeroDivisionError": (
        "Divisão por Zero",
        "Tentativa de dividir um número por zero (0), o que é matematicamente impossível.",
    ),
    "IndexError": (
        "Índice Fora do Limite",
        "Tentativa de acessar uma posição que não existe na lista ou texto.",
    ),
    "KeyError": (
        "Chave Não Encontrada",
        "A chave procurada não existe no dicionário.",
    ),
    "AttributeError": (
        "Atributo Não Encontrado",
        "O objeto não possui a função ou atributo solicitado.",
    ),
    "FileNotFoundError": (
        "Arquivo Não Encontrado",
        "O arquivo informado não foi localizado no caminho especificado.",
    ),
    "RecursionError": (
        "Erro de Recursão Infinita",
        "A função chamou a si mesma tantas vezes que estourou o limite de memória.",
    ),
    "KeyboardInterrupt": (
        "Execução Interrompida",
        "O programa foi interrompido pelo usuário.",
    ),
}


def mapear_traceback(tb_str: str, sourcemap: Optional[SourceMap] = None) -> str:
    """
    Processa uma string de traceback do Python, remapeando as linhas e caminhos
    para o arquivo .jy original e adicionando explicações didáticas em português.
    """
    if not tb_str:
        return ""

    linhas = tb_str.splitlines()
    linhas_processadas = []

    # Regex para capturar linhas de traceback: File "...", line 12, in ...
    file_line_regex = re.compile(r'(\s*File\s+")([^"]+)(".*line\s+)(\d+)(.*)')

    for linha in linhas:
        match = file_line_regex.match(linha)
        if match and sourcemap:
            prefix, filepath, middle, line_str, suffix = match.groups()
            py_line = int(line_str)
            jy_line = sourcemap.get_jy_line(py_line)
            
            nome_arquivo = sourcemap.jy_filepath if sourcemap.jy_filepath else "programa.jy"
            linhas_processadas.append(f'{prefix}{nome_arquivo}{middle}{jy_line}{suffix}')
        else:
            linhas_processadas.append(linha)

    # Identificar o erro final e acrescentar explicação didática
    texto_final = "\n".join(linhas_processadas)
    
    for err_name, (titulo_pt, explicacao) in ERROS_TRADUZIDOS.items():
        if err_name in texto_final:
            texto_final += f"\n\n💡 Dica Jybóia [{titulo_pt}]: {explicacao}"
            break

    return texto_final
