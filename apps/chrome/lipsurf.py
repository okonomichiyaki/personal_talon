from talon import actions,ui

lipsurf = False

def focus_handler(window):
    global lipsurf
    if "Google Chrome" in window.title:
        print("[LipSurf] disabling speech")
        lipsurf = True
        actions.speech.disable()
    elif lipsurf:
        lipsurf = False
        print("[LipSurf] enabling speech")
        actions.speech.enable()

ui.register("win_focus", focus_handler)
