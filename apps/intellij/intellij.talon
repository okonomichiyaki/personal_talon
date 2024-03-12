os: mac
and app.bundle: com.jetbrains.intellij.ce
-
tag(): user.tabs
tag(): user.splits

# fix for muscle memory double click title bar (intellij bug: https://youtrack.jetbrains.com/issue/IDEA-274588)
duke: key(ctrl-alt-enter)

# window/tab management:
close others: key(ctrl-shift-w)
toggle structure: key(cmd-7)

# navigation:
go top: key(cmd-pageup)
go bottom: key(cmd-pagedown)
go back: key(cmd-[)
go forward: key(cmd-])
go declaration: key(cmd-b)
go usages: key(alt-f7)
(use|usage) last: key(ctrl-alt-up)
(use|usage) next: key(ctrl-alt-down)

# editing

comment this: key(cmd-/)
(import that|suggest that): key(alt-enter)

clear left: edit.delete()
clear word left: key(alt-backspace)

snip line:
  key(up)
  edit.line_end()
  key(right)
  key(shift-down)
  edit.cut()

dupe line:
  key(up)
  edit.line_end()
  key(right)
  key(shift-down)
  edit.copy()
  edit.paste()
  sleep(200ms)
  edit.paste()

# refactoring:
generate code: key(cmd-n)
rename|rename that: key(shift-f6)
replace in path: key(ctrl-shift-r)
safe delete that:
  key(cmd-delete)
  sleep(500ms)
  key(enter)

# run
run (last|again): key(ctrl-r)
run (this|that): key(ctrl-shift-r)

# requires customized keymap:
# split horizontally (from splits tag)
open recent: key(alt-o)
git blame: key(alt-a)
file (hunt|open): key(alt-s)
file hunt <user.text> [over]:
  key(alt-s)
  sleep(500ms)
  insert(text)

# idiosyncratic shortcuts:
cucumber|given when then:
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
drip:
  key(enter)
  ","
