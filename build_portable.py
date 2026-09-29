"""
Script de Criação do Jybóia IDE Portable para Windows.
Gera a distribuição no formato oficial PyInstaller Onedirectory (onedir),
com executável nativo Jyboia.exe, pasta _internal/, pasta samples/ no topo,
Python embutido e isolamento completo via portable_thonny.ini.
"""

import os
import sys
import shutil
import zipfile
import subprocess
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
DIST_DIR = ROOT_DIR / "dist"
TARGET_DIR = DIST_DIR / "Jyboia"
ZIP_FILE = DIST_DIR / "Jyboia-Portable-Windows.zip"
SPEC_FILE = ROOT_DIR / "jyboia.spec"


def log(msg):
    print(f"[*] {msg}", flush=True)


def error(msg):
    print(f"\n[ERRO] {msg}", flush=True)
    sys.exit(1)


def main():
    print("=" * 65)
    print("   Jybóia IDE — Gerador de Pacote Portable Windows (Onedir)    ")
    print("=" * 65)

    # 1. Identificar interpretador Python com PyInstaller
    python_exe = Path(sys.executable).resolve()
    python_dir = python_exe.parent
    log(f"Python em uso: {python_exe}")

    # Verifica PyInstaller
    has_pyinstaller = False
    try:
        res = subprocess.run(
            [str(python_exe), "-m", "PyInstaller", "--version"],
            capture_output=True,
            text=True,
            check=False,
        )
        if res.returncode == 0:
            has_pyinstaller = True
            log(f"PyInstaller detectado: v{res.stdout.strip()}")
    except Exception:
        pass

    if not has_pyinstaller:
        # Tenta encontrar no Thonny ou no ambiente local
        thonny_py = Path(os.environ.get("LOCALAPPDATA", "")) / "Programs" / "Thonny" / "python.exe"
        if thonny_py.exists():
            python_exe = thonny_py
            python_dir = python_exe.parent
            log(f"PyInstaller localizado via Thonny Python: {python_exe}")
            has_pyinstaller = True

    if not has_pyinstaller:
        error(
            "PyInstaller não foi encontrado neste interpretador Python.\n"
            "Instale com: pip install pyinstaller"
        )

    # 2. Limpeza pré-build
    log("Limpando diretórios de build anteriores...")
    if TARGET_DIR.exists():
        shutil.rmtree(TARGET_DIR, ignore_errors=True)

    build_dir = ROOT_DIR / "build" / "jyboia"
    if build_dir.exists():
        shutil.rmtree(build_dir, ignore_errors=True)

    if ZIP_FILE.exists():
        try:
            ZIP_FILE.unlink()
        except Exception:
            pass

    # 3. Compilar com PyInstaller no formato Onedirectory via jyboia.spec
    log(f"Executando PyInstaller com {SPEC_FILE.name} (Modo Onedirectory)...")
    cmd = [
        str(python_exe),
        "-m",
        "PyInstaller",
        "--clean",
        "--noconfirm",
        str(SPEC_FILE),
    ]

    result = subprocess.run(cmd, cwd=str(ROOT_DIR))
    if result.returncode != 0:
        error(f"Falha na compilação com PyInstaller (código de saída {result.returncode}).")

    if not (TARGET_DIR / "Jyboia.exe").exists():
        error(f"O executável Jyboia.exe não foi gerado em {TARGET_DIR}.")

    log("Compilação PyInstaller onedir finalizada com sucesso!")

    # 4. Pós-processamento e enriquecimento do pacote Portable (Onedir)
    log("Configurando estrutura portable no formato Onedir...")

    # 4.1 Marcadores de portabilidade total
    (TARGET_DIR / "portable_thonny.ini").write_text("[general]\n", encoding="utf-8")
    (TARGET_DIR / "jyboia_python.ini").write_text("[general]\n", encoding="utf-8")
    log("Marcadores de portabilidade criados (portable_thonny.ini).")

    # 4.2 Pasta de exemplos na raiz do diretório para os alunos
    samples_src = ROOT_DIR / "samples"
    samples_dest = TARGET_DIR / "samples"
    if samples_src.exists():
        shutil.copytree(samples_src, samples_dest, dirs_exist_ok=True)
        log("Pasta de exemplos (samples/) copiada para a raiz do pacote.")

    # 4.3 Binários python.exe e pythonw.exe para backend autônomo
    for exe_name in ["python.exe", "pythonw.exe"]:
        src_exe = python_dir / exe_name
        if src_exe.exists():
            shutil.copy2(src_exe, TARGET_DIR / exe_name)
    log("Interpretadores auxiliares python.exe/pythonw.exe integrados para o backend.")

    # 4.4 Arquivo ._pth e Lib/ da biblioteca padrão para o python.exe autônomo
    pth_file = TARGET_DIR / f"python{sys.version_info.major}{sys.version_info.minor}._pth"
    pth_file.write_text(".\n_internal\n_internal\\base_library.zip\nimport site\n", encoding="utf-8")
    log(f"Arquivo de caminhos {pth_file.name} criado para o backend autônomo.")

    lib_src = Path(sys.base_prefix) / "Lib"
    if lib_src.exists():
        log("Copiando biblioteca padrão (Lib/) para o backend portátil...")
        shutil.copytree(
            lib_src,
            TARGET_DIR / "Lib",
            ignore=shutil.ignore_patterns("test", "tests", "idlelib", "turtledemo", "__pycache__"),
            dirs_exist_ok=True,
        )

    # 4.5 Garantir que os módulos do Thonny e Jybóia estejam disponíveis para o python.exe
    log("Garantindo código fonte do Jybóia/Thonny para execução via python.exe...")
    shutil.copytree(ROOT_DIR / "thonny", TARGET_DIR / "_internal" / "thonny", dirs_exist_ok=True)
    shutil.copytree(ROOT_DIR / "thonny", TARGET_DIR / "thonny", dirs_exist_ok=True)

    # 4.6 Assets e documentação
    for doc in ["README.md", "MANUAL_USUARIO.md", "TODO.md", "PLANEJAMENTO_PROJETO.md", "logo.ico", "logo.png", "logo-mascote.png"]:
        src_file = ROOT_DIR / doc
        if src_file.exists():
            shutil.copy2(src_file, TARGET_DIR / doc)

    # 4.7 Lançador Batch amigável
    bat_launcher = TARGET_DIR / "Iniciar_Jyboia.bat"
    bat_launcher.write_text(
        "@echo off\r\n"
        "cd /d \"%~dp0\"\r\n"
        "start \"\" \"%~dp0Jyboia.exe\" %*\r\n",
        encoding="utf-8",
    )
    log("Lançador Iniciar_Jyboia.bat gerado.")

    # 5. Compactação em arquivo .zip
    log(f"Criando arquivo compactado para distribuição: {ZIP_FILE.name}...")
    with zipfile.ZipFile(ZIP_FILE, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(TARGET_DIR):
            for file in files:
                abs_file = Path(root) / file
                rel_path = abs_file.relative_to(DIST_DIR)
                zipf.write(abs_file, rel_path)

    if hasattr(sys.stdout, "reconfigure"):
        try:
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        except Exception:
            pass

    print("\n" + "=" * 65)
    print("       BUILD PORTABLE (ONEDIRECTORY) CONCLUIDO COM SUCESSO!     ")
    print(f"  Diretorio Onedir: {TARGET_DIR}")
    print(f"  Arquivo Compactado: {ZIP_FILE}")
    print("=" * 65)
    print("\nEstrutura do pacote Onedirectory:")
    print("  dist/Jyboia/")
    print("  |-- Jyboia.exe              # Executavel nativo principal")
    print("  |-- Iniciar_Jyboia.bat      # Lancador alternativo")
    print("  |-- python.exe / pythonw.exe# Backend Python embutido autonomo")
    print("  |-- portable_thonny.ini     # Isolamento de configuracoes locais")
    print("  |-- samples/                # Codigos de exemplo em .jy e .py")
    print("  \\-- _internal/              # Dependencias, bibliotecas e DLLs")
    print("=" * 65)


if __name__ == "__main__":
    main()
