from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron
from .unreal_mouse_look import surround_key_with_console

running=False
def toggle_running():
    global running
    if running:
        actions.key("shift:up")
        running=False
    else:
        actions.key("shift:down")
        running=True

mod = Module()
ctx = Context()
ctx.matches = r"""
os: windows
and app.name: Call of Cthulhu
os: windows
and app.exe: CallOfCthulhu.exe
"""
@ctx.action_class("user")
class call_of_cthulhu_user:   
    def pop():
        actions.user.unreal_toggle_walk()

    def hiss_up():
        toggle_running()
