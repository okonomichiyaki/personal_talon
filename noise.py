# adapted from: https://github.com/fidgetingbits/knausj_talon/blob/48e57b1b1e7c2d4aa8151bba38c2d57818a14d71/code/noise.py
# this is adapted from @rntz script:
# https://gist.github.com/rntz/914bdb60187858d4a014e82fbcf591c3

import talon
from talon import Module, noise, actions, scripting, ui, app
from typing import Callable, Union, Any
import logging

mod = Module()
@mod.action_class
class Actions:

    def pop(): 
        """pop action overrideable by contexts"""
        actions.user.mouse_click_or_zoom()

    def pop_quick_action_clear():
        """Clears the quick macro"""
        global pop_quick_action
        global pop_quick_action_last
        if pop_quick_action:
            pop_quick_action_last = pop_quick_action
            pop_quick_action = None
            app.notify(subtitle="pop quick action cleared")

    # XXX - it would be nice to have some sort of indicator for this
    # similar to talon_hud stuff
    def pop_quick_action_set():
        """Sets the quick macro"""
        global pop_quick_action
        if len(scripting.core.command_history) > 1:
            pop_quick_action = scripting.core.command_history[-1]
            app.notify(subtitle=f"pop quick action set\n{pop_quick_action}")

    def pop_quick_action_set_last():
        """Sets the quick macro to the previously set action"""
        global pop_quick_action
        global pop_quick_action_last
        pop_quick_action = pop_quick_action_last
        app.notify(subtitle=f"pop quick action set\n{pop_quick_action}")

    def pop_quick_action_run():
        """Runs the quick macro"""
        print(*pop_quick_action)
        scripting.core.CoreActions.run_command(*pop_quick_action)

    def hiss_up():
        """hiss action overrideable by contexts"""
        print("hiss_up")
        pass

    def hiss_down(): 
        """hiss action overrideable by contexts"""
        print("hiss_down")
        pass

    def hiss_quick_action_clear():
        """Clears the quick macro"""
        global hiss_quick_action
        global hiss_quick_action_last
        hiss_quick_action_last = hiss_quick_action
        hiss_quick_action = None

    def hiss_quick_action_set():
        """Sets the quick macro"""
        global hiss_quick_action
        if len(scripting.core.command_history) > 1:
            hiss_quick_action = scripting.core.command_history[-1]
            app.notify(subtitle=f"hiss quick action set\n{pop_quick_action}")

    def hiss_quick_action_set_last():
        """Sets the quick macro to the previously set action"""
        global hiss_quick_action
        global hiss_quick_action_last
        hiss_quick_action = hiss_quick_action_last
        app.notify(subtitle=f"hiss quick action set\n{pop_quick_action}")

    def hiss_quick_action_run():
        """Runs the quick macro"""
        print(*hiss_quick_action)
        scripting.core.CoreActions.run_command(*hiss_quick_action)


ui.register("app_deactivate", lambda app: actions.user.pop_quick_action_clear())
ui.register("win_focus", lambda win: actions.user.pop_quick_action_clear())

pop_quick_action = None
pop_quick_action_last = None
pop_quick_action_history = []
def on_pop(active):
    global pop_quick_action
    if pop_quick_action is None:
        actions.user.pop()
    else:
        actions.user.pop_quick_action_run()

hiss_quick_action = None
hiss_quick_action_last = None
hiss_quick_action_history = []
def on_hiss(active):
    global hiss_quick_action
    if not active:
        actions.user.hiss_up()
    else:
        actions.user.hiss_down()

try:
    noise.register("pop", on_pop)
    # noise.register("hiss", on_hiss)
except talon.lib.cubeb.CubebError as e:
    app.notify("Failed to register pop. Is possible audio error")
    print("Failed to register pop. Is possible audio error")
    print(e)

try:
    noise.register("hiss", on_hiss)
except talon.lib.cubeb.CubebError as e:
    app.notify("Failed to register hiss. Is possible audio error")
    print("Failed to register hiss. Is possible audio error")
    print(e)
