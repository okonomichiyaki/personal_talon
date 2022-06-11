from user.knausj_talon.code.screenshot import get_screenshot_path, flash_rect

from talon import Module, screen, ui, cron, app, actions, clip, Context, cron
from talon.experimental import locate
from talon.canvas import Canvas, Rect

import inspect
import os
import re
from subprocess import PIPE, CREATE_NO_WINDOW
import subprocess
from typing import Optional
from datetime import datetime
from itertools import groupby

import json
from PIL import Image

PYTHON_PATH = r"C:\Users\michiaki\AppData\Local\Microsoft\WindowsApps\python.exe"
SARU_PATH = r"C:\Users\michiaki\Dropbox\Headquarters\Code\saru.py"
FULL_DIALOG_BOX = ui.Rect(500, 850, 800, 150) # magic numbers for TRV @ 1920x1080
SCREENSHOT_FOLDER = r"C:\Users\michiaki\Dropbox\Headquarters\NOTES\Taiko Risshiden V\screenshots\ocr"

GREEN = "39FF14"
RED = "EE4B2B"
BLACK = "000000"
WHITE = "FFFFFF"

canvas = None
text_size = 20
text_margin = 10
fsize = 15
screen_watcher = None
draw_fns = []

def get_screenshot_path(title=None, dated=True):
    filename = "screenshot"
    if dated:
        date = datetime.now().strftime("%Y-%m-%dT%H-%M-%S")
        filename = filename + "-" + date
    if title:
        filename = filename + "-" + title
    filename = filename + ".png"
    path = os.path.expanduser(os.path.join(SCREENSHOT_FOLDER, filename))
    return os.path.normpath(path)

def take_screenshots(rect: ui.Rect):
    clear()
    full_path = get_screenshot_path("xxxxx")
    main_screen = screen.main_screen()
    full_img = screen.capture_rect(main_screen.rect)
    full_img.write_file(full_path)

    watch_path = get_screenshot_path("watch", False)
    h = rect.height / 9
    watch_rect = ui.Rect(rect.x, rect.y + h, rect.width, h)
    watch_img = screen.capture_rect(watch_rect)
    watch_img.write_file(watch_path)

    flash_rect(rect)
    text_path = get_screenshot_path("text", False)
    text_img = screen.capture_rect(rect)
    text_img.write_file(text_path)
    return (full_path, text_path, watch_path)

def clear():
    global canvas
    global draw_fns
    if canvas != None:
        canvas.close()
        canvas = None
        draw_fns = []

def on_draw(c):
    global draw_fns
    for fn in draw_fns:
        fn(c)

def draw(fn):
    global canvas
    draw_fns.append(fn)
    if canvas == None:
        canvas = Canvas.from_rect(ui.screens()[0].rect)
        canvas.register("draw", on_draw)
        canvas.freeze()

def start_watching(path):
     global screen_watcher
     if screen_watcher:
         return
     def job():
         global screen_watcher
         matches = locate.locate(path)
         if len(matches) == 0:
             clear()
             cron.cancel(screen_watcher)
             #os.remove(path)
             screen_watcher = None
     screen_watcher = cron.interval("500ms", job)

def box_to_rect(box):
    x = FULL_DIALOG_BOX.x + box[0]
    y = FULL_DIALOG_BOX.y + box[1]
    return Rect(x, y, box[2], box[3])

def show_furigana(fs):
    def on_draw(c):
        for f in fs:
            text = f["reading"]
            x = FULL_DIALOG_BOX.x + f["x"]
            y = FULL_DIALOG_BOX.y + f["y"]
            #c.paint.typeface = "ms gothic"
            c.paint.typeface = "meiryo"
            c.paint.textsize = fsize
            c.paint.color = GREEN
            #c.draw_rect(Rect(x, y, 3, 3))
            rect = c.paint.measure_text(text)[1]
            x = x - rect.width / 2
            # y parameter to draw_text appears to be the baseline, and text is drawn above it
            c.paint.color = "000000"
            c.paint.style = c.paint.Style.STROKE
            c.draw_text(text, x, y)
    draw(on_draw)

def show_subtitles(text):
    lines = text.split("\n")
    lines = map(lambda line: line.strip(), lines)
    lines = filter(lambda line: len(line) > 0, lines)
    lines = list(lines)
    lines.reverse()
    print(lines)
    def on_draw(c):
        for idx, line in enumerate(lines):
