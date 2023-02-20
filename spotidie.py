"""
Spotidie
A simple script to kill spotify when it crashes
Usage: spotidie.py --install/--uninstall/--repair

Designed for Windows only, sorry Linux users
"""

import ctypes, os, sys

def check_if_admin():
    try:
        is_admin = os.getuid() == 0
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    # Check if the user is running as admin
    if is_admin == False:
        print("Spotidie installer must be run as admin")
        exit(1)
      
def install():
    if os.path.exists("C:\Windows\System32\spotidie.py") == False and os.path.exists('C:\Windows\System32\spotidie.bat') == False:
        sdcore = open('C:\Windows\System32\spotidie.py', 'w')
        sdcore.write('import os\nos.system("taskkill /f /im  Spotify.exe")')
        sdcore.close()
        sdbat = open('C:\Windows\System32\spotidie.bat', 'w')
        sdbat.write('python C:\Windows\System32\spotidie.py')
        sdbat.close()
    else:
        print("Already installed, if its not working, run spotidie.py --repair")
        exit(1)
    print("Installed")

def uninstall():
    if os.path.exists("C:\Windows\System32\spotidie.py"):
        os.remove("C:\Windows\System32\spotidie.py")
    if os.path.exists('C:\Windows\System32\spotidie.bat'):
        os.remove('C:\Windows\System32\spotidie.bat')
    print("Uninstalled")

def repair():
    uninstall()
    install()
    print("Repaired")

check_if_admin()

try:
    if sys.argv[1] == "--install":
        install()
    elif sys.argv[1] == "--uninstall":
        uninstall()
    elif sys.argv[1] == "--repair":
        repair()
    else:
        print(f"Invalid argument: '{sys.argv[1]}'\nusage: spotidie.py --install/--uninstall/--repair")
except IndexError:
    print("Usage: spotidie.py --install/--uninstall/--repair")


