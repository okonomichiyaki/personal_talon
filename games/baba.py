from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron
from user.personal_talon.games.screen_regions import ScreenRegions, TAP_ARROWS3

screen_regions = ScreenRegions(TAP_ARROWS3)

ctx = Context()
ctx.settings["key_hold"] = 16
ctx.settings["key_wait"] = 16
ctx.matches = r"""
os: windows
and app.name: Baba Is You
os: windows
and app.exe: Baba Is You.exe
"""
@ctx.action_class("user")
class baba_user:
    def noise_trigger_pop():
        print("baba noise")
        screen_regions.do()
