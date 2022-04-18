app.name: IntelliJ IDEA
app.name: Android Studio
-
file hunt: user.idea("action SearchEverywhere")
file hunt <user.text> [over]:
  user.idea("action SearchEverywhere")
  sleep(500ms)
  insert(text)
generate code: key(cmd-n)
rename: key(shift-f6)
(import that|suggest that): key(alt-enter)
replace in path: key(ctrl-shift-r)
cucumber:
  "// Given "
  key(enter)
  "// When "
  key(enter)
  "// Then "
  key(up)
  key(up)
  edit.line_end()

(use|usage) last: key(ctrl-alt-up)
(use|usage) next: key(ctrl-alt-down)

drop:
  key(enter)
  "."

#crimp:
