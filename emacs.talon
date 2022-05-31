app.exe: emacs.exe
-
tag(): editor
tag(): user.tabs
tag(): user.splits
tag(): user.line_commands


run python: user.emacs_command("run-python")
python load file: key(ctrl-c ctrl-l enter)

# ----- GENERAL ----- #
save and quit | save buffers kill emacs: user.emacs_command("s-b-k-e")
suplex: key(ctrl-x)
exchange: key(ctrl-x ctrl-x)
# "execute" previously named "command", but this caused lots of problems
execute: key(alt-x)
execute <user.text>$:
  key(alt-x)
  user.insert_formatted(text, "DASH_SEPARATED")
evaluate: key(alt-:)
prefix: key(ctrl-u)
prefix <number_small>: user.emacs_prefix(number_small)

reflow: key(alt-q)
toggle read only: key(ctrl-x ctrl-q)
occurs: key(ctrl-c o)
multi occurs: key(ctrl-c shift-o)
directory: key(ctrl-x ctrl-j)
other [window] directory: key(ctrl-x 4 ctrl-j)
other [window] scroll [down]: key(alt-pagedown)
other [window] scroll up: key(alt-pageup)
insert unicode: key(ctrl-x 8 enter)

manual: user.emacs_command("man")
customize variable: user.emacs_command("customize-variable")
customize group: user.emacs_command("customize-group")
customize face: user.emacs_command("customize-face")
[toggle] line numbers: user.emacs_command("d-nu")
visual line mode: user.emacs_command("visu-l-m")
highlight line mode: user.emacs_command("hl-l-m")
auto fill mode: user.emacs_command("auto-f")
describe (char|character): user.emacs_command("desc-char")
browse kill ring: user.emacs_command("b-ri")

emacs record: key("ctrl-x (")
emacs stop: key("ctrl-x )")
emacs play: key(ctrl-x e)

recenter: key(ctrl-u ctrl-l)
center [<number_small> from] top:
  user.emacs_prefix(number_small or 0)
  key(ctrl-l)
center [<number_small> from] bottom:
  number = number_small or 0
  user.emacs_prefix(-1-number)
  key(ctrl-l)

# ----- HELP ----- #
apropos:
  user.emacs_help()
  key(a)
describe (fun|function):
  user.emacs_help()
  key(f)
describe key:
  user.emacs_help()
  key(k)
describe key briefly:
  user.emacs_help()
  key(c)
describe symbol:
  user.emacs_help()
  key(o)
describe variable:
  user.emacs_help()
  key(v)
describe mode:
  user.emacs_help()
  key(m)

describe (fun|function) <user.text>$:
  user.emacs_help()
  key(f)
  user.insert_formatted(text, "DASH_SEPARATED")
  key(enter)
describe symbol <user.text>$:
  user.emacs_help()
  key(o)
  user.insert_formatted(text, "DASH_SEPARATED")
  key(enter)  
describe variable <user.text>$:
  user.emacs_help()
  key(v)
  user.insert_formatted(text, "DASH_SEPARATED")
  key(enter)


# ----- BUFFERS & WINDOWS ----- #
switch: key(ctrl-x b)
switch back: key(ctrl-x b enter)

other [window] switch:
  key(ctrl-x 4 b)
[other [window]] display:
  key(ctrl-x 4 ctrl-o)
other [window] switch back: key(ctrl-x 4 b enter)
[other [window]] display back: key(ctrl-x 4 ctrl-o enter)

[split|tab] rebalance: key(ctrl-x +)
tab shrink: key(ctrl-x -)
tab grow: key(ctrl-x ^)
tab grow <number_small>:
  user.emacs_prefix(number_small)
  key(ctrl-x ^)
tab shrink <number_small>:
  amount = number_small or 1
  user.emacs_prefix(0 - amount)
  key(ctrl-x ^)

