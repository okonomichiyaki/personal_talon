from talon import Module, actions
mod = Module()
mod.mode("throttle", "throttle mode")
@mod.action_class
class Actions:
    def enable_throttle():
        "enable throttle mode"
        actions.mode.enable("user.throttle")
