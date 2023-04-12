# switch between zoom and control mouse modes, exclusively one or the other
mouse control:
  tracking.control_zoom_toggle(false)
  tracking.control_toggle(true)
mouse zoom:
  tracking.control_zoom_toggle(true)
  tracking.control_toggle(false)
mouse center: mouse_move(960,540)
mouse hide: mouse_move(1921,1081)
mouse snore: user.mouse_sleep()
wheel tick down: user.mouse_scroll_down()
wheel tick up: user.mouse_scroll_up()
