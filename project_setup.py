#!/usr/bin/env python
import subprocess
subprocess.Popen("powershell.exe start-process chrome.exe --incognito")
for i in range(4):
    subprocess.Popen("cmd.exe start cmd /k powershell", creationflags = subprocess.CREATE_NEW_CONSOLE)
for i in range(2):
    subprocess.Popen("cmd.exe start cmd /k ipython", creationflags = subprocess.CREATE_NEW_CONSOLE)
#subprocess.Popen("powershell.exe start-process C:\\Users\\Oliver\\AppData\\Local\\atom\\atom.exe")
subprocess.Popen("powershell.exe start-process spotify.exe")
