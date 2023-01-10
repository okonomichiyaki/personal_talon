from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron
import time

last_pop_time = 0

mod = Module()
ctx = Context()
ctx.matches = r"""
os: windows
and app.name: Breach.exe
os: windows
and app.exe: Breach.exe
"""
@ctx.action_class("user")
class breach_user:
    def hiss_down():
        actions.tracking.control_toggle()

#    def pop():
#        global last_pop_time
#        now = time.time() * 1000
#        diff = now - last_pop_time
#        last_pop_time = now
#        if diff < 200:
#            actions.tracking.control_toggle()
#        else:
#            actions.user.mouse_click_or_zoom()
