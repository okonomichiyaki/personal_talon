tag: terminal
-
change [<user.text>]: "cd {text or ''}"
change home: "cd ~\n"
change up: "cd ..\n"
change talon: "cd ~/.talon/user/knausj_talon/"

reverse search [<user.text>]:
    key(ctrl-r)
    "{text or ''}"

curl <user.text> <number> <user.text>: "curl {text_1}:{number}/{text_2}"

go line start: key(ctrl-a)
go line end: key(ctrl-e)
copy line:
    key(ctrl-a)
    "echo \""
    key(ctrl-e)
    "\" | pbcopy"

#query param <user.text> <user.text>: 