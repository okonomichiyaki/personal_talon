tag: terminal
-
list: "ls "
list here: "ls\n"
list up: "ls ..\n"

change [<user.text>]: "cd {text or ''}"
change [<user.text>] tab:
    "cd {text}"
    key(tab)
change home: "cd ~\n"
change up: "cd ..\n"

make direct [<user.text>]: "mkdir {text or ''}"
copy: "cp "
move [<user.text>]: "mv {text or ''}"
up: ".."
remove: "rm "
long arg [<user.text>]: "--{text or ''}"

python: "python "
python mod: "python -m "
python pip: "python -m pip "
python interact: "python \n"
python envy: "pyenv "

bundle exec ruby: "bundle exec ruby "

sig kill: key(ctrl-c)
grep recurse:
    "grep -r '' ."
    key(left:3)
silver search [<user.text>]:
    "ag {text or ''}"
    key(enter)
silver search clipboard:
    "ag '"
    edit.paste()
    "'"
    key(enter)
reverse search [<user.text>]:
    key(ctrl-r)
    "{text or ''}"

abort that:
    edit.line_start()
    "#"
    key(enter)
