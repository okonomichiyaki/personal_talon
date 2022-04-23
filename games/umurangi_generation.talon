os: windows
and app.name: Umurangi Generation.exe
-
settings():
    key_wait = 16.0
    key_hold = 16.0

menu: key(escape)
change|pickup: key(e)
crouch: key(c)

walk: key(w:down)
run:
    key(shift:down)
    key(w:down)
hop:
    key(space)
    key(w)
inch: key(w)
inch back: key(s)

zoom in: user.ug_zoom_in()
zoom out: user.ug_zoom_out()
wheel tick down: skip()
wheel tick up: skip()
wheel downer: skip()
wheel upper: skip()

folk in:
    key(shift:down)
    user.mouse_scroll_up()
    key(shift:up)
folk out:
    key(shift:down)
    user.mouse_scroll_down()
    key(shift:up)
