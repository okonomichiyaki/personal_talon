app.exe: warhammer3.exe
-
settings():
    key_wait = 16.0
    key_hold = 16.0
    user.gamepad_left_stick_left = "a"
    user.gamepad_left_stick_right = "d"
    user.gamepad_left_stick_up = "w"
    user.gamepad_left_stick_down = "s"

end turn: key(enter)
pause|paws: key(p)
lord: key(home)

form: user.tw_right_drag()
pan: user.tw_pan()
slide: user.tw_slide()
release all: user.tw_release()
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
    key(shift:down)
    sleep(0.1)
    mouse_click(0)
    key(shift:up)

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

tack view: key(tab)
