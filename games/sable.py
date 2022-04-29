from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron
from talon.experimental import locate

holding = False
talking = False
screen_watcher = None

def start_screen_watcher():
    global screen_watcher, talking
    if screen_watcher:
        return
    def job():
        global talking
        path="C:\\Users\\michi\\Pictures\\Sable_answer.png"
        matches = locate.locate(path)
        if len(matches) > 0:
            talking = True
        else:
            talking = False
    screen_watcher = cron.interval("500ms", job)

def focus_handler(window):
    if "Sable" in window.title:
        start_screen_watcher()

ui.register("win_focus", focus_handler)

def toggle_walk():
    global holding
    print("toggle_walk", holding)
    if holding:
        for k in ["shift","w","s","q"]:
            actions.key(k + ":up")
    else:
        actions.key("w:down")
    holding = not holding

mod = Module()
@mod.action_class
class Actions:
    def walk_backwards():
        """walk_backwards"""
        global holding
        actions.key("s:down")
        holding = True

    def sprint():
        """sprint"""
        actions.key("shift:down")

    def compass():
        """compass"""
        global holding
        actions.key("q:down")
        holding = True

sable_context = Context()
sable_context.matches = r"""
os: windows
and app.name: Sable.exe
"""
@sable_context.action_class("user")
class sable_user:
    def pop():
        print("pop", talking)
        if talking:
            actions.user.mouse_click_or_zoom()
        else:
            toggle_walk()

    def hiss_down():
        print("sable hiss_down")
        actions.key("a:down")

    def hiss_up():
        print("sable hiss_up")
        actions.key("a:up")

obs_context = Context()
obs_context.matches = r"""
os: windows
and app.name: OBS Studio
os: windows
and app.exe: obs64.exe
"""
@obs_context.action_class("user")
class obs:
    # def pop():
    #     actions.user.switcher_focus("Sable")
    #     toggle_walk()

    def hiss_down():
        actions.user.switcher_focus("Sable")
        #actions.key("space")
