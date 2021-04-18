app.name: IntelliJ IDEA
-
file hunt: user.idea("action SearchEverywhere")
file hunt <user.text> [over]:
  user.idea("action SearchEverywhere")
  sleep(500ms)
  insert(text)
generate code: key(ctrl-n)
rename: key(shift-f6)
