app.name: steam_app_779340
app.name: steam_app_594570
-
settings():
    key_wait = 16.0
    key_hold = 16.0

end turn: key(enter)
pause|paws: key(p)
#zoom out: key(tab)

form: user.tw_right_drag()
pan: user.tw_pan()
slide: user.tw_slide()
release: user.tw_release()
charge:
    mouse_click(1)
    mouse_click(1)
move: mouse_click(1)
group one: key(ctrl-1)
group two: key(ctrl-2)
group three: key(ctrl-3)
group four: key(ctrl-4)
group five: key(ctrl-5)

in pick:
    key(shift:down)
    sleep(0.1)
    mouse_click(0)
    key(shift:up)

tick pick:
    key(ctrl:down)
    sleep(0.1)
    mouse_click(0)
    key(ctrl:up)

wheel tick down: skip()
wheel tick up: skip()
wheel downer: skip()
wheel upper: skip()

zoom in:
    key(z:down)
    sleep(0.2)
    key(z:up)

zoom out:
    key(x:down)
    sleep(0.2)
    key(x:up)
