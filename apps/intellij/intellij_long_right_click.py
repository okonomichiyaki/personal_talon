import time

from talon import Context, ctrl

ctx = Context()
ctx.matches = 'app: jetbrains'
@ctx.action_class('main')
class Actions:
    def mouse_click(button: int=0):
        """click right mouse button, holding it down a little bit longer"""
        print("mouse long right")
        if button == 1:
            ctrl.mouse_click(button=button, hold=200)
        else:
            ctrl.mouse_click(button=button)
