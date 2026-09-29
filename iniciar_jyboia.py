"""
Ponto de entrada principal para o Jybóia IDE e runner de processos de backend.
Suporta tanto inicialização da interface gráfica quanto execução como interpretador/backend.
"""

import os
import sys

# Garante que o diretório do projeto esteja no topo do PYTHONPATH
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)


def _dispatch_args():
    # Ignora flags de interpretador padrão do Python passadas para subprocessos
    python_flags = {"-u", "-B", "-s", "-S", "-O", "-OO", "-v", "-E", "-I", "-q"}

    args = sys.argv[1:]
    idx = 0
    while idx < len(args) and args[idx] in python_flags:
        idx += 1

    if idx < len(args):
        first_arg = args[idx]

        # Modo módulo: python -m module_name ...
        if first_arg == "-m" and idx + 1 < len(args):
            import runpy

            mod_name = args[idx + 1]
            sys.argv = [mod_name] + args[idx + 2 :]
            runpy.run_module(mod_name, run_name="__main__", alter_sys=True)
            return True

        # Modo comando: python -c "code" ...
        if first_arg == "-c" and idx + 1 < len(args):
            code = args[idx + 1]
            sys.argv = [sys.argv[0]] + args[idx + 2 :]
            exec(code, {"__name__": "__main__"})
            return True

        # Modo execução de backend interno (cp_launcher.py) ou subprocesso com flags de interpretador
        if "cp_launcher" in first_arg or (idx > 0 and first_arg.endswith(".py")):
            import runpy

            script_path = first_arg
            sys.argv = args[idx:]

            # Se o arquivo não existir diretamente pelo caminho relativo, tenta resolver absoluto
            if not os.path.exists(script_path):
                alt_path = os.path.join(ROOT_DIR, script_path)
                if os.path.exists(alt_path):
                    script_path = alt_path

            runpy.run_path(script_path, run_name="__main__")
            return True

    return False


def _check_environment():
    """Valida se o interpretador Python atual atende aos requisitos minimos do Jyboia."""
    if sys.version_info < (3, 9):
        print("=" * 60)
        print("[ERRO] Python 3.9 ou superior e obrigatorio para executar o Jyboia.")
        print(f"Versao detectada: {sys.version.split()[0]}")
        print("Por favor atualize o Python em https://www.python.org/downloads/")
        print("=" * 60)
        sys.exit(1)

    try:
        import tkinter
    except ImportError:
        print("=" * 60)
        print("[ERRO] O modulo de interface grafica 'tkinter' nao esta instalado.")
        print("No Windows: Reinstale o Python marcando a opcao 'tcl/tk and IDLE'.")
        print("No Ubuntu/Debian: Execute 'sudo apt install python3-tk'.")
        print("No Fedora: Execute 'sudo dnf install python3-tkinter'.")
        print("No Arch Linux: Execute 'sudo pacman -S tk'.")
        print("=" * 60)
        sys.exit(1)


if __name__ == "__main__":
    if not _dispatch_args():
        _check_environment()
        from thonny.main import run

        sys.exit(run())
