from talon import actions,ui,cron

watcher = None
wanikani = False

def check_title():
    title = actions.win.title()
    return "WaniKani / Reviews" in title or "WaniKani / Recent Mistakes" in title

def check_and_toggle():
    global wanikani
    if check_title() and not wanikani:
        print("WaniKani: disabling speech")
        wanikani = True
        actions.speech.disable()
    elif not check_title() and wanikani:
        wanikani = False
        print("WaniKani: enabling speech")
        actions.speech.enable()

def stop_watcher():
    global watcher
    if not watcher:
        return
    cron.cancel(watcher)
    watcher = None

def start_watcher():
    global watcher
    if watcher:
        return
    watcher = cron.interval("500ms", check_and_toggle)

def focus_handler(window):
    global watcher
    check_and_toggle()
    if "Google Chrome" in actions.win.title():
        start_watcher()
    else:
        stop_watcher()

ui.register("win_focus", focus_handler)
