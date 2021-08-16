import sublime
import sublime_plugin
import re
import sys




class ReduceToSingleSpaces(sublime_plugin.TextCommand):
    def space_replace(self, edit):
        view = self.view
        sel = view.sel()
        pstr = lambda _rej: print(f"region: «{view.substr(_rej)}»\nlength: {len(view.substr(_rej))}")
        # i=0

        for region in sel:
            inner_spaces = view.find_all(r"(?<!^)(?<=\S)(?: {2,}?(?=\S))", region.begin())
            inner_spaces.reverse()
            for s in inner_spaces:
                view.replace(edit, s, " ")

            [pstr(es) for es in inner_spaces]

            trailing_space = view.find(r" +(?=\n?$)", region.begin())
            view.replace(edit, trailing_space, "")
            # extra_spaces = [*inner_spaces, trailing_space]







            # print(view.substr(region)) 
            # if i > 10:
            #     break
            # for es in  extra_spaces:
            #     # es = extra_spaces.pop(0)
            #     replacement = "" if es == trailing_space else " "
            #     j+=1
            #     if j > 10:
            #         break
            #     print(region.contains(es))
            #     if region.contains(es) and es:
            #         print("*")
            #         view.replace(edit, es, replacement)
            #     else: break


    def run(self,  edit):
        self.space_replace(edit)
        # view = self.view
        # sel = view.sel()
        # i=0
        # for region in sel:
        #     extra_space = view.find(r"(?<!^)(?<=\S) {2,}(?=$|\S)", region.begin())
        #     # trailing_space = view.find(r" +(?=\n?$)", region.begin())
        #     # while True:
        #         # if region.contains(trailing_space):
        #         #     view.replace(edit, trailing_space, "")
        #             # continue
        #     i+=1
        #     j=0
        #     while sel.contains(extra_space):
        #         j+=1
        #         print([i,j]) 
        #         view.replace(edit, extra_space, " ")
        #         # else:
        #         #     break
