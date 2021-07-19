import sublime
import sublime_plugin
import re
import sys

class ReduceToSingleSpaces(sublime_plugin.TextCommand):
    def run(self,  edit):
        view = self.view
        sel = view.sel()
        for region in sel:
            while True:
                trailing_space = view.find(r" +(?=\n)", region.begin())
                if region.contains(trailing_space):
                    view.replace(edit, trailing_space, "")
                    continue
                extra_space = view.find(r"(?<!^)(?<=\S) {2,}(?=$|\S)", region.begin())
                if sel.contains(extra_space):
                    view.replace(edit, extra_space, " ")
                else:
                    break
