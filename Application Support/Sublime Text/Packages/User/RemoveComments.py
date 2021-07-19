import sublime
import sublime_plugin
import re
import sys

class RemoveComments(sublime_plugin.TextCommand):
    def run(self,  edit):
        pass
        # view = self.view
        # sel = view.sel()
        # for region in sel:
        #     while True:
        #         extra_space = view.find(r"(?=.*//)(?!)//(?!.*\")[^\n]*|/\*[\s\S]*\*/", region.begin())
        #         if sel.contains(extra_space):
        #             view.replace(edit, extra_space, "")
        #         else:
        #             break
