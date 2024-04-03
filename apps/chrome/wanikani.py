from talon import actions,ui

wanikani = False

def focus_handler(window):
    global wanikani
    if "WaniKani / Reviews" in window.title:
        print("WaniKani reviews: disabling speech")
        wanikani = True
        actions.speech.disable()
    elif wanikani:
        wanikani = False
        print("WaniKani reviews: enabling speech")
        actions.speech.enable()

ui.register("win_focus", focus_handler)
