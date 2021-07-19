import sublime
from sublime_plugin import EventListener
# import re

cmdstr = "build"
argstr = {"build_system": 'Packages/PackageDev/Package/Convert to ....sublime-build', "variant": "JSON"}

class UserListeners(EventListener):
        @staticmethod
        def on_post_save(view):
            if "/.config/karabiner" in view.file_name():
                sublime.active_window().run_command(cmdstr, argstr)
