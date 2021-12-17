from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron

unreal_console_open=False
unreal_walking=False
unreal_should_reopen=False

def surround_key_with_console(key):
    if unreal_console_open:
        actions.key("escape")
        actions.key(key)
        actions.key("`")
    else:
        actions.key(key)

def start_walking():
    global unreal_walking
    actions.key("w:down")
    unreal_walking=True

def stop_walking():
    global unreal_walking
    actions.key("w:up")
    unreal_walking=False

def close_console():
    global unreal_console_open
    actions.key("escape")
    unreal_console_open=False

def open_console():
    global unreal_console_open
    actions.key("`")
    unreal_console_open=True

mod = Module()
mod.tag("unreal", "unreal engine dev console based mouse look")

@mod.action_class
class Actions:
    def unreal_toggle_walk():
        """toggle walking in a game without auto walk"""
        print("unreal toggle walk")
        global unreal_should_reopen
        if unreal_console_open:
            close_console()
            unreal_should_reopen=True
        if unreal_walking:
            stop_walking()
            if unreal_should_reopen:
                open_console()
                unreal_should_reopen=False
        else:
            start_walking()

    def unreal_reset():
        """reset the stored state of the console"""
        global unreal_console_open
        unreal_console_open=False

    def unreal_menu():
        """press escape key"""
        surround_key_with_console("escape")
    
    def unreal_e_key():
        """press E key"""
        surround_key_with_console("e")

    def unreal_ctrl_key():
        """press ctrl key"""
        surround_key_with_console("ctrl")

    def unreal_toggle_console():
        """toggles the console based on the stored state"""
        global unreal_console_open
        if unreal_console_open:
            actions.key("escape")
            unreal_console_open = False
        else:
            actions.key("`")
            unreal_console_open = True
