from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron

walking = False
zooming = False

def stop_zoom():
    global zooming
    actions.user.mouse_scroll_stop()
    zooming = False

def start_zoom(direction):
    global zooming
    zooming = True
    if direction > 0:
        actions.user.mouse_scroll_up_continuous()
    else:
        actions.user.mouse_scroll_down_continuous()

def toggle_walk():
    global walking
    if walking:
        actions.key("w:up")
    else:
        actions.key("w:down")
    walking = not walking

mod = Module()
@mod.action_class
class Actions:
    def ug_zoom_in():
        """ug_zoom_in"""
        print("ug_zoom_in")
    
    def ug_zoom_out():
        """ug_zoom_out"""
        print("ug_zoom_out")

ctx = Context()
ctx.matches = r"""
os: windows
and app.name: Umurangi Generation.exe
"""
@ctx.action_class("user")
class umurangi_generation_user:
    # def hiss_down():
    #     actions.key("space")
    
    def pop():
        if zooming:
            stop_zoom()
        else:
            toggle_walk()
    
    def ug_zoom_in():
        print("ug_zoom_in")
        start_zoom(1)
    
    def ug_zoom_out():
        print("ug_zoom_out")
        start_zoom(-1)
