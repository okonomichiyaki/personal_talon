os: mac
tag: terminal
-
go line start: key(ctrl-a)
go line end: key(ctrl-e)
copy line:
  edit.line_start()
  "echo \""
  edit.line_end()
  "\" | pbcopy"
