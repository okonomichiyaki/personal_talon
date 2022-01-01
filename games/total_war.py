from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron

holding_wasd=False
holding_middle=False
holding_right=False
sliding=False

thirdy=1080/3
thirdx=1920/3

def release_all():
    global holding_wasd
    global holding_middle
    global holding_right
    global sliding
    actions.key("w:up")
    actions.key("s:up")
    actions.key("a:up")
    actions.key("d:up")
    actions.key("alt:up")
    actions.mouse_release(0)
    actions.mouse_release(1)
    actions.mouse_release(2)
    holding_wasd = False
    holding_middle = False
    holding_right = False
    sliding = False

def hold_wasd(key):
    global holding_wasd
    actions.key(key + ":down")
    holding_wasd = True

def start_wasd():
    x, y = ctrl.mouse_pos()
    if (y < thirdy and x > thirdx and x < 2*thirdx):
        hold_wasd("w")
    elif (y > 2*thirdy and x > thirdx and x < 2*thirdx):
        hold_wasd("s")
    elif (x < thirdx):
        hold_wasd("a")
    elif (x > 2*thirdx):
        hold_wasd("d")

def toggle_wasd():
    global holding_wasd
    x, y = ctrl.mouse_pos()
    print("(hold) x:",x,"y:",y)

    if holding_wasd:
        release_all()
    elif (y < thirdy and x > thirdx and x < 2*thirdx):
        hold_wasd("w")
    elif (y > 2*thirdy and x > thirdx and x < 2*thirdx):
        hold_wasd("s")
    elif (x < thirdx):
        hold_wasd("a")
    elif (x > 2*thirdx):
        hold_wasd("d")
    #else:
        #actions.user.mouse_click_or_zoom()

def toggle_middle():
    global holding_middle
    if holding_middle:
        actions.mouse_release(2)
    else:
        actions.mouse_drag(2)
    holding_middle = not holding_middle

def toggle_right():
    global holding_right
    if holding_right:
        actions.mouse_release(1)
    else:
        actions.mouse_drag(1)
    holding_right = not holding_right

def start_slide():
    global sliding
    actions.key("alt:down")
    actions.mouse_drag(0)
    sliding = True

mod = Module()
@mod.action_class
class Actions:
    def tw_pan(): 
        """pan action overrideable by contexts"""
        print("pan action")
    
    def tw_slide():
        """slide action overrideable by contexts"""
        print("slide action")

    def tw_release():
        """release action overrideable by contexts"""
        print("release action")

    def tw_right_drag():
        """right mouse drag action overrideable by contexts"""
        print("right mouse drag action")

ctx = Context()
ctx.matches = r"""
os: linux
and app.name: TotalWarhammer2
"""
@ctx.action_class("user")
class total_war_user:
    def pop():
        if holding_middle or holding_wasd or sliding or holding_right:
            release_all()
        else:
            actions.user.mouse_click_or_zoom()

    def hiss_down():
        start_wasd()

    def hiss_up():
        release_all()
    
    def tw_right_drag():
        toggle_right()

    def tw_pan():
        toggle_middle()
    
    def tw_slide():
        start_slide()

    def tw_release():
        release_all()
