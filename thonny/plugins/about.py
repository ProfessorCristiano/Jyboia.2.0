# -*- coding: utf-8 -*-

import datetime
import platform
import sys
import tkinter as tk
import tkinter.font
from logging import getLogger
from tkinter import ttk

import thonny
from thonny import get_workbench, ui_utils
from thonny.common import get_python_version_string
from thonny.languages import tr
from thonny.ui_utils import CommonDialog, CommonDialogEx, create_url_label, get_hyperlink_cursor

logger = getLogger(__name__)


class AboutDialog(CommonDialogEx):
    def __init__(self, master):
        super().__init__(master)

        self.title("Sobre o Jybóia")
        self.resizable(height=tk.FALSE, width=tk.FALSE)

        default_heading_font = tkinter.font.nametofont("TkHeadingFont")
        heading_font = default_heading_font.copy()
        heading_font.configure(size=int(default_heading_font["size"] * 1.7), weight="bold")
        
        heading_label = ttk.Label(
            self.main_frame, text="🐍 Jybóia IDE " + thonny.get_version(), font=heading_font
        )
        heading_label.grid(pady=(self.get_large_padding(), self.get_small_padding()))

        jyboia_desc = ttk.Label(
            self.main_frame,
            text="*Jybóia 2.0*\nCriada por Professor Cristiano Teixeira como Fork do Thonny IDE",
            justify=tk.CENTER,
            font="TkDefaultFont 9 bold",
        )
        jyboia_desc.grid(pady=(0, 2))

        jyboia_url_label = create_url_label(
            self.main_frame,
            "https://github.com/ProfessorCristiano/Jyboia.2.0",
            "Projeto disponível em: https://github.com/ProfessorCristiano/Jyboia.2.0",
            justify=tk.CENTER,
        )
        jyboia_url_label.grid(pady=(0, self.get_small_padding()))

        original_header = ttk.Label(
            self.main_frame,
            text="Original em: https://thonny.org",
            justify=tk.CENTER,
            font="TkDefaultFont 8 italic",
        )
        original_header.grid(pady=(0, self.get_small_padding()))

        if sys.platform == "linux":
            try:
                import distro
                system_desc = distro.name(True)
            except ImportError:
                system_desc = "Linux"

            if "32" not in system_desc and "64" not in system_desc:
                system_desc += self.get_os_word_size_suffix()
        elif sys.platform == "darwin":
            mac_ver = platform.mac_ver()[0]
            mac_arch = platform.mac_ver()[2]
            system_desc = f"macOS {mac_ver} ({mac_arch})"
        else:
            release = platform.release()
            if sys.platform == "win32":
                try:
                    build = int(platform.version().split(".")[2])
                    if release == "10" and build >= 22000:
                        release = "11"
                except Exception:
                    logger.exception("Could not determine Windows version")

            system_desc = platform.system() + " " + release + self.get_os_word_size_suffix()

        platform_label = ttk.Label(
            self.main_frame,
            justify=tk.CENTER,
            text=system_desc
            + "\n"
            + "Python "
            + get_python_version_string()
            + "\n"
            + "Tk "
            + ui_utils.get_tk_version_str(),
        )
        platform_label.grid(pady=self.get_medium_padding())

        credits_label = create_url_label(
            self.main_frame,
            "https://github.com/thonny/thonny/blob/master/CREDITS.rst",
            tr(
                "Made in\n"
                + "University of Tartu, Estonia,\n"
                + "with the help from\n"
                + "open-source community,\n"
                + "Raspberry Pi Foundation\n"
                + "and Cybernetica AS"
            ),
            justify=tk.CENTER,
        )
        credits_label.grid()

        default_font = tkinter.font.nametofont("TkDefaultFont")
        license_font = default_font.copy()
        license_font.configure(size=round(default_font["size"] * 0.7))
        license_label = ttk.Label(
            self.main_frame,
            text="Copyright (©) "
            + str(datetime.datetime.now().year)
            + " Aivar Annamaa\n"
            + tr(
                "This program comes with\n"
                + "ABSOLUTELY NO WARRANTY!\n"
                + "It is free software, and you are welcome to\n"
                + "redistribute it under certain conditions, see\n"
                + "https://opensource.org/licenses/MIT\n"
                + "for details"
            ),
            justify=tk.CENTER,
            font=license_font,
        )
        license_label.grid(pady=self.get_medium_padding())

        ok_button = ttk.Button(
            self.main_frame, text=tr("OK"), command=self.on_close, default="active"
        )
        ok_button.grid(pady=(0, self.get_large_padding()))
        ok_button.focus_set()

        self.bind("<Return>", self.on_close, True)

    def get_os_word_size_suffix(self):
        if "32" in platform.machine() and "64" not in platform.machine():
            return " (32-bit)"
        else:
            return ""


def load_plugin() -> None:
    def open_about():
        ui_utils.show_dialog(AboutDialog(get_workbench()))

    def open_url(url):
        import webbrowser
        webbrowser.open(url)

    get_workbench().add_command(
        "changelog",
        "help",
        tr("Version history"),
        lambda: open_url("https://github.com/thonny/thonny/blob/master/CHANGELOG.rst"),
        group=60,
    )
    get_workbench().add_command(
        "issues",
        "help",
        tr("Report problems"),
        lambda: open_url("https://github.com/ProfessorCristiano/Jyboia.2.0/issues"),
        group=60,
    )
    get_workbench().add_command("about", "help", "Sobre o Jybóia", open_about, group=61)

    # For Mac
    get_workbench().createcommand("tkAboutDialog", open_about)
