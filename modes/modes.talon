not mode: sleep
-
Japanese dictation mode:
    mode.disable("sleep")
    mode.disable("command")
    mode.enable("user.japanese")
    mode.enable("dictation")
    user.code_clear_language_mode()
    mode.disable("user.gdb")

(hay LipSurf | hey LipSurf | snore | talon sleep):
    speech.disable()
    user.history_disable()
talon wake:
    speech.enable()
    user.history_enable()

^(the command mode | the man mode | command mode)$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.enable("command")
