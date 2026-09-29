"""
Plugin do Jybóia IDE: Visualizador de Código Python Traduzido (.py).
Exibe em tempo real o código Python equivalente gerado a partir do código em Português Estruturado (.jy).
"""

import tkinter as tk
from tkinter import ttk

from thonny import get_workbench, ui_utils
from thonny.codeview import CodeView
from thonny.languages import tr
from thonny.jyboia.transpiler import transpilar


class JyboiaPythonPreviewView(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Barra superior com informações e botão de cópia
        self.toolbar = ttk.Frame(self)
        self.toolbar.pack(side="top", fill="x", padx=4, pady=2)

        self.info_label = ttk.Label(
            self.toolbar,
            text="🐍 Python Traduzido (Sincronizado)",
            font="Helvetica 9 bold",
        )
        self.info_label.pack(side="left", padx=2)

        self.copy_button = ttk.Button(
            self.toolbar,
            text="📋 Copiar Python",
            command=self.copiar_codigo,
            width=15,
        )
        self.copy_button.pack(side="right", padx=2)

        # Editor de visualização com Syntax Highlighting nativo
        self.code_view = CodeView(self, font="EditorFont", readonly=True)
        self.code_view.pack(side="bottom", fill="both", expand=True)

        self._scheduled_update = None
        self._last_jy_code = ""

        # Eventos para sincronização
        get_workbench().bind("ActiveEditorChanged", self._on_editor_changed, True)
        get_workbench().bind("Saved", self._on_editor_changed, True)
        get_workbench().bind("Save", self._on_editor_changed, True)
        get_workbench().bind("LocalFileOperation", self._on_editor_changed, True)

        # Agendamento periódico para atualização suave ao digitar
        self._schedule_periodic_check()

    def _schedule_periodic_check(self):
        self.atualizar_preview()
        self.after(500, self._schedule_periodic_check)

    def _on_editor_changed(self, event=None):
        self.atualizar_preview()

    def atualizar_preview(self):
        editor = get_workbench().get_editor_notebook().get_current_editor()
        if not editor:
            self._set_content("# Nenhum arquivo aberto no editor.")
            return

        text_widget = editor.get_text_widget()
        codigo_atual = text_widget.get("1.0", "end-1c")

        if codigo_atual == self._last_jy_code:
            return

        self._last_jy_code = codigo_atual

        if not codigo_atual.strip():
            self._set_content("# Digite seu código em Português Estruturado no editor...")
            return

        try:
            codigo_py, _ = transpilar(codigo_atual, incluir_runtime=False)
            self._set_content(codigo_py)
        except Exception as e:
            self._set_content(f"# Aguardando código válido...\n# ({e})")

    def _set_content(self, text: str):
        text_widget = self.code_view.text
        text_widget.set_read_only(False)
        text_widget.delete("1.0", "end")
        text_widget.insert("1.0", text)
        text_widget.set_read_only(True)

    def copiar_codigo(self):
        codigo = self.code_view.text.get("1.0", "end-1c")
        self.clipboard_clear()
        self.clipboard_append(codigo)
        self.info_label.config(text="✅ Código Python Copiado!")
        self.after(2000, lambda: self.info_label.config(text="🐍 Python Traduzido (Sincronizado)"))


def load_plugin():
    get_workbench().add_view(
        JyboiaPythonPreviewView,
        "Python Traduzido",
        "e",
        default_position_key="zz",
    )
