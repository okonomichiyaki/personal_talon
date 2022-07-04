app.name: OBS Studio
app.exe: obs64.exe
app.name: Application Frame Host
app.exe: ApplicationFrameHost.exe
app.name: Taiko5DX
app.exe: Taiko5DX.exe
-
tycho fury ghana: user.trv_furigana()
tycho (test | debug): user.trv_debug()
tycho copy: user.trv_copy()
tycho translate: user.trv_translate()
tycho deep look:
    key(ctrl-f8)
	  mouse_move(450, 820)
	  user.mouse_drag(0)
    mouse_move(1425, 1020)
	  user.mouse_drag_end()
tycho jisho:
    user.trv_copy()
    text = clip.text()
    user.search_with_search_engine("https://jisho.org/search/%s", text)
