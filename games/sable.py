from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron
from talon.experimental import locate

holding = []
# talking = False
# screen_watcher = None

# def start_screen_watcher():
#     global screen_watcher, talking
#     if screen_watcher:
#         return
#     def job():
#         global talking
#         path="C:\\Users\\michiaki\\Pictures\\Sable_answer.png"
#         matches = locate.locate(path)
#         if len(matches) > 0:
#             talking = True
#         else:
#             talking = False
#     screen_watcher = cron.interval("500ms", job)

# def focus_handler(window):
#     if "Sable" in window.title:
#         start_screen_watcher()

# ui.register("win_focus", focus_handler)

def any_holding():
    global holding
    return len(holding) > 0

def release():
    global holding
    if len(holding) > 0:
        key = holding.pop()
        actions.key(key + ":up")

def hold(key):
    global holding
    if key not in holding :
        holding.append(key)
        actions.key(key + ":down")

mod = Module()
@mod.action_class
class Actions:
    def walk_backwards():
        """walk_backwards"""
        hold("s")

    def sprint():
        """sprint"""
        hold("w")
        hold("shift")

    def compass():
        """compass"""
        hold("q")

sable_context = Context()
sable_context.matches = r"""
os: windows
and app.name: Sable.exe
"""
@sable_context.action_class("user")
class sable_user:
    def pop():
        if any_holding():
            release()
        else:
            hold("w")

    def hiss_down():
        hold("space")

    # def hiss_up():
    #     actions.key("space:up")
