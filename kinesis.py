from talon import ctrl, Module

mod = Module()
@mod.action_class
class Actions:
    def kinesis_left_pedal_down():
        """overrideable action for kinesis left pedal down"""
        ctrl.mouse_click(2, down=True)

    def kinesis_left_pedal_up():
        """overrideable action for kinesis left pedal up"""
        ctrl.mouse_click(2, up=True)
