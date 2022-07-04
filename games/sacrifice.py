from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron
from talon.experimental import locate

holding = False

def toggle_walk():
    global holding
    if holding:
        actions.key("up:up")
    else:
        actions.key("up:down")
    holding = not holding

mod = Module()
@mod.action_class
class Actions:
    def log_mouse():
        """log_mouse"""
        x, y = ctrl.mouse_pos()
        print("current mouse position:",x,y)

sable_context = Context()
sable_context.matches = r"""
os: windows
and app.exe: Sacrifice.exe
"""
@sable_context.action_class("user")
class Sacrifice:
    def pop():
            toggle_walk()
