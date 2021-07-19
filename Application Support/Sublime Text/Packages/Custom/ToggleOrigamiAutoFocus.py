import sublime, sublime_plugin,re

class ToggleOrigamiAutoFocusCommand(sublime_plugin.ApplicationCommand):
    def run(self):
        file ="Origami.sublime-settings"
        key = "auto_zoom_on_focus"
        settings = sublime.load_settings(file)
        current_status = settings.get(key)
        print(current_status)
        if current_status == True:
            settings.set(key, False)
        else:
            settings.set(key, True) 
        settings.set("newkey","newvalue")
        sublime.save_settings(file)
# class ChangeOrigamiFractionCommand(sublime_plugin.ApplicationCommand):
#     # def input(self, fraction = 0.9):
#     #     self.validate(fraction)
#     #     return fraction 
#     def run(self,fraction):
#         file ="Origami.sublime-settings"
#         key = "auto_zoom_on_focus"
#         settings = sublime.load_settings(file)
#         fraction = self.input()
#         settings.set(key, fraction)
#         sublime.save_settings(file)
