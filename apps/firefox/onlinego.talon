app.name: Firefox
and title: Game Finished — Mozilla Firefox
-

beginning: key(home)

forward:
    user.direction_forward()
    user.step()
backward:
    user.direction_backward()
    user.step()
step forward:
    user.direction_forward()
    user.step_continuous()
step backward:
    user.direction_backward()
    user.step_continuous()

mouse|toggle mouse: user.toggle_mouse()
