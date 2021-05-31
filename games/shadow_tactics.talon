app.name: Shadow Tactics.exe
-
settings():
    key_wait = 16.0
    key_hold = 16.0

slow: key(f2)

(high jato|jato|hi jato|hiatal): key(1)
(yuki|you I|I|yuuki): key(2)
morgan: key(3)
(tacoma|takuma): key(5)

sword: key(a)
stone: key(d)
socket: key(d)
whistle: key(d)
trap: key(s)
(star|start): key(s)
wind: key(s)

(view cone|you cone|you come|yukon): key(x)
map: key(m)
crouch: key(space)
quick save: key(f5)
quick load: key(f8)
rotate left: key(q)
rotate right: key(e)
mission log: key(b)
bat: skip()
focus: key(w)
highlight: key(h)

pick: key(ctrl:down)

zoom out:
    user.mouse_scroll_down()
    user.mouse_scroll_down()
    user.mouse_scroll_down()
    user.mouse_scroll_down()
    user.mouse_scroll_down()
    user.mouse_scroll_down()
    user.mouse_scroll_down()
    user.mouse_scroll_down()
    user.mouse_scroll_down()
    user.mouse_scroll_down()
    user.mouse_scroll_down()
    user.mouse_scroll_down()

zoom in:
    user.mouse_scroll_up()
    user.mouse_scroll_up()
    user.mouse_scroll_up()
    user.mouse_scroll_up()
    user.mouse_scroll_up()
    user.mouse_scroll_up()
    user.mouse_scroll_up()
    user.mouse_scroll_up()
    user.mouse_scroll_up()
    user.mouse_scroll_up()
    user.mouse_scroll_up()
