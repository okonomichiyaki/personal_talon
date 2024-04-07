from talon import Module, Context, actions

ctx = Context()
ctx.matches = r"""
app.name: Firefox
"""
@ctx.action_class("browser")
class FirefoxBrowserActions:
    def bookmark():
        actions.key("alt-i")
