from user.knausj_talon.code.screenshot import get_screenshot_path, flash_rect
from talon import Module, screen, ui, cron, app, actions, clip, Context, cron
from talon.experimental import locate
from talon.canvas import Canvas, Rect
from typing import Optional
from datetime import datetime
import os

from PIL import Image
import pytesseract
from urllib import request, parse
import json

FULL_DIALOG_BOX = ui.Rect(450, 820, 975, 200)
SCREENSHOT_FOLDER = r'C:\Users\michiaki\Dropbox\Headquarters\NOTES\Taiko Risshiden V\screenshots\ocr'

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def translate(text):
    data = parse.urlencode({'auth_key': deepl_key, 'text': text, 'target_lang': 'EN'}).encode()
    req =  request.Request('https://api-free.deepl.com/v2/translate', data=data)
    resp = request.urlopen(req)
    return json.loads(resp.read())['translations'][0]['text']

def extract(path):
    text = pytesseract.image_to_string(Image.open(path), lang='jpn')
    text = text.strip()
    return text

def get_screenshot_path(title = None, dated = False):
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
    full_path = get_screenshot_path("xxxxx", True)
    main_screen = screen.main_screen()
    full_img = screen.capture_rect(main_screen.rect)
    full_img.write_file(full_path)

    watch_path = get_screenshot_path()
    watch_rect = ui.Rect(rect.x, rect.y, rect.width, rect.height / 3)
    watch_img = screen.capture_rect(watch_rect)
    watch_img.write_file(watch_path)

    flash_rect(rect)
    text_img = screen.capture_rect(rect)
    parts = full_path.split(".")
    text_path = parts[0] + "_text." + parts[1]
    text_img.write_file(text_path)
    return (full_path, text_path, watch_path)

canvas = None
text_size = 20
text_margin = 10
screen_watcher = None

def start_watching(path):
     global screen_watcher
     if screen_watcher:
         return
     def job():
         global screen_watcher
         matches = locate.locate(path)
         if len(matches) == 0:
             clear_subtitles()
             cron.cancel(screen_watcher)
             os.remove(path)
             screen_watcher = None
     screen_watcher = cron.interval("500ms", job)

def clear_subtitles():
    global canvas
    if canvas != None:
        canvas.close()
        canvas = None

def draw_subtitle(c, text, idx):
    c.paint.typeface = "arial"
    c.paint.textsize = text_size
    rect = c.paint.measure_text(text)[1]
    c.paint.color = "000000"
    c.paint.style = c.paint.Style.FILL
    x = 1920 / 2 - (rect.width + text_margin) / 2
    y = 1080 - (idx + 1) * (rect.height + text_margin)
    w = rect.width + text_margin
    h = rect.height + text_margin
    c.draw_rect(Rect(x, y, w, h))
    c.paint.color = "FFFFFF"
    c.draw_text(text, x + text_margin / 2, y + rect.height + text_margin / 2)

def show_subtitles(text):
    global canvas
    clear_subtitles()
    lines = text.split("\n")
    lines = map(lambda line: line.strip(), lines)
    lines = filter(lambda line: len(line) > 0, lines)
    lines = list(lines)
    lines.reverse()
    print(lines)
    def on_draw(c):
        for idx, line in enumerate(lines):
            draw_subtitle(c, line, idx)
    canvas = Canvas.from_rect(ui.screens()[0].rect)
    canvas.register("draw", on_draw)
    canvas.freeze()

def capture_text(watch = False):
    (full_path, text_path, watch_path) = take_screenshots(FULL_DIALOG_BOX)
    text = extract(text_path)
    os.remove(text_path)
    cleaned_up = text.replace("\n", "_").replace("?", "q")
    os.rename(full_path, full_path.replace("xxxxx", cleaned_up))
    if watch:
        start_watching(watch_path)
    return text

mod = Module()
@mod.action_class
class Actions:
    def trv_copy():
        """ocr dialogue box from taiko risshiden and put it in the clipboard"""
        clear_subtitles()
        text = capture_text()
        clip.set_text(text)

    def trv_translate():
        """ocr dialogue box from taiko risshiden and translate it to on-screen subtitles"""
        clear_subtitles()
        text = capture_text(True)
        translation = translate(text)
        show_subtitles(translation)
