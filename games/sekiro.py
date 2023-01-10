import pathlib

from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron
from talon.experimental import locate

path = str(pathlib.Path(__file__).parent.resolve() / "sekiro_corner.png")
locate_job = None

def stop_locate_job():
    global locate_job
    print("stopping locate job")
    if not locate_job:
        return
    cron.cancel(locate_job)
    locate_job = None

def start_locate_job():
    global locate_job
    print("starting locate job")
    if locate_job:
        return
    def job():
        matches = locate.locate(path)
        if len(matches) > 0:
            actions.tracking.control_toggle(True)
            print("found the upper left corner")
        else:
            #actions.tracking.control_toggle(False)
            print("didn't find the upper left corner")
    locate_job = cron.interval("500ms", job)

def focus_handler(window):
    if "Sekiro" in window.title:
        start_locate_job()
    elif locate_job:
        stop_locate_job()

#ui.register("win_focus", focus_handler)
