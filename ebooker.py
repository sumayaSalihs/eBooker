#!/usr/bin/env python3

# Imports
from tester import Tester
from commands import Com
from extras import getInput, isPython3, isNix, clear
import internals
import sys, os, webbrowser

try:
    import httplib
except:
    import http.client as httplib

# Create instances of classes
testerInst = Tester();
comInst = Com();
    
# Run tester script (see tester.py)
testerInst.test(0)

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
    "  \___|____/ \___/ \___/|_|\_\___|_| v" + internals.__version__ +
    "\n                       Running on Python " +
    str(sys.version_info[0]) + "!\n"
    "\n"
    "Type in \"help\" at the prompt for, of course, help."
)

# Read input and run the proper command (see commands.py)
def main():
    while True:
        testerInst.test(0)
        
        cmd = getInput("eBooker > ")
        
        if cmd == "help":
            comInst.ehelp()
        elif cmd == "exit":
            comInst.exit()
        elif cmd == "about":
            comInst.about()
        elif cmd == "edit":
            comInst.edit()
        elif cmd == "serve":
            comInst.serve()
        elif cmd == "clear":
            comInst.clear()
        elif cmd == "debug":
            comInst.debug()
        elif cmd == "docs":
            comInst.docs()
        else:
            print(
                "\"" + cmd + "\" is not a valid command. Type \"help\" for more options"
            )

# Run main() unless user hits Ctrl-C, in which case exit...
# Or if there is an error, show a message
try:
    # Run main()
    main()
except KeyboardInterrupt:
    # Ctrl-C
    print("")
    sys.exit()
except:
    # An error
    print("\nAn internal error occurred!")
    print("Program execution stopped. Type RETURN to exit. Run \"debug\" command when you next open eBooker to report this problem.")
    print("If you didn't already, always cd into eBooker's folder before running this program.")
    raise
    # Wait for RETURN, then exit
    getInput("")
    sys.exit(1)