file open: key(ctrl-x ctrl-f)
file hunt: key(ctrl-x c l)
file rename: user.emacs_command("rename-file")
other [window] file open: key(ctrl-x 4 ctrl-f)
(file | buffer) close: key(ctrl-c k)
buffer kill: key(ctrl-x k)
buffer bury: user.emacs_command("bur")
buffer revert | revert buffer: user.emacs_command("rev-buf")
buffer finish: key(ctrl-x ctrl-s ctrl-x #)
buffer list | switch: key(ctrl-x b)
buffer next: key(ctrl-x right)
buffer last: key(ctrl-x left)

diff (buffer | [buffer] with file):
  user.emacs_command("d-b-w")
  key(enter)
kill buffers matching file name: user.emacs_command("k-b-m-f")
other [window] quit: key(ctrl-c q)


# ----- MOTION AND EDITING ----- #
cut line: key(home alt-1 ctrl-k)
auto indent: key(alt-ctrl-\)

mark: key(ctrl-space)
go back: key(ctrl-u ctrl-space)
global [go] back: key(ctrl-x ctrl-@)

page mark: key(ctrl-x ctrl-p)
next page | page next: key(ctrl-x ])
last page | page last: key(ctrl-x [)
next error | error next: key(alt-g n)
last error | error last: key(alt-g p)

sentence right: key(alt-e)
sentence left: key(alt-a)
sentence kill: key(alt-k)
term left: key(alt-ctrl-b)
term right: key(alt-ctrl-f)
term up: key(esc ctrl-up)
term down: key(esc ctrl-down)
term kill: key(esc ctrl-k)
term mark: key(esc ctrl-space)
term copy: key(escape ctrl-space alt-w)
graph kill: user.emacs_command("kill-par")
graph up: key(alt-p)
graph down: key(alt-n)
graph mark: key(alt-h)
graph copy: key(alt-h alt-w)
graph cut: key(alt-h ctrl-w)

# could call these "pull", as they pull the thing behind point forward
transpose [word|words]: key(alt-t)
transpose (term|terms): key(ctrl-alt-t)
transpose (char|chars): key(ctrl-t)
transpose (line|lines): key(ctrl-x ctrl-t)
transpose (sentence|sentences): user.emacs_command("tr-sen")
transpose (graph|graphs|paragraphs): user.emacs_command("tr-par")

register (copy|save): key("ctrl-x r s")
register (paste|insert): key("ctrl-x r i")
register jump: key(ctrl-x r j)

# ----- smerge minor mode -----
merge next: key("ctrl-c ^ n")
merge last: key("ctrl-c ^ p")
merge keep upper: key("ctrl-c ^ u")
merge keep lower: key("ctrl-c ^ l")
merge keep this: key("ctrl-c ^ enter")
merge refine: key("ctrl-c ^ R")
merge split: key("ctrl-c ^ r")


# ----- SEARCH & REPLACE ----- #
#action(edit.find): key(ctrl-s)
action(user.find_reverse): key(ctrl-r)
#action(edit.find_next): key(ctrl-s)
#action(edit.find_previous): key(ctrl-r)

search regex: key(alt-ctrl-s)
search regex back: key(alt-ctrl-r)
replace: key(alt-%)
replace regex: key(alt-ctrl-%)
search buffer:
  key(ctrl-home)
  edit.find()
search buffer regex: key(ctrl-home alt-ctrl-s)
replace buffer: key(ctrl-home alt-%)
replace regex buffer: key(ctrl-home ctrl-alt-%)
# TODO: this only works for search not for replace! :(
search toggle (regex | regular | pattern): key(alt-r)
search toggle word: key(alt-s w)
search edit: key(alt-e)


# ----- TALON ACTIONS ----- #
#action(code.toggle_comment): user.emacs_command("comment-dwim")
action(edit.line_swap_down): key(down ctrl-x ctrl-t up)
action(edit.line_swap_up): key(ctrl-x ctrl-t up:2)
#action(edit.line_clone): key(ctrl-a ctrl-k ctrl-y enter ctrl-y home)

#action(edit.word_left): key(alt-b)
#action(edit.word_right): key(alt-f)
#action(edit.extend_word_left): key(shift-alt-b)
#action(edit.extend_word_right): key(shift-alt-f)
#action(edit.select_all): key(ctrl-x h)
# indent_{more,less} work on the current region, but knausj expects them to
# operate on the current line if there is no selection. no easy way to do this.
action(edit.indent_more):
  user.emacs_prefix(4)
  key(ctrl-x tab)
action(edit.indent_less):
  user.emacs_prefix(-4)
  key(ctrl-x tab)
#action(edit.zoom_in): key(ctrl-x ctrl-+)
#action(edit.zoom_out): key(ctrl-x ctrl--)
#action(edit.zoom_reset): key(ctrl-x ctrl-0)

#action(edit.save): key(ctrl-x ctrl-s)
#action(edit.copy): key(alt-w)
#action(edit.cut): key(ctrl-w)
#action(edit.paste): key(ctrl-y)
#action(edit.undo): key(ctrl-_)

#action(app.tab_next): key("ctrl-x o")
#action(app.tab_previous):
#  user.emacs_prefix(-1)
#  key("ctrl-x o")
#action(app.tab_close): key("ctrl-x 0")
#action(app.tab_open): key("ctrl-x 2")
#action(app.window_open): key(ctrl-x 5 2)

#action(user.split_window): key(ctrl-x 2)
#action(user.split_window_vertically): key(ctrl-x 2)
#action(user.split_window_horizontally): key(ctrl-x 3)
#action(user.split_next): key("ctrl-x o")
#action(user.split_last):
#  user.emacs_prefix(-1)
#  key("ctrl-x o")
#split close: key(ctrl-x 0)
#action(user.split_clear): key(ctrl-x 1)
#action(user.split_clear_all): key(ctrl-x 1)
