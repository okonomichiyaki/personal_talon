not mode: sleep
-
Japanese|japanese:
    mode.enable("user.japanese")
    mode.disable("command")
hey LipSurf:
    user.mouse_enable_zoom_mouse()
	  user.mouse_disable_control_mouse()
    speech.disable()
    user.history_disable()
snore | snooze:
    speech.disable()
^(the command mode | the man mode | command mode)$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.enable("command")
