from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron
from user.personal_talon.misc.unreal_mouse_look import surround_key_with_console

mod = Module()
@mod.action_class
class Actions:
    def pk_reality():
        """toggle reality"""
        print("pk reality")
        surround_key_with_console("x")

    def pk_interact():
        """press E key"""
        print("pk interact")
        surround_key_with_console("e")

    def pk_close():
        """press Q key"""
        print("pk close")
        surround_key_with_console("q")

    def pk_auto_walk():
        """press backslash key"""
        print("pk auto walk")
        surround_key_with_console("\\")

mod = Module()
ctx = Context()
ctx.matches = r"""
os: windows
and app.name: Paradise Killer
"""
@ctx.action_class("user")
class paradise_killer_user:   
    def pop():
        print("pk pop")
        surround_key_with_console("\\")

    def hiss_up():
        print("pk hiss up")
        #surround_key_with_console("space")
