#!/usr/bin/env bash
# ====================================================
#            Iniciando Jyboia IDE 2.0 (Linux / macOS)
# ====================================================

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR" || exit 1

PYTHON_CMD=""

# 1. Procura candidatos compativeis de Python (versao >= 3.9)
for cand in python3 python3.14 python3.13 python3.12 python3.11 python3.10 python3.9 python; do
    if command -v "$cand" >/dev/null 2>&1; then
        if "$cand" -c "import sys; exit(0 if sys.version_info >= (3, 9) else 1)" >/dev/null 2>&1; then
            PYTHON_CMD="$cand"
            break
        fi
    fi
done

if [ -z "$PYTHON_CMD" ]; then
    echo "============================================================"
    echo "[ERRO] Nao foi possivel encontrar o Python 3.9+ no sistema."
    echo "============================================================"
    echo "Instale o Python 3.9 ou superior usando o gerenciador de pacotes:"
    echo "  - Ubuntu / Debian:  sudo apt update && sudo apt install python3 python3-tk"
    echo "  - Fedora / RHEL:    sudo dnf install python3 python3-tkinter"
    echo "  - Arch Linux:       sudo pacman -S python tk"
    echo "  - openSUSE:         sudo zypper install python3 python3-tk"
    echo "  - macOS:            brew install python python-tk"
    echo ""
    exit 1
fi

# 2. Valida suporte a interface grafica (Tkinter)
if ! "$PYTHON_CMD" -c "import tkinter" >/dev/null 2>&1; then
    echo "============================================================"
    echo "[AVISO] Modulo de interface grafica (Tkinter) nao encontrado!"
    echo "============================================================"
    echo "O Jyboia IDE requer a biblioteca Tkinter para exibir sua interface."
    echo ""
    echo "Para instalar:"
    echo "  - Ubuntu / Debian:  sudo apt install python3-tk"
    echo "  - Fedora:           sudo dnf install python3-tkinter"
    echo "  - Arch Linux:       sudo pacman -S tk"
    echo "  - openSUSE:         sudo zypper install python3-tk"
    echo "  - macOS:            brew install python-tk"
    echo ""
    exit 1
fi

# 3. Executa o Jyboia IDE
exec "$PYTHON_CMD" "$SCRIPT_DIR/iniciar_jyboia.py" "$@"
