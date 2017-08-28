#!/usr/bin/env python3
from tester import Tester, get_input, is_python_3
import sys
import os
import codecs
import webbrowser
import glob

try:
    import httplib
except:
    import http.client as httplib

# test if files exist
Tester().test()

__version__ = "1.1.0"
__help_string__ = "eBooker v" + __version__ + " Help\n==============" + \
    ("=" * len(__version__)) + "\n"+\
    "help   - show this help\n"+\
    "exit   - quit the session\n"+\
    "about  - read about this tool\n"+\
    "edit   - edit/create a file\n"+\
    "clear  - clear the screen\n"+\
    "debug  - give you a list of commonly occurring issues\n"+\
    "serve  - open your book in a web browser for reviewing"
__about_string__ = "eBooker is a command-line tool which lets you create ebooks and other text files from command line with ease. \
You don't have to be a programming expert or a nerd to use this. Anyone with a basic knowledge in computers can use this tool very easily."

def install_markdown():
    ''' install markdown module if not found '''
    if is_python_3:
        os.system("pip3 install markdown")
    else:
        os.system("easy_install --home pip; pip install markdown")

is_unix = os.name == "posix"


def clear():
    ''' clears the terminal '''
    if is_unix:
        os.system("clear")
    else:
        os.system("cls")


def open_editor(fileString):
    if is_unix:
        os.system("nano " + fileString)
    else:
        os.system("notepad " + fileString)


def augment(filecontentsString):
    return "<!DOCTYPE html><html><head><title>" + "Your Book" + \
        "</title></head>" + filecontentsString + "</body></html>"


def debug():
    ''' print debug messages '''
    print(
        "|-----------------------|--------|\n"
        "|Message                |Code    |\n"
        "|-----------------------|--------|"
    )

    if is_unix:
        print(
            "|nano: command not found|42912246|\n"
            "|-----------------------|--------|\n"
            "|other message          |87376634|\n"
            "|-----------------------|--------|"
        )
    else:
        print(
            "|'notepad' is not       |64485253|\n"
            "|recognized as an       |        |\n"
            "|internal or external   |        |\n"
            "|command, operable      |        |\n"
            "|program or batch file. |        |\n"
            "|-----------------------|--------|\n"
            "|other message          |93856898|\n"
            "|-----------------------|--------|"
        )


def internet():
    conn = httplib.HTTPConnection("www.google.com", timeout=1)
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False

def markdown_installed():
    return 'markdown' in sys.modules

clear()

if not markdown_installed():
    if internet():
        install_markdown()
    else:
        print("Your internet connection is either too slow or nonexistent! I cannot install the required packages for you.")
        sys.exit(1)

import markdown

clear()
print(
    "       ____              _ \n"
    "      |  _ \            | |\n"
    "   ___| |_) | ___   ___ | | _____ _ __\n"
    "  / _ \  _ < / _ \ / _ \| |/ / _ \  __|\n"
    " |  __/ |_) | (_) | (_) |   <  __/ |\n"
    "  \___|____/ \___/ \___/|_|\_\___|_| v" + __version__ +
    "                       Running on Python " +
    str(sys.version_info[0]) + "!\n"
    "\n"
    "Type in \"help\" at the prompt for, of course, help."
)

def cmd_debug():
    print("Debugging help for MacOS/*is_unix __version__:")
    print(
        "Email me at archmaster@yahoo.com with the error code for the error message you encountered.")
    debug()


def cmd_clear():
    print("Clearing...")
    clear()
    print("******************** eBooker v" +
          __version__ + " ********************")
    print("")


def cmd_serve():
    print("Serving book...")
    filenameArray = glob.glob(os.path.dirname(
        os.path.realpath(__file__)) + "/*.html")
    filebufferString = ""

    for filenameString in filenameArray:
        newfilenameString = os.path.basename(filenameString)
        chapternameString = os.path.splitext(newfilenameString)[0]
        chapternameString = chapternameString.replace("-", " ", 1)
        chapternameString = chapternameString.capitalize()
        filebufferString += "<h1>" + chapternameString + "</h1>"
        filecontentsString = codecs.open(
            newfilenameString, "r", "utf-8").read()
        filebufferString += markdown.markdown(filecontentsString)
        filebufferString += "<hr/>"
    filebufferString += "<center><h1>THE END!</h1></center>"
    filebufferString = augment(filebufferString)
    reviewfileFile = codecs.open("review-book.html", "w", "utf-8")
    reviewfileFile.write(filebufferString)
    reviewfileFile.close()
    webbrowser.open(
        "file://" + os.path.dirname(os.path.realpath(__file__)) + "/review-book.html")
    print(
        "Success! Your book is served. Press RETURN when you are done reviewing it."
    )

    get_input("")
    os.remove("review-book.html")


def cmd_edit():
    editloopBool = True

    while editloopBool:
        editBool = get_input(
            "Would you like to create a new chapter? (y/n) "
        )

        if editBool == "y":
            editloopBool = False
            print("You want to create a new chapter.")

            while True:
                newfileString = get_input(
                    "What would you like the chapter number to be? ")
                if (newfileString == "") or (newfileString is None) or (newfileString == " "):
                    print("You must enter a chapter number.")
                else:
                    try:
                        newfileString = int(newfileString)
                        break
                    except ValueError:
                        print("You must enter a number.")

            print("Creating file...")

            newfileFile = codecs.open(
                "chapter-" + str(newfileString) + ".html", "a", "utf-8"
            )
            newfileFile.write(
                "Press CTRL-O then hit return to save. Press CTRL-X to exit.\n"
            )
            newfileFile.write(
                "Don't worry if you can't see part of your lines; they will\n"
            )

            newfileFile.write("be saved anyway.")
            newfileFile.close()

            print("Your file is created!")

            open_editor("chapter-" + str(newfileString) + ".html")

            print("If you got an error, use the \"debug\" command.")

        elif editBool == "n":
            editloopBool = False
            print("You want to edit an existing chapter!")

            while True:
                editfileString = get_input(
                    "Please type in the chapter number. ")
                if (editfileString == "") or (editfileString is None) or (editfileString == " "):
                    print("You must enter a chapter number.")
                else:
                    try:
                        editfileString = int(editfileString)
                        break
                    except ValueError:
                        print("You must enter a number.")

            print("Opening file for editing...")

            open_editor("chapter-" + str(editfileString) + ".html")

            print("If you got an error, use the \"debug\" command.")

        else:
            print("Please type in \"y\" or  \"n\".")


def cmd_about():
    print(__about_string__)

def cmd_exit():
    exitloopBool = True
    while exitloopBool:
        exitBool = get_input("Would you like to quit? (y/n) ")
        if exitBool == "y":
            exitloopBool = False
            clear()
            sys.exit()
        elif exitBool == "n":
            exitloopBool = False
            print("OK, not exited!")
        else:
            print("Please type in \"y\" or  \"n\".")

def cmd_help():
    print(__help_string__)

def main():
    while True:
        cmd = get_input("eBooker > ")

        if cmd == "help":
            cmd_help()
        elif cmd == "exit":
            cmd_exit()
        elif cmd == "about":
            cmd_about()
        elif cmd == "edit":
            cmd_edit()
        elif cmd == "serve":
            cmd_serve()
        elif cmd == "clear":
            cmd_clear()
        elif cmd == "debug":
            cmd_debug()
        else:
            print(
                "\"" + cmd + "\" is not a valid command. Type \"help\" for more options"
            )

try:
    main()

except KeyboardInterrupt:
    print("")
    sys.exit()