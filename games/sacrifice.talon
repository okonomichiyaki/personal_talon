os: windows
and app.exe: Sacrifice.exe
-
settings():
    key_wait = 16.0
    key_hold = 16.0
    user.mouse_continuous_scroll_amount = 300
zoom out:
    user.mouse_scroll_down()
    repeat(10)
zoom in:
    user.mouse_scroll_up()
    repeat(10)
pause|paws: key(ctrl-p)
menu: key(escape)
convert: key(c)
structure: key(ctrl-s)
creation: key(ctrl-c)
mana lith: key(m)
mana hore: key(n)
druid: key(ctrl-d)
ranger: key(ctrl-r)
shrike: key(ctrl-s)
wrath: key(ctrl-w)
scarab: key(ctrl-c)
