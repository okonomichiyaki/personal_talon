floppy disk: edit.save()
floppy: edit.save()
alt tab:
    key(alt:down)
    key(ctrl:down)
    key(tab)
    key(alt:up)
    key(ctrl:up)
throttle mode: user.enable_throttle()

lip surf:
    key(ctrl-shift-s)
    speech.disable()
    user.history_disable()

copy under:
    mouse_click()
    mouse_click()
    edit.copy()
paste under:
    mouse_click()
    mouse_click()
    edit.paste()

# miscellaneous misfires:
caret: skip()
go nine: edit.line_end()

# misfires and replacements from pop to click:
one: skip()
itchy: key(1)
two: skip()
knee: key(2)
four: skip()
yawn: key(4)
eight: skip()
hatch: key(8)
off: skip()
