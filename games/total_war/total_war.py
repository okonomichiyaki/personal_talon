from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron
from talon.experimental import locate
from user.personal_talon.games.screen_regions import get_from_regions, hold, nop, show_overlay, hide_overlay, WASD5

holding_wasd=False
holding_middle=False
holding_right=False
sliding=False

screen_watcher = None

def start_screen_watcher():
    global screen_watcher
    if screen_watcher:
        return
    def job():
        path="C:\\Users\\michi\\Pictures\\TWW3_end_turn.png"
        matches = locate.locate(path)
        if len(matches) > 0:
            print("found the end turn button")
    screen_watcher = cron.interval("500ms", job)

def focus_handler(window):
    if "Total War: WARHAMMER 3" in window.title:
        start_screen_watcher()

#ui.register("win_focus", focus_handler)

def release_all():
    stop_cron_job()
    for k in ["w","a","s","d","alt"]:
        actions.key(k+":up")
    for b in [0,1,2]:
        actions.mouse_release(b)

hold_functions = [
    [ hold("w","a"), hold("w"),  hold("w","d") ],
    [ hold("a"),     nop,        hold("d")     ],
    [ hold("a","s"), hold("s"),  hold("s","d") ]
]

holding = set()
cron_job = None
current_keys = None

def make_job(region_keys):
    def job():
        global holding
        new_holding = set()
        keys = get_from_regions(region_keys)
        for k in keys:
            new_holding.add(k)
        stop_holding = holding.difference(new_holding)
        for k in stop_holding:
            actions.key(k+":up")
        holding = new_holding
        for k in holding:
            actions.key(k+":down")
    return job

def stop_cron_job():
    global cron_job
    global current_keys
    global holding
    if cron_job:
        cron.cancel(cron_job)
        holding = set()
        for k in ["w","a","s","d","alt"]:
            actions.key(k+":up")
        cron_job = None
        current_keys = None
        hide_overlay()

def start_cron_job(region_keys):
    global cron_job
    global current_keys
    stop_cron_job()
    job = make_job(region_keys)
    cron_job = cron.interval("60ms", job)
    current_keys = region_keys
   # show_overlay(region_keys)

def toggle_wasd():
    if cron_job:
        stop_cron_job()
    else:
        start_cron_job(WASD5)

def start_wasd():
    global holding_wasd
    print("start_wasd")
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
app.name: Warhammer3.exe
app.name: Total War: WARHAMMER 2
app.exe: Warhammer2.exe
"""
@ctx.action_class("user")
class total_war_user:
    def pop():
        if holding_middle or holding_wasd or sliding or holding_right:
            release_all()
        else:
            actions.user.mouse_click_or_zoom()

    def hiss_down():
        toggle_wasd()

    #def hiss_up():
    #    toggle_wasd()
    
    def tw_right_drag():
        toggle_right()

    def tw_pan():
        toggle_middle()
    
    def tw_slide():
        start_slide()

    def tw_release():
        release_all()
