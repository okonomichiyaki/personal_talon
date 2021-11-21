from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron

midy=1080/2
thirdx=1920/3

def do_wasd():
    x, y = ctrl.mouse_pos()
    print("x:",x,"y:",y)
    if (y < midy and x > thirdx and x < 2*thirdx):
        actions.key("w")
    elif (y > midy and x > thirdx and x < 2*thirdx):
        actions.key("s")
    elif (x < thirdx):
        actions.key("a")
    elif (x > 2*thirdx):
        actions.key("d")

mod = Module()
ctx = Context()
ctx.matches = r"""
os: windows
and app.name: Inscryption.exe
"""
@ctx.action_class("user")
class inscryption_user:
    def hiss():
        do_wasd()

    def pop():
        do_wasd()
