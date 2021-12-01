from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron

hiss=False

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

def hold_wasd():
    x, y = ctrl.mouse_pos()
    print("(hold) x:",x,"y:",y)
    if (y < midy and x > thirdx and x < 2*thirdx):
        actions.key("w:down")
    elif (y > midy and x > thirdx and x < 2*thirdx):
        actions.key("s:down")
    elif (x < thirdx):
        actions.key("a:down")
    elif (x > 2*thirdx):
        actions.key("d:down")

def release_wasd():
    actions.key("w:up")
    actions.key("s:up")
    actions.key("a:up")
    actions.key("d:up")

def wasd():
    global hiss
    if hiss:
        release_wasd()
        hiss=False
    else:
        hold_wasd()
        hiss=True
 
mod = Module()
ctx = Context()
ctx.matches = r"""
os: windows
and app.name: Inscryption.exe
"""
@ctx.action_class("user")
class inscryption_user:
    def hiss_down():
        hold_wasd()
    
    def hiss_up():
        release_wasd()

    def pop():
        do_wasd()
