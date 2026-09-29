#!/usr/bin/env python3
"""
Script de automação para geração do pacote Jybóia 2.0 Universal / Multiplataforma.
Gera uma versão leve em dist/Jyboia-Universal para computadores que já possuem Python instalado
(Windows, Linux e macOS), incluindo launchers inteligentes de detecção do interpretador.
"""

import os
import shutil
import stat
import sys
import zipfile
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent
DIST_DIR = ROOT_DIR / "dist"
TARGET_DIR = DIST_DIR / "Jyboia-Universal"
ZIP_FILE = DIST_DIR / "Jyboia-Universal.zip"


def log(msg: str) -> None:
    print(f"[*] {msg}")


def error(msg: str) -> None:
    print(f"[ERRO] {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> None:
    print("=" * 65)
    print("    GERADOR DO PACOTE JYBOIA 2.0 UNIVERSAL (MULTIPLATAFORMA)    ")
    print("=" * 65)

    DIST_DIR.mkdir(parents=True, exist_ok=True)

    # 1. Limpeza de builds anteriores
    if TARGET_DIR.exists():
        log(f"Removendo build universal anterior em {TARGET_DIR.name}...")
        shutil.rmtree(TARGET_DIR, ignore_errors=True)

    if ZIP_FILE.exists():
        try:
            ZIP_FILE.unlink()
        except Exception:
            pass

    TARGET_DIR.mkdir(parents=True, exist_ok=True)

    # 2. Copia do pacote principal do Jybóia / Thonny
    log("Copiando pacote thonny/ e módulos do Jybóia...")
    shutil.copytree(
        ROOT_DIR / "thonny",
        TARGET_DIR / "thonny",
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc", "*.pyo", "test", "tests"),
        dirs_exist_ok=True,
    )

    # 3. Copia dos exemplos didáticos (samples/)
    samples_src = ROOT_DIR / "samples"
    if samples_src.exists():
        log("Copiando códigos didáticos de exemplo (samples/)...")
        shutil.copytree(samples_src, TARGET_DIR / "samples", dirs_exist_ok=True)

    # 4. Copia dos inicializadores multiplataforma
    launchers = ["iniciar_jyboia.py", "iniciar_jyboia.bat", "iniciar_jyboia.sh"]
    for l_name in launchers:
        src = ROOT_DIR / l_name
        dest = TARGET_DIR / l_name
        if src.exists():
            if l_name.endswith(".sh"):
                # Garante quebras de linha Unix (\n)
                content = src.read_bytes().replace(b"\r\n", b"\n")
                dest.write_bytes(content)
                # Permissão de execução no Linux/macOS
                try:
                    dest.chmod(dest.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
                except Exception:
                    pass
            else:
                shutil.copy2(src, dest)
            log(f"Lançador incluído: {l_name}")

    # 5. Marcador de portabilidade para manter dados isolados em user_data/
    (TARGET_DIR / "portable_thonny.ini").write_text("[general]\n", encoding="utf-8")
    log("Marcador portable_thonny.ini adicionado.")

    # 6. Documentação, configurações e dependências
    support_files = [
        "pyproject.toml",
        "requirements.txt",
        "README.md",
        "MANUAL_USUARIO.md",
        "TODO.md",
        "PLANEJAMENTO_PROJETO.md",
        "logo.ico",
        "logo.png",
        "logo-mascote.png",
    ]
    for sf in support_files:
        src = ROOT_DIR / sf
        if src.exists():
            shutil.copy2(src, TARGET_DIR / sf)

    log("Documentação e assets integrados ao pacote.")

    # 7. Compactação em formato ZIP
    log(f"Compactando pacote em {ZIP_FILE.name}...")
    with zipfile.ZipFile(ZIP_FILE, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(TARGET_DIR):
            for file in files:
                abs_file = Path(root) / file
                rel_path = abs_file.relative_to(DIST_DIR)
                zip_info = zipfile.ZipInfo.from_file(abs_file, str(rel_path))
                # Preserva permissões de execução para scripts shell no ZIP
                if file.endswith(".sh"):
                    zip_info.external_attr = 0o755 << 16
                zipf.writestr(zip_info, abs_file.read_bytes())

    size_mb = ZIP_FILE.stat().st_size / (1024 * 1024)

    print("\n" + "=" * 65)
    print("     BUILD UNIVERSAL (MULTIPLATAFORMA) CONCLUIDO COM SUCESSO!   ")
    print(f"  Diretório:          {TARGET_DIR}")
    print(f"  Arquivo Compactado: {ZIP_FILE} ({size_mb:.2f} MB)")
    print("=" * 65)
    print("\nComo executar:")
    print("  • Windows: Clique duplo em 'iniciar_jyboia.bat'")
    print("  • Linux / macOS: No terminal, execute './iniciar_jyboia.sh'")
    print("  • Terminal direto: 'python iniciar_jyboia.py'")
    print("=" * 65)


if __name__ == "__main__":
    main()
