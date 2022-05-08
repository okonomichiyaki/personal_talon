app.name: Obsidian
-
zoom in:
    key(ctrl:down)
    user.mouse_scroll_up()
    key(ctrl:up)
ruby that:
    edit.copy()
    "<ruby><rb>"
    edit.paste()
    "</rb><rp>(</rp><rt>"
    "<rt><rp>)</rp></ruby>"
    edit.left()
    repeat(20)
