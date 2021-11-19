app: jetbrains
-
safe delete that:
    user.idea("action SafeDelete")
    sleep(500ms)
    key(enter)
paste that: key(cmd-v)
select all: key(cmd-a)

close others: key(ctrl-shift-w)
git blame: key(ctrl-shift-a)

punch:
    edit.line_end()
    insert(";")
    key(enter)
pinch:
    edit.line_end()
    insert(";")

hammer string: "String"

open recent:
    key(ctrl-shift-o)

go next: key(shift-alt-down)
go last: key(shift-alt-up)

# live templates:

when then return:
    insert("when then return")
    sleep(200ms)
    key(enter)

four eye:
    insert("fori")
    sleep(200ms)
    key(enter)
