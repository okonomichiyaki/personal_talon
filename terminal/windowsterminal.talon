app.name: WindowsTerminal.exe
#2021-02-07 14:05:33    IO Executable: C:\Program Files\WindowsApps\Microsoft.WindowsTerminal_1.5.10271.0_x64__8wekyb3d8bbwe\WindowsTerminal.exe
-
tag(): terminal
tag(): user.git

change code: "cd ~\Dropbox\Headquarters\Code \n"
change talon: "cd ~\AppData\Roaming\\talon \n"
virtual activate: ".\Scripts\Activate.ps1 \n"

clean repeat: key(ctrl-l up enter)
python repeat: key(ctrl-z enter up enter)
python quit: key(ctrl-z enter)
