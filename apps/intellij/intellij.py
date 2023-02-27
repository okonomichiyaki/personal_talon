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
        for part in parts:
            if "." in part:
                return part
        return title

@ctx.action_class('main')
class Actions:
    def mouse_click(button: int=0):
        """click right mouse button, holding it down a little bit longer"""
        if button == 1:
            ctrl.mouse_click(button=button, hold=200)
        else:
            ctrl.mouse_click(button=button)
