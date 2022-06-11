from talon import Context, actions, ui, Module, app, clip

mod = Module()
ctx = Context()
ctx.matches = r'''
app.exe: emacs.exe
'''
@mod.action_class
class Actions:
    def emacs_command(name: str): "Runs an emacs command."
    def emacs_prefix(n: int): "Inputs a prefix argument."
    def emacs_help(): "Runs the emacs help command prefix."

@ctx.action_class("self")
class emacs_actions:
    def split_window(): actions.key("ctrl-x 2")
    def split_window_vertically(): actions.key("ctrl-x 2")
    def split_window_horizontally(): actions.key("ctrl-x 3")
    def split_next(): actions.key("ctrl-x o")
    def split_last():
        actions.user.emacs_prefix(-1)
        actions.key("ctrl-x o")
    def split_clear(): actions.key("ctrl-x 1")
    def split_clear_all(): actions.key("ctrl-x 1")

    def emacs_command(name):
        actions.key("alt-x")
        actions.insert(name)
        actions.key("enter")

    # Applying meta to each key is fewer keypresses overall and works in
    # ansi-term mode.
#     def emacs_prefix(n): actions.key(" ".join(f"alt-{i}" for i in str(n)))
    def emacs_prefix(n): actions.key(f'ctrl-u {" ".join(str(n))}')

    # NB. f1 works in ansi-term mode; C-h doesn't.
    def emacs_help(): actions.key("f1")

    # def clobber_selection_if_exists():
    #     actions.key("ctrl-alt-shift-backspace") # keybinding added for talon

    def dictation_peek_left(clobber=False):
        # NB. need to clobber because while we restore the mark position, we
        # don't restore transient mark mode. TODO: restore transient mark mode?
        if clobber:
            actions.user.clobber_selection_if_exists()
        actions.key("ctrl-@")
        actions.edit.word_left()
        text = actions.edit.selected_text()
        actions.key("ctrl-u ctrl-@")
        return text

    def dictation_peek_right():
        actions.edit.extend_right()
        text = actions.edit.selected_text()
        actions.key("ctrl-u ctrl-@")
        return text

    def select_range(line_start, line_end):
        actions.edit.jump_line(line_start)
        actions.key("ctrl-@ ctrl-@")
        actions.edit.jump_line(line_end)
        actions.edit.line_end()
        actions.edit.right()

@ctx.action_class('app')
class app_actions:
    def tab_next(): actions.key("ctrl-x o")
    def tab_close(): actions.key("ctrl-x 0")
    def tab_open(): actions.key("ctrl-x 2")
    def tab_previous():
        actions.user.emacs_prefix(-1)
        actions.key("ctrl-x o")
    def window_open(): actions.key("ctrl-x 5 2")

@ctx.action_class('edit')
class edit_actions:
    def delete(): actions.key("backspace")
    def find(text: str = None): actions.key("ctrl-s")
    def find_next(): actions.key("ctrl-s")
    def find_previous(): actions.key("ctrl-s")

    def word_left(): actions.key("alt-b")
    def word_right(): actions.key("alt-f")
    def extend_word_left(): actions.key("shift-alt-b")
    def extend_word_right(): actions.key("shift-alt-f")
    def select_all(): actions.key("ctrl-x h")
    def select_line(n: int = None):
        actions.key("ctrl-a shift-down")
        # TODO repeat n times
    def line_clone(): actions.key("ctrl-a ctrl-k ctrl-y enter shift-left ctrl-y ctrl-a")

    def save(): actions.key("ctrl-x ctrl-s")
    def copy(): actions.key("alt-w")
    def cut(): actions.key("ctrl-w")
    def paste(): actions.key("ctrl-y")
    def undo(): actions.key("ctrl-_")

    def zoom_in(): actions.key("ctrl-x ctrl-+")
    def zoom_out(): actions.key("ctrl-x ctrl--")
    def zoom_reset(): actions.key("ctrl-x ctrl-0")

    # # this relies on a custom binding for M-W that copies the selection to the
    # # clipboard without unselecting it or cluttering the kill ring
    # def selected_text():
    #     with clip.capture() as s:
    #         # TODO: if transient mark is not on, perhaps return ""?
    #         actions.key("alt-shift-w")
    #     try: return s.get()
    #     except clip.NoChange: return ""

    def jump_line(n):
        actions.user.emacs_prefix(n)
        actions.key("alt-g g")

@ctx.action_class('win')
class win_actions:
    def filename():
        # expecting something like this in init.el:
        # (setq frame-title-format '("%b" " - " "[" (:eval (format "%s" major-mode)) "]"))
        title = actions.win.title()
        title = title.split(" - ")[0]
        return title

@ctx.action_class('code')
class code_actions:
    def toggle_comment(): actions.key("alt-;")
