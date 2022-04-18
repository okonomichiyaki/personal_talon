from talon import Module, Context, ui, actions, ctrl
from typing import Optional

mod = Module()
ctx = Context()
ctx.matches = r"""
os: mac
"""
@ctx.action_class("user")
class Actions:
    def screenshot(screen_number: Optional[int] = None):
        """Takes a screenshot of the entire screen using the normal mac keyboard shortcut"""
        actions.key("shift-cmd-3")

    def screenshot_window():
        """Takes a screenshot of the active window using the normal mac keyboard shortcut"""
        win = ui.active_window()
        actions.key("shift-cmd-4")
        actions.sleep(0.1)
        actions.key("space")
        ctrl.mouse_move(win.rect.x + win.rect.width / 2, win.rect.y + win.rect.height / 2)
        ctrl.mouse_click(button=0, hold=16000)
