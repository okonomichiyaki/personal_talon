
san san|sam sam:
    key(enter)
    key(enter)

floppy disk: edit.save()
floppy: edit.save()
throttle mode: user.enable_throttle()

lip surf:
    key(ctrl-shift-s)
    speech.disable()
    user.history_disable()

glue that: edit.paste()

copy under:
    mouse_click()
    mouse_click()
    edit.copy()
(glue|paste) under:
    mouse_click()
    mouse_click()
    edit.paste()
clear under:
    mouse_click()
    mouse_click()
    edit.delete()

tab replace:
    app.tab_close()
    app.tab_open()

# miscellaneous misfires:
caret: skip()
go nine: edit.line_end()
home bar: ", "

# misfires and replacements from pop to click:
#one: skip()
itchy: key(1)
#two: skip()
knee: key(2)
#four: skip()
yawn: key(4)
#eight: skip()
hatch: key(8)
#off: skip()
