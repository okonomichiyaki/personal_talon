not mode: sleep
-
japanese:
    mode.enable("user.japanese")
    mode.disable("command")
(hay LipSurf | hey LipSurf | snore | snooze):
    speech.disable()
^(the command mode | the man mode | command mode)$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.enable("command")
