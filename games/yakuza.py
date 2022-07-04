from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron

holding = False

mod = Module()
ctx = Context()
ctx.matches = r"""
os: windows
and app.name: Yakuza0.exe
os: windows
and app.exe: Yakuza0.exe
"""
@ctx.action_class("user")
class yakuza_user:
    def pop():
        global holding
        if holding:
            actions.key("shift:up")
            actions.key("w:up")
            holding = False
        else:
            actions.key("shift:down")
            actions.key("w:down")
            holding = True

