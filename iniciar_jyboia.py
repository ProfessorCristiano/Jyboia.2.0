"""
Ponto de entrada principal para iniciar o Jybóia IDE.
"""

import os
import sys

# Garante que o diretório do projeto esteja no topo do PYTHONPATH
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from thonny.main import run

if __name__ == "__main__":
    sys.exit(run())
