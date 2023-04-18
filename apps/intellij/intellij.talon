os: mac
and app.bundle: com.jetbrains.intellij.ce
-
tag(): user.tabs
tag(): user.splits

# window/tab management:
close others: key(ctrl-shift-w)
toggle structure: key(cmd-7)

# navigation:
go back: key(cmd-[)
go forward: key(cmd-])
go declaration: key(cmd-b)
go usages: key(alt-f7)
(use|usage) last: key(ctrl-alt-up)
(use|usage) next: key(ctrl-alt-down)

# editing
(import that|suggest that): key(alt-enter)
clear left: edit.delete()

# refactoring:
generate code: key(cmd-n)
rename: key(shift-f6)
replace in path: key(ctrl-shift-r)
safe delete that:
  key(cmd-delete)
  sleep(500ms)
  key(enter)

# run
run this: key(ctrl-r)

# requires customized keymap:
# split horizontally (from splits tag)
open recent: key(alt-o)
git blame: key(alt-a)
file hunt: key(alt-s)
file hunt <user.text> [over]:
  key(alt-s)
  sleep(500ms)
  insert(text)

# idiosyncratic shortcuts:
cucumber:
  "// Given "
  key(enter)
  "// When "
  key(enter)
  "// Then "
  key(up)
  key(up)
  edit.line_end()
drop:
  key(enter)
  "."
