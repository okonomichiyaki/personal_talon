from talon import Module, Context, actions

yomichan = False

mod = Module()
@mod.action_class
class Actions:
    def ff_yomichan_on():
        """hold shift and switch to control mouse mode"""
        global yomichan
        if not yomichan:
            actions.key("shift:down")
            actions.user.mouse_enable_control_mouse()
            actions.user.mouse_disable_zoom_mouse()
            yomichan = True

ctx = Context()
ctx.matches = r"""
app.name: Firefox
"""
@ctx.action_class("user")
class FirefoxUserActions:
    def pop():
        global yomichan
        if yomichan:
            actions.key("shift:up")
            actions.user.mouse_enable_zoom_mouse()
            actions.user.mouse_disable_control_mouse()
            yomichan = False
        else:
            actions.user.mouse_click_or_zoom()


ctx = Context()
ctx.matches = r"""
app.name: Firefox
"""
@ctx.action_class("browser")
class FirefoxBrowserActions:
    def bookmark():
        actions.key("alt-i")
