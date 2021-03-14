from talon import ctrl, ui, Module, Context, actions, clip, app, noise

ctx = Context()
ctx.matches = r"""
app.name: CoQ.exe
"""
@ctx.action_class("user")
class caves_of_qud_user:
    def pop():
        actions.key("w") 
