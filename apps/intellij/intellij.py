import time
from talon import Context, actions, ctrl

ctx = Context()
ctx.matches = """
os: mac
and app.bundle: com.jetbrains.intellij.ce
"""

@ctx.action_class("win")
class WinActions:
    def filename():
        title = actions.win.title()
        parts = title.split(" ")
        result = title
        for part in parts:
            if "." in part:
                result = part
                break
        return result

@ctx.action_class('main')
class Actions:
    def mouse_click(button: int=0):
        """click right mouse button, holding it down a little bit longer"""
        if button == 1:
            ctrl.mouse_click(button=button, hold=200)
        else:
            ctrl.mouse_click(button=button)

@ctx.action_class('user')
class UserActions:
    def split_window_horizontally():
        actions.key('alt-h')

