import ctypes
import os
import random
import winreg 

# while d == "desktop.ini avoiding having wallpaper desktop.ini set up with another process (e.g. office laptop) - can be skipped

path = "C:/Your folder path with wallpapers"

files=os.listdir(path)

d=random.choice(files)

while d == "desktop.ini":
    d = random.choice(files)
      
ctypes.windll.user32.SystemParametersInfoW(20, 0, path + d , 1+2)

