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
run: key(shift:down w:down)
hop: key(space w)
dub hop: key(space space w)

inch: key(w)
inch left: key(a)
inch right: key(d)
inch back: key(s)

zoom in: user.ug_zoom_in()
zoom out: user.ug_zoom_out()
folk in:
    key(shift:down)
    user.ug_zoom_in()
folk out:
    key(shift:down)
    user.ug_zoom_out()

wheel tick down: skip()
wheel tick up: skip()
wheel downer: skip()
wheel upper: skip()
