"""
Funções auxiliares de tempo de execução para programas Jybóia / Python didático.
Permitem leitura tipada e operações facilitadas para iniciantes.
"""

import sys
from typing import Any, Union


def leia_inteiro(prompt: str = "") -> int:
    """Lê um número inteiro do usuário com repetição amigável em caso de erro."""
    while True:
        try:
            valor = input(prompt)
            return int(valor.strip())
        except ValueError:
            print("❌ Erro: Digite um número inteiro válido!", file=sys.stderr)


def leia_real(prompt: str = "") -> float:
    """Lê um número real (float) do usuário com suporte a vírgula ou ponto decimal."""
    while True:
        try:
            valor = input(prompt).strip().replace(",", ".")
            return float(valor)
        except ValueError:
            print("❌ Erro: Digite um número decimal válido (ex: 7.5 ou 7,5)!", file=sys.stderr)


def leia_texto(prompt: str = "") -> str:
    """Lê uma string do usuário."""
    return input(prompt)


# Aliases comuns
leia_int = leia_inteiro
leia_float = leia_real

RUNTIME_HEADER = """# --- Jybóia Runtime Helpers ---
import sys

def leia_inteiro(prompt=""):
    while True:
        try:
            return int(input(prompt).strip())
        except ValueError:
            print("❌ Digite um número inteiro válido!", file=sys.stderr)

def leia_real(prompt=""):
    while True:
        try:
            return float(input(prompt).strip().replace(",", "."))
        except ValueError:
            print("❌ Digite um número decimal válido!", file=sys.stderr)

def leia_texto(prompt=""):
    return input(prompt)

leia_int = leia_inteiro
leia_float = leia_real
# ------------------------------
"""
