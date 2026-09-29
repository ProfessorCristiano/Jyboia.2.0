# -*- mode: python ; coding: utf-8 -*-
#
# jyboia.spec — Configuração do PyInstaller para gerar o Jybóia IDE Portable
#

import sys
from pathlib import Path
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

block_cipher = None

# Diretório raiz do projeto (onde este .spec está localizado)
ROOT = Path(SPECPATH)

# Coleta automática de todos os submódulos e dados do pacote thonny
thonny_submodules = collect_submodules('thonny')
thonny_data_files = collect_data_files('thonny')

extra_hidden_imports = [
    # Pacote principal e submódulos Jybóia
    'thonny',
    'thonny.main',
    'thonny.workbench',
    'thonny.editors',
    'thonny.running',
    'thonny.shell',
    'thonny.codeview',
    'thonny.tktextext',
    'thonny.ui_utils',
    'thonny.common',
    'thonny.config',
    'thonny.languages',
    'thonny.token_utils',
    'thonny.ast_utils',
    'thonny.jyboia',
    'thonny.jyboia.transpiler',
    'thonny.jyboia.keywords',
    'thonny.jyboia.sourcemap',
    'thonny.jyboia.builtins_runtime',
    
    # Todos os Plugins e Temas do Thonny
    'thonny.plugins',
    'thonny.plugins.tidy_ui_themes',
    'thonny.plugins.base_ui_themes',
    'thonny.plugins.clean_ui_themes',
    'thonny.plugins.classic_ui_themes',
    'thonny.plugins.base_syntax_themes',
    'thonny.plugins.tomorrow_syntax_theme',
    'thonny.plugins.theme_and_font_config_page',
    'thonny.plugins.coloring',
    'thonny.plugins.variables',
    'thonny.plugins.jyboia_python_view',
    'thonny.plugins.about',
    'thonny.plugins.assistant_config_page',
    'thonny.plugins.ast_view',
    'thonny.plugins.autocomplete',
    'thonny.plugins.backend_config_page',
    'thonny.plugins.calltip',
    'thonny.plugins.cells',
    'thonny.plugins.commenting_indenting',
    'thonny.plugins.common_editing_commands',
    'thonny.plugins.debugger',
    'thonny.plugins.editor_config_page',
    'thonny.plugins.event_logging',
    'thonny.plugins.event_view',
    'thonny.plugins.files',
    'thonny.plugins.find_replace',
    'thonny.plugins.general_config_page',
    'thonny.plugins.goto_definition',
    'thonny.plugins.heap',
    'thonny.plugins.highlight_names',
    'thonny.plugins.locals_marker',
    'thonny.plugins.notes',
    'thonny.plugins.object_inspector',
    'thonny.plugins.outline',
    'thonny.plugins.paren_matcher',
    'thonny.plugins.pip_gui',
    'thonny.plugins.problems',
    'thonny.plugins.replayer',
    'thonny.plugins.run_debug_config_page',
    'thonny.plugins.shell_config_page',
    'thonny.plugins.shell_macro',
    'thonny.plugins.statement_boxes',
    'thonny.plugins.terminal_config_page',
    'thonny.plugins.thonny_folders',
    'thonny.plugins.todo_view',
    'thonny.plugins.cpython_backend',
    'thonny.plugins.cpython_backend.cp_back',
    'thonny.plugins.cpython_frontend',
    'thonny.plugins.cpython_frontend.cp_front',

    # Tkinter (GUI)
    'tkinter',
    'tkinter.ttk',
    'tkinter.messagebox',
    'tkinter.filedialog',
    'tkinter.font',
    'tkinter.colorchooser',
    '_tkinter',

    # Dependências externas
    'send2trash',
    'docutils',
    'docutils.parsers',
    'docutils.parsers.rst',
    'packaging',
    'packaging.version',
    'packaging.specifiers',

    # Stdlib usada dinamicamente
    'tokenize',
    'token',
    'ast',
    'queue',
    'threading',
    'subprocess',
    'pkgutil',
    'importlib',
    'importlib.util',
    'importlib.machinery',
    'shutil',
    'traceback',
    'inspect',
    'logging',
]

all_hidden_imports = list(set(thonny_submodules + extra_hidden_imports))

a = Analysis(
    [str(ROOT / 'iniciar_jyboia.py')],
    pathex=[str(ROOT)],
    binaries=[],
    datas=[
        # ── Arquivos de dados do pacote thonny ──────────────────────────────
        (str(ROOT / 'thonny' / 'VERSION'),          'thonny'),
        (str(ROOT / 'thonny' / 'defaults.ini'),     'thonny'),
        (str(ROOT / 'thonny' / 'res'),               'thonny/res'),
        (str(ROOT / 'thonny' / 'locale'),            'thonny/locale'),
        (str(ROOT / 'thonny' / 'plugins'),           'thonny/plugins'),

        # ── Assets visuais da raiz ──────────────────────────────────────────
        (str(ROOT / 'logo.png'),                     '.'),
        (str(ROOT / 'logo.ico'),                     '.'),
        (str(ROOT / 'logo-mascote.png'),             '.'),

        # ── Exemplos .jy para os alunos ─────────────────────────────────────
        (str(ROOT / 'samples'),                      'samples'),
    ] + thonny_data_files,
    hiddenimports=all_hidden_imports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'numpy',
        'PIL',
        'PyQt5',
        'wx',
        'scipy',
        'pandas',
        'IPython',
        'jupyter',
        'notebook',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Jyboia',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    icon=str(ROOT / 'logo.ico'),
    version_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Jyboia',
)
