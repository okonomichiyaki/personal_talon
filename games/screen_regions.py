from talon import actions, ctrl

def __get_index__(width, height, x_splits, y_splits, x, y):
    w = width / x_splits
    h = height / y_splits
    i = divmod(x, w)[0]
    j = divmod(y, h)[0]
    return (int(i), int(j))

def get_index(x_splits, y_splits):
    x, y = ctrl.mouse_pos()
    return __get_index__(1920, 1080, x_splits, y_splits, x, y)

def call_region(x_splits, y_splits, functions):
    i, j = get_index(x_splits, y_splits)
    functions[j][i]()

def nop():
    print("nop")

def hold(*args):
    def op():
        for name in args:
            actions.key(name + ":down")
            held.add(name)
    return op

def tap(name):
    return lambda: actions.key(name)

def short_hold(k):
    def op():
        actions.key(k + ":down")
        actions.sleep(0.2)
        actions.key(k + ":up")
    return op

