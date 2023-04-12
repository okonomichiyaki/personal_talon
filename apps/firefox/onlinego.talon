app: firefox
title: Game Finished
-
beginning: key(home)
mouse toggle: user.toggle_mouse()
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
