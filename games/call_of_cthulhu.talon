os: windows
and app.name: Call of Cthulhu
os: windows
and app.exe: CallOfCthulhu.exe
-
tag(): user.unreal
settings():
    key_wait = 16.0
    key_hold = 16.0

interact|touch: user.unreal_e_key()
crouch: user.unreal_ctrl_key()
