from talon import ctrl, ui, Module, Context, actions, clip, app, noise

ctx = Context()
ctx.matches = r"""
"""
@ctx.action_class("user")
class pop_default_user:
    def pop():
        actions.user.mouse_zoom()
