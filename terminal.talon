tag: terminal
-

bundle exec ruby: "bundle exec ruby"
#paste that: key(cmd-v)

change [<user.text>]: "cd {text or ''}"
change [<user.text>] tab:
    "cd {text}"
    key(tab)
change home: "cd ~\n"
change up: "cd ..\n"
change talon: "cd ~/.talon/user/knausj_talon/"

sig kill: key(ctrl-c)
grep recurse:
    "grep -r '' ."
    key(left)
    key(left)
    key(left)
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

find by name: "find . -name "

make direct [<user.text>]: "mkdir {text or ''}"
copy: "cp "
move [<user.text>]: "mv {text or ''}"
up: ".."
remove: "rm "

abort that:
    key(ctrl-a)
    "#"
    key(enter)
