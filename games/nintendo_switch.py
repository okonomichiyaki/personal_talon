from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron
from user.personal_talon.games.screen_regions import tap, hold, short_hold, get_index, call_region

walk_job = None
holding = set()

functions = [
    [ tap("left"),     short_hold("m"),  tap("up")       ],
    [ short_hold("j"), tap("a"),         short_hold("k") ],
    [ tap("down"),     short_hold("n"),  tap("right")    ]
]
hold_functions = [
    [ hold("j","m"),    hold("m"),  hold("m","k")      ],
    [ hold("j"),      tap("a"),   hold("k")      ],
    [ hold("j","n"),    hold("n"),  hold("n","k")   ]
]

walk_region_keys = [
    [ ["j","m"], ["m"], ["m","k"]  ],
    [ ["j"],     [],    ["k"]      ],
    [ ["j","n"], ["n"], ["n","k"] ]
]
look_region_keys = [
    [ ["o","u"], ["o"], ["o","i"]  ],
    [ ["u"],     [],    ["i"]      ],
    [ ["u","p"], ["p"], ["i","p"] ]
]

def make_job(region_keys):
    def job():
        global holding
        new_holding = set()
        i, j = get_index(3, 3)
        for k in region_keys[j][i]:
            new_holding.add(k)
        stop_holding = holding.difference(new_holding)
        for k in stop_holding:
            actions.key(k+":up")
        holding = new_holding
        for k in holding:
            actions.key(k+":down")
    return job

def release_all():
    global holding
    print("release all")
    for k in ["j","k","n","m","u","i","o","p"]:
        actions.key(k+":up")
    holding = set()

def stop_walk():
    global walk_job
    print("stop walk")
    if walk_job:
        cron.cancel(walk_job)
        release_all()
        walk_job = None

def start_walk():
    global walk_job
    print("start walk")
    stop_walk()
    job = make_job(walk_region_keys)
    walk_job = cron.interval("60ms", job)

def start_look():
    global walk_job
    print("start look")
    stop_walk()
    job = make_job(look_region_keys)
    walk_job = cron.interval("60ms", job)

mod = Module()
@mod.action_class
class Actions:
    def ns_walk(): 
        """Nintendo switch walk action overrideable by contexts"""
        print("ns walk action")
    
    def ns_look(): 
        """Nintendo switch look action overrideable by contexts"""
        print("ns look action")

ctx = Context()
ctx.matches = r"""
os: windows
app.name: Titan Two Programming Software
app.name: OBS Studio
"""
@ctx.action_class("user")
class nintendo_switch_user:
    def pop():
        global walk_job
        if walk_job:
            stop_walk()
        else:
            call_region(3, 3, functions)

    def ns_walk():
        start_walk()

    def ns_look():
        start_look()
