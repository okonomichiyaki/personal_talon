from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron

state="Normal"

def surround_key_with_console(key):
    if state == "Normal":
        actions.key(key)
    elif state == "Open":
        actions.key("escape")
        actions.key(key)
        actions.key("`")

mod = Module()
@mod.action_class
class Actions:
    def pk_reset():
        """reset the stored state of the console"""
        print("pk reset")
        global state
        state="Normal"

    def pk_interact():
        """press E key"""
        print("pk interact")
        surround_key_with_console("e")

    def pk_close():
        """press Q key"""
        print("pk close")
        surround_key_with_console("q")

    def pk_menu():
        """press escape key"""
        print("pk menu")
        surround_key_with_console("escape")

    def pk_toggle_console():
        """toggles the console based on the stored state"""
        global state
        print("pk toggle console")
        if state == "Normal":
            actions.key("`")
            state = "Open"
        elif state == "Open":
            actions.key("escape")
            state = "Normal"
    
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
        surround_key_with_console("space")
