from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron

ctx = Context()
ctx.matches = r"""
os: windows
and app.name: KaijuWars.exe
"""
@ctx.action_class("user")
class sable_user:
    def hiss_down():
        actions.mouse_click(1)

    # def hiss_up():
    #     actions.key("space:up")
