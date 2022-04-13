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
walk: user.ns_walk()
pan: user.ns_look()
