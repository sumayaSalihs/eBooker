#!/usr/bin/env python3

# Imports
from tester import Tester
from commands import Com
from extras import getInput, isPython3, isNix, clear
import sys, os, webbrowser

try:
    import httplib
except:
    import http.client as httplib

# Run tester script (see tester.py)
Tester().test(0)

# Install markdown module if not found
def install_markdown():
    if isPython3:
        os.system("pip3 install markdown")
    else:
        os.system("easy_install --home pip; pip install markdown")

# Check internet connection
def internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=1)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

# Check if markdown module is installed
def markdown_installed():
    return 'markdown' in sys.modules

# Clear the screen
clear()

# Install markdown...
# Except if internet connection doesn't work.
if not markdown_installed():
    if internet():
        install_markdown()
    else:
        print("Your internet connection is either too slow or nonexistent. The required packages could not be installed.")
        sys.exit(1)

# Another import
import markdown

# Print eBooker initial text
clear()
print(
    "       ____              _ \n"
    "      |  _ \            | |\n"
    "   ___| |_) | ___   ___ | | _____ _ __\n"
    "  / _ \  _ < / _ \ / _ \| |/ / _ \  __|\n"
    " |  __/ |_) | (_) | (_) |   <  __/ |\n"
    "  \___|____/ \___/ \___/|_|\_\___|_| v" + __version__ +
    "\n                       Running on Python " +
    str(sys.version_info[0]) + "!\n"
    "\n"
    "Type in \"help\" at the prompt for, of course, help."
)

# Read input and run the proper command (see commands.py)
def main():
    while True:
        Tester.test(0)
        
        cmd = getInput("eBooker > ")
        
        if cmd == "help":
            Com.ehelp()
        elif cmd == "exit":
            Com.exit()
        elif cmd == "about":
            Com.about()
        elif cmd == "edit":
            Com.edit()
        elif cmd == "serve":
            Com.serve()
        elif cmd == "clear":
            Com.clear()
        elif cmd == "debug":
            Com.debug()
        elif cmd == "docs":
            Com.docs()
        else:
            print(
                "\"" + cmd + "\" is not a valid command. Type \"help\" for more options"
            )

# Run main() unless user hits Ctrl-C, in which case exit.
try:
    main()
except KeyboardInterrupt:
    print("")
    sys.exit()