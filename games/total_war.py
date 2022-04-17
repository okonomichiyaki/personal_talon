from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron
from user.personal_talon.games.screen_regions import get_from_regions, hold, nop

holding_wasd=False
holding_middle=False
holding_right=False
sliding=False

def release_all():
    global holding_wasd
    global holding_middle
    global holding_right
    global sliding
    for k in ["w","a","s","d","alt"]:
        actions.key(k+":up")
    for b in [0,1,2]:
        actions.mouse_release(b)
    holding_wasd = False
    holding_middle = False
    holding_right = False
    sliding = False

hold_functions = [
    [ hold("w","a"), hold("w"),  hold("w","d") ],
    [ hold("a"),     nop,        hold("d")     ],
    [ hold("a","s"), hold("s"),  hold("s","d") ]
]

def start_wasd():
    global holding_wasd
    get_from_regions(hold_functions)()
    holding_wasd = True

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
    actions.sleep(0.1)
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
app.name: steam_app_779340
app.name: steam_app_594570
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
