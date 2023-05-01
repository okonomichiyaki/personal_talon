import time
from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron

mod = Module()

left_stick_left = mod.setting(
    "gamepad_left_stick_left",
    type=str,
    default="left",
    desc="Set the keyboard binding for the left joystick when pushed left",
)
left_stick_right = mod.setting(
    "gamepad_left_stick_right",
    type=str,
    default="right",
    desc="Set the keyboard binding for the left joystick when pushed right",
)
left_stick_up = mod.setting(
    "gamepad_left_stick_up",
    type=str,
    default="up",
    desc="Set the keyboard binding for the left joystick when pushed up",
)
left_stick_down = mod.setting(
    "gamepad_left_stick_down",
    type=str,
    default="down",
    desc="Set the keyboard binding for the left joystick when pushed down",
)
stick_dead_zone = mod.setting(
    "gamepad_stick_dead_zone",
    type=float,
    default=0.25,
    desc="Set the dead zone threshold for the joysticks (smaller value means smaller dead zone)",
)

last_event = None

def job():
    global last_event

    if not last_event:
        return

    now = time.time() * 1000
    (x, y, t) = last_event

    left = left_stick_left.get()
    right = left_stick_right.get()
    up = left_stick_up.get()
    down = left_stick_down.get()
    dead_zone = stick_dead_zone.get()

    age = now - t
    if (age > 100):
        actions.key(f"{left}:up")
        actions.key(f"{right}:up")
        actions.key(f"{up}:up")
        actions.key(f"{down}:up")
    else:
        if (x > dead_zone):
            actions.key(f"{left}:down")
        elif (x < -1 * dead_zone):
            actions.key(f"{right}:down")
        else:
            actions.key(f"{left}:up")
            actions.key(f"{right}:up")

        if (y > dead_zone):
            actions.key(f"{down}:down")
        elif (y < -1 * dead_zone):
            actions.key(f"{up}:down")
        else:
            actions.key(f"{up}:up")
            actions.key(f"{down}:up")

cron_job = None

def stop_cron_job():
    global cron_job
    if cron_job:
        cron.cancel(cron_job)

def start_cron_job():
    global cron_job
    stop_cron_job()
    cron_job = cron.interval("60ms", job)

@mod.action_class
class Actions:
    def left_xy(x: float, y: float):
        """left_xy"""
        global last_event
        t = time.time() * 1000
        last_event = (x, y, t)

start_cron_job()
