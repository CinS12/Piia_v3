import ctypes

from pubsub import pub

from Controller import C_Setup
from Model import M_LanguageSelection
from View import V_LanguageSelection
import tkinter as tk
class LanguageSelection:
    def __init__(self, parent):
        self.lang = ""
        self.parent = parent
        pub.subscribe(self.lang_selected, "LANG_SELECTED")

        self.view_lang = V_LanguageSelection.ViewLanguageSelection(parent)
        self.model_lang = M_LanguageSelection.ModelLanguageSelection()
        self.check_language()
        return
    def check_language(self):
        lang = self.model_lang.loadSelected()
        if lang["selected"] == "":
            self.view_lang.ask_lang()
        else:
            print(lang)
            lang = lang["selected"]
            self.lang = lang
            pub.sendMessage("LANG_OK_LOADED")

    def lang_selected(self, lang):
        self.lang = lang
        self.model_lang.updateSelected(lang)
        print(lang)
        pub.sendMessage("LANG_OK_ASKED")