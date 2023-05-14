from typing import Callable
from talon import actions, ctrl, ui, cron
from talon.canvas import Canvas, Rect
from math import sqrt

WIDTH = 1920
HEIGHT = 1080
canvas = None

# utilities for manipulating regions:

def _get_splits(matrix):
    """
    given a two dimensional array (assumes every row has same number of columns),
    calculate the number of splits
    """
    x_splits = len(matrix[0])
    y_splits = len(matrix[1])
    return (x_splits, y_splits)

def _get_index(matrix, width, height, x, y):
    """returns a tuple indexing into matrix based on the pixel coordinates from the screen"""
    x_splits, y_splits = _get_splits(matrix)
    w = width / x_splits
    h = height / y_splits
    j = divmod(x, w)[0]
    i = divmod(y, h)[0]
    return (int(i), int(j))

def _get_from_regions_xy(regions, x, y):
    """returns the element pointed to by the x,y coords provided"""
    i, j = _get_index(regions, WIDTH, HEIGHT, x, y)
    return regions[i][j]

def _get_from_regions_mouse(regions):
    """returns the element pointed to by the current mouse position"""
    x, y = ctrl.mouse_pos()
    return _get_from_regions_xy(regions, x, y)

# public API:

class Binding:
    """
    An operation attached to a screen region
    Consists of a name (eg 'hold', 'tap', etc.) and a list of keys
    Optionally a lambda to be called when triggered
    """
    def __init__(self, name: str, keys: list[str], operation: Callable = None):
        self.name = name
        self.keys = keys
        self.operation = operation

    def do(self):
        if self.operation:
            self.operation()

    def __str__(self):
        return f"Binding({self.name},{self.keys})"

def nop():
    """Returns a no-op Binding"""
    return Binding("nop", [], lambda: print("nop"))

def hold(*keys: str):
    """Returns a Binding which (indefinitely) holds down the specified keys"""
    # def op():
    #     for k in keys:
    #         actions.key(f"{k}:down")
    return Binding("hold", keys, None)

def short_press(key: str, duration: float =  0.2):
    """Returns a Binding which presses a key for a short duration"""
    def op():
        actions.key(f"{key}:down")
        actions.sleep(duration)
        actions.key(f"{key}:up")
    return Binding("short_press", [key], op)

def tap(key: str):
    return Binding("tap", [key], lambda: actions.key(f"{key}"))

def build_regions(keys: list[str], n: int = 3, m: int = 3, corners: bool = False):
    """Helper function for constructing 2-D arrays of strings (keys)"""
    result = [[[] for i in range(n)] for j in range(m)]

    if len(keys) != 4 and len(keys) != 8:
        raise ValueError("must supply exactly 4 or 8 keys")
    if len(keys) == 8 and corners:
        raise ValueError("corners flag only make sense with 4 keys")

    up = keys[0]
    down = keys[2]
    left = keys[1]
    right = keys[3]

    x = 0 if corners else 1
    for i in range(x, n-x):
        result[0][i].append(up)
    for i in range(x, n-x):
        result[m-1][i].append(down)
    for i in range(x, m-x):
        result[i][0].append(left)
    for i in range(x, m-x):
        result[i][n-1].append(right)

    if len(keys) == 8:
        result[0][0] = keys[4]
        result[0][n-1] = keys[5]
        result[m-1][0] = keys[6]
        result[m-1][n-1] = keys[7]

    return result

def build(fn: Callable, keys: list[str], n: int = 3, m: int = 3, corners: bool = False):
    """Helper function for constructing 2-D arrays of Bindings"""
    def convert(keys):
        if len(keys) > 0:
            return fn(*keys)
        else:
            return nop()
    array = build_regions(keys, n, m, corners)
    return [[convert(keys) for keys in row] for row in array]

# pre-defined regions for WASD and arrow keys of various sizes:

WASD3 = build(hold, "wasd", corners=True)
WASD4 = build(hold, "wasd", n=4, m=4, corners=True)
WASD5 = build(hold, "wasd", n=5, m=5, corners=True)

ARROWS3 = build(hold, ["up","left","down","right"], corners=True)
ARROWS4 = build(hold, ["up","left","down","right"], n=4, m=4, corners=True)
ARROWS5 = build(hold, ["up","left","down","right"], n=5, m=5, corners=True)

TAP_ARROWS3 = build(tap, ["up","left","down","right"])
TAP_ARROWS4 = build(tap, ["up","left","down","right"], n=4, m=4)
TAP_ARROWS5 = build(tap, ["up","left","down","right"], n=5, m=5)

class ScreenRegions:
    def __init__(self, bindings, color: str = "FF69B4", draw_text: bool = True):
        self.bindings = bindings
        self.color = color
        self.draw_text = draw_text
        self.cron_job = None
        self.holding = set()
        self.canvas = None

    def get_all_keys(self):
        keys = set()
        for row in self.bindings:
            for b in row:
                keys.update(b.keys)
        return keys

    def do(self):
        binding = _get_from_regions_mouse(self.bindings)
        print(binding)
        binding.do()

    def stop(self):
        if self.cron_job:
            cron.cancel(self.cron_job)
            self.cron_job = None
            self.holding = set()
            for k in self.get_all_keys():
                actions.key(k+":up")
            self.hide()

    def start(self):
        if self.cron_job != None:
            return

        def job():
            new_holding = set()
            binding = _get_from_regions_mouse(self.bindings)
            keys = binding.keys
            for k in keys:
                new_holding.add(k)
            stop_holding = self.holding.difference(new_holding)
            for k in stop_holding:
                actions.key(k+":up")
            self.holding = new_holding
            for k in self.holding:
                actions.key(k+":down")
        self.show()
        self.cron_job = cron.interval("60ms", job)

    def hide(self):
        if self.canvas:
            self.canvas.close()
            self.canvas = None

    def show(self):
        self.hide()
        x_splits, y_splits = _get_splits(self.bindings)
        w = WIDTH / x_splits
        h = HEIGHT / y_splits
        def on_draw(c):
            c.paint.stroke_width = 5
            c.paint.color = self.color
            for n in range(0, x_splits):
                for m in range(0, y_splits):
                    x = n * w
                    y = m * h
                    binding = _get_from_regions_xy(self.bindings, x + w / 2, y + h / 2)
                    c.paint.style = c.paint.Style.STROKE
                    c.draw_rect(Rect(x,y,w,h))
                    if self.draw_text:
                        c.paint.typeface = "arial"
                        c.paint.style = c.paint.Style.FILL
                        c.paint.textsize = round(h / 5)
                        keys = binding.keys
                        text = ",".join(keys)
                        rect = c.paint.measure_text(text)[1]
                        xt = x + w / 2 - rect.x - rect.width / 2
                        yt = y + h / 2 + rect.height / 2
                        c.draw_text(text, xt, yt)
        self.canvas = Canvas.from_rect(ui.screens()[0].rect)
        self.canvas.register("draw", on_draw)
        self.canvas.freeze()
