from talon import Context, actions, Module

mod = Module()
ctx = Context()
ctx.matches = r"""
os: mac
and app.bundle: com.microsoft.VSCode
"""
@ctx.action_class("edit")
class EditActions:
    # customized select line (mostly to make clear line behavior match intellij)
    def select_line(n: int=None):
        actions.key("ctrl-a")
        actions.edit.extend_line_down()
