from talon import ctrl, ui, Module, Context, actions, clip, app, noise, cron
from user.personal_talon import mouse

step_job = None
direction = 1
mouse_toggle = False

mod = Module()
@mod.action_class
class Actions:
    def direction_forward():
        """Change direction to forward"""
    def direction_backward():
        """Change direction to backward"""
    def step():
        """Step through game history one move"""
    def step_continuous():
        """Step through game history continuously"""
    def toggle_mouse():
        """Toggle pop for zoom mouse"""

ctx = Context()
ctx.matches = r"""
title: Game Finished
app: firefox
"""
@ctx.action_class("user")
class online_go_user:
    def direction_forward():
        """Change direction to forward"""
        global direction
        direction = 1

    def direction_backward():
        """Change direction to backward"""
        global direction
        direction = -1

    def step():
        """Step through game history one move"""
        step(direction)

    def step_continuous():
        """Step through game history continuously"""
        global mouse_mode
        global mouse_toggle
        mouse_toggle = False
        mouse_mode = 2
        stop_step()
        start_step()

    def toggle_mouse():
        """Toggle pop for zoom mouse"""
        global mouse_toggle
        mouse_toggle = not mouse_toggle

    def noise_trigger_pop():
        global mouse_mode
        if step_job:
            stop_step()
        elif mouse_toggle:
            mouse.click_or_zoom_or_stop_scroll()
        else:
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
