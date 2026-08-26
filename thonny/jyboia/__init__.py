"""
Jybóia Transpiler Package para Thonny IDE.
"""

from thonny.jyboia.transpiler import transpilar, transpilar_arquivo
from thonny.jyboia.keywords import PALAVRAS_CHAVE, FUNCOES_EMBUTIDAS, TODAS_PALAVRAS_RESERVADAS
from thonny.jyboia.sourcemap import SourceMap, mapear_traceback

__all__ = [
    "transpilar",
    "transpilar_arquivo",
    "PALAVRAS_CHAVE",
    "FUNCOES_EMBUTIDAS",
    "TODAS_PALAVRAS_RESERVADAS",
    "SourceMap",
    "mapear_traceback",
]
