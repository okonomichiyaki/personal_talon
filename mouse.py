from talon_plugins import eye_zoom_mouse
from talon import noise, ctrl, Context, Module
import user.community.plugin.mouse.mouse as community

# make zoom mouse feel snappier, albeit a tiny bit twitchier:
eye_zoom_mouse.config.frames=5
eye_zoom_mouse.config.eye_avg=5

mod = Module()
ctx = Context()

# these actions enable disabling/enabling zoom mouse
# allows `mouse.talon` to switch between control-only and zoom-only
@mod.action_class
class Actions:
    def mouse_disable_zoom_mouse():
        """Disable zoom mouse"""
        eye_zoom_mouse.toggle_zoom_mouse(False)

    def mouse_enable_zoom_mouse():
        """Enable zoom mouse"""
        eye_zoom_mouse.toggle_zoom_mouse(True)
        # work around so pop stops scrolling without triggering zoom mouse:
        noise.unregister("pop",eye_zoom_mouse.zoom_mouse.on_pop)

# this enables popping to stop scroll without also triggering zoom
@ctx.action("user.noise_trigger_pop")
def click_or_zoom_or_stop_scroll():
    """Triggers a normal mouse click, or triggers zoom mouse, or stops scroll wheel"""
    if community.scroll_job:
        community.stop_scroll()
    elif not eye_zoom_mouse.zoom_mouse.enabled:
        ctrl.mouse_click(button=0)
    elif eye_zoom_mouse.zoom_mouse.enabled:
        eye_zoom_mouse.zoom_mouse.on_pop(eye_zoom_mouse.zoom_mouse.state)
