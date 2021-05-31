from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron

step_job = None
direction = None
mouse_mode = 0
mouse_toggle = False

mod = Module()
@mod.action_class
class Actions:
    def step_forward_continuous():
        """Step forward through game history continuously"""
    def step_backward_continuous():
        """Step backward through game history continuously"""
    def enable_mouse():
        """Enable pop for zoom mouse"""
    def toggle_mouse():
        """Toggle pop for zoom mouse"""

ctx = Context()
ctx.matches = r"""
os: windows
and app.name: Firefox
and title: Game Finished — Mozilla Firefox
"""
@ctx.action_class("user")
class online_go_user:
    def step_forward_continuous():
        """Step forward through game history continuously"""
        global direction
        global mouse_mode
        global mouse_toggle
        mouse_toggle = False
        mouse_mode = 2
        direction = 1
        stop_step()
        start_step()

    def step_backward_continuous():
        """Step backward through game history continuously"""
        global direction
        global mouse_mode
        global mouse_toggle
        mouse_toggle = False
        mouse_mode = 2
        direction = -1
        stop_step()
        start_step()

    def enable_mouse():
        """Enable pop for zoom mouse"""
        global mouse_mode
        mouse_mode = 0
    
    def toggle_mouse():
        """Toggle pop for zoom mouse"""
        global mouse_toggle
        mouse_toggle = not mouse_toggle
    
    def pop():
        global mouse_mode
        if step_job:
            stop_step()
        elif mouse_toggle:
            actions.user.mouse_click_or_zoom()
        elif mouse_mode == 0 or mouse_mode == 1:
            actions.user.mouse_click_or_zoom()
            mouse_mode = mouse_mode + 1
        else:
            step(direction)

    def hiss():
        step(direction)

def step(direction):
    if direction > 0:
        actions.key("right")
    else:
        actions.key("left")

def step_continuous_helper(direction):
    def helper():
        step(direction)
    return helper

def start_step():
    global step_job
    step_job = cron.interval("250ms", step_continuous_helper(direction))

def stop_step():
    global step_job  
    if step_job:
        cron.cancel(step_job)
        step_job = None
