tag: terminal
-
change [<user.text>]: "cd {text or ''}"
change home: "cd ~\n"
change up: "cd ..\n"
change talon: "cd ~/.talon/user/knausj_talon/"

silver search [<user.text>]:
    "ag {text or ''}"
    key(enter)
silver search clipboard:
    "ag '"
    key(cmd-v)
    "'"
    key(enter)
reverse search [<user.text>]:
    key(ctrl-r)
    "{text or ''}"

go line start: key(ctrl-a)
go line end: key(ctrl-e)
copy line:
    key(ctrl-a)
    "echo \""
    key(ctrl-e)
    "\" | pbcopy"
