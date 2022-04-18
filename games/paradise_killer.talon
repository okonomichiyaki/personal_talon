os: windows
and app.name: Paradise Killer
-
tag(): unreal
settings():
    key_wait = 16.0
    key_hold = 16.0

walk|auto walk: user.pk_auto_walk()
pickup|interact|examine|talk|open|use: user.pk_interact()
close: user.pk_close()
alt reality|reality: user.pk_reality()
