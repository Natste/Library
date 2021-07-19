import sublime
import sublime_plugin
import re
import sys

class ReplaceWithSpaces(sublime_plugin.TextCommand):
    def run(self,  edit):
        view = self.view
        sel = view.sel()
        for region in sel:
            for offset in range(region.size()):
                to_be_cleared = view.find(r".", region.begin()+offset)
                view.replace(edit, to_be_cleared, " ")
                # print(f"{region.a} {region.begin()}---{region.b} {region.end()}")
