os: windows
app.name: Titan Two Programming Software
app.name: OBS Studio
-
settings():
    key_wait = 16.0
    key_hold = 16.0

right: key(right)
left: key(left)
up: key(up)
down: key(down)

yes|ok: key(a)
back|cancel|close: key(b)
home: key(h)
auto: key(c)
menu: key(x)
reset camera: key(e)
walk: user.ns_walk()
run: user.ns_run()
pan: user.ns_look()
toggle overlay: user.ns_toggle_overlay()
show empty overlay: user.ns_empty_overlay()
(close|hide) overlay: user.ns_hide_overlay()

key(w): user.pop()
