import sublime
import sublime_plugin
import re
import traceback
from subprocess import call

def _print(v):
    print("~≈==≈~~≈==≈~~≈==≈~~≈==≈~\n\n{}\n\n~≈==≈~~≈==≈~~≈==≈~~≈==≈~".format(v))

def _view_texdoc(file):
    command = ["texdoc", "--view"]
    command.append(file)
    call(command)


class TexDocumentationPackageUnderCaret(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        sel = view.sel()
        for region in sel:
            word = view.word(region)
            word_str = view.substr(word)
            _view_texdoc(word_str)