#            if re.search('[a-zA-Z]', line):
#                c.paint.typeface = "arial"
#            else:
            c.paint.typeface = "meiryo"
            c.paint.textsize = text_size
            rect = c.paint.measure_text(line)[1]
            c.paint.color = BLACK
            c.paint.style = c.paint.Style.FILL
            x = 1920 / 2 - (rect.width + text_margin) / 2
            y = 1080 - (idx + 1) * (rect.height + text_margin)
            w = rect.width + text_margin
            h = rect.height + text_margin
            c.draw_rect(Rect(x, y, w, h))
            c.paint.color = WHITE
            c.draw_text(line, x + text_margin / 2, y + rect.height + text_margin / 2)
    draw(on_draw)

def draw_box(c, box):
    rect = box_to_rect(box)
    c.paint.color = GREEN
    c.paint.style = c.paint.Style.STROKE
    c.draw_rect(rect)

def show_boxes(boxes):
    def on_draw(c):
        for box in boxes:
            draw_box(c, box)
    draw(on_draw)

def show_all_boxes(cdata):
    boxes = []
    for line in cdata:
        for d in line:
            box = d["box"]
            boxes.append(box)
    show_boxes(boxes)

def show_low_confidence(cdata):
    boxes = []
    for line in cdata:
        for d in line:
            if d["conf"] < 50:
                boxes.append(d["box"])
    #show_boxes(boxes)
    def on_draw(c):
        for box in boxes:
            #draw_box(c, box)
            r  = box_to_rect(box)
            x = r.x
            y = r.y + r.height + r.height / 3
            c.paint.color = RED
            c.paint.style = c.paint.Style.STROKE
            while x + 5 < r.x + r.width:
                c.draw_line(x, y, x + 5, y - 5)
                c.draw_line(x + 5, y - 5, x + 10, y)
                x = x + 10
    draw(on_draw)

def call_saru(filename, furigana="all", translate=False):
    """Call saru.py as subprocess and parse output"""
    command = [PYTHON_PATH, SARU_PATH, filename]
    if furigana:
        command.append("-f")
        command.append(furigana)
    if translate:
        command.append("-t")
    result = subprocess.run(command, stdout=PIPE, stderr=PIPE, creationflags=CREATE_NO_WINDOW)
    err = result.stderr.decode("utf-8")
    if len(err) > 0:
        print("stderr from saru:\n" + "\n".join(["ERROR " + line.strip() for line in err.split("\n")]))
    if result.returncode != 0:
        # TODO visual error
        return None
    raw = result.stdout.decode("utf-8")
    return json.loads(raw)

def capture_text(watch=True, translate=False):
    """Capture screenshots with original text, return data from saru.py"""
    (full_path, text_path, watch_path) = take_screenshots(FULL_DIALOG_BOX)
    saru = call_saru(text_path, translate=translate)
    if saru == None:
        return
    text = saru["original"]
    #os.remove(text_path)
    cleaned_up = text.replace("\n", "_").replace("?", "q")
    os.rename(full_path, full_path.replace("xxxxx", cleaned_up))
    if watch:
        start_watching(watch_path)
    return saru

def debug():
    saru = capture_text(watch=True, translate=True)
    if saru == None:
        return
    show_low_confidence(saru["cdata"])
    show_all_boxes(saru["cdata"])
    show_furigana(saru["furigana"])
    original = saru["original"]
    translation = saru["translation"]
    show_subtitles(translation)

mod = Module()
@mod.action_class
class Actions:
    def trv_furigana():
        """show furigana"""
        saru = capture_text(True)
        if saru == None:
            return
        show_furigana(saru["furigana"])

    def trv_copy():
        """ocr dialogue box from taiko risshiden and put it in the clipboard"""
        saru = capture_text(True)
        if saru == None:
            return
        text = saru["original"]
        clip.set_text(text)

    def trv_translate():
        """ocr dialogue box from taiko risshiden and translate it to on-screen subtitles"""
        saru = capture_text(True)
        if saru == None:
            return
        text = saru["original"]
        clip.set_text(text)
        translation = saru["translation"]
        show_subtitles(text)

    def trv_debug():
        """display details for debugginging"""
        debug()
