import sublime
import sublime_plugin
import re
import sys

# def run_on_selections(view, edit, func):
#     settings = sublime.load_settings(SETTINGS_FILE)
#     detectAcronyms = settings.get("detect_acronyms", True)
#     useList = settings.get("use_acronyms_list", True)
#     if useList:
#         acronyms = settings.get("acronyms", [])
#     else:
#         acronyms = False

#     for s in view.sel():
#         region = s if s else view.word(s)

#         text = view.substr(region)
#         # Preserve leading and trailing whitespace
#         leading = text[:len(text)-len(text.lstrip())]
#         trailing = text[len(text.rstrip()):]
#         new_text = leading + func(text.strip(), detectAcronyms, acronyms) + trailing
#         if new_text != text:
#             view.replace(edit, region, new_text)

class ReduceToSingleLines(sublime_plugin.TextCommand):
    def run(self,  edit):
        view = self.view
        sel = view.sel()
        for region in sel:
            while True:
                only_space = view.find(r"(?<=\n) *(?=\n)", region.begin())
                # if sel.contains(only_space):
                view.replace(edit, only_space, "")
                extra_line = view.find(r"\n{2,}", region.begin())
                # if sel.contains(extra_line):
                view.replace(edit, extra_line, "\n")
                # else:
                    # break
                if not sel.contains(extra_line):
                    break
