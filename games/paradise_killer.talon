os: windows
and app.name: Paradise Killer
-
settings():
    key_wait = 16.0
    key_hold = 16.0

reset: user.pk_reset()
look: user.pk_toggle_console()
walk|auto walk: user.pk_auto_walk()
pickup|interact|examine: user.pk_interact()
close: user.pk_close()
menu: user.pk_menu()
