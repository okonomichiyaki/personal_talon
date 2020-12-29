app.name: Per Aspera.exe
-
settings():
    key_wait = 16.0
    key_hold = 16.0
    user.mouse_hide_mouse_gui = 1

# speed
pause: key(space)
play: key(1)
faster: key(3)
fastest: key(5)

# camera
reset: key(x)
zoom: user.mouse_scroll_up_continuous()
zoom out: user.mouse_scroll_down_continuous()
up:
  key(w:down)
  sleep(0.2)
  key(w:up)
down:
  key(s:down)
  sleep(0.2)
  key(s:up)
right:
  key(d:down)
  sleep(0.2)
  key(d:up)
left:
  key(a:down)
  sleep(0.2)
  key(a:up)
tick up: key(w)
tick down: key(s)
tick right: key(d)
tick left: key(a)

# modes
scanner: key(f4)
maintenance: key(f3)
power: key(f2)
traffic: key(f1)
