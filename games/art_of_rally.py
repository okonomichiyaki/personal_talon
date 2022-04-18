from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron

hiss=False

midy=1080/2
thirdx=1920/3

def hold_wasd():
    x, y = ctrl.mouse_pos()
    print("(hold) x:",x,"y:",y)
    if (x < thirdx):
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
os: linux
and app.name: artofrally_demo.x64
"""
@ctx.action_class("user")
class rally_user:
    def hiss_down():
        wasd()
    
    def hiss_up():
        wasd()

    def pop():
        pass
