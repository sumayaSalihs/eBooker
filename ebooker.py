#!/usr/bin/env python3
version = "1.0.3"

from time import sleep
import sys
import os
import codecs;

# TESTS
def tests():
    try:
        assert os.path.exists("docs/stylesheet.css")
        assert os.path.exists("README.md")
        assert os.path.exists("docs/index.html")
        assert os.path.exists("ebooker.py")
        assert os.path.exists("docs")
        assert helpString != ""
        assert aboutString != ""
        return
    except:
        print("")
        print("An internal error occurred!")
        print("Program execution stopped. Type RETURN to exit.")
        errorLoopBool = True
        while errorLoopBool:
            errorBool = get_input("")
            sys.exit(1)
# END TESTS

py3 = False
if sys.version_info[0] >= 3:
	py3 = True
def get_input(message):
	if py3 == True:
		return str(input(message))
	else:
		return raw_input(message)

Nix = False
if os.name == "posix":
	Nix = True

def clear():
    if Nix == True:
        os.system("clear")
    else:
        os.system("cls")
def open_editor(fileString):
    if Nix == True:
        os.system("nano " + fileString)
    else:
        os.system("notepad " + fileString)
def debug():
    print("|-----------------------|--------|")
    print("|Message                |Code    |")
    print("|-----------------------|--------|")
    if Nix == True:
        print("|nano: command not found|42912246|")
        print("|-----------------------|--------|")
        print("|other message          |87376634|")
        print("|-----------------------|--------|")
    else:
        print("|'notepad' is not       |64485253|")
        print("|recognized as an       |        |")
        print("|internal or external   |        |")
        print("|command, operable      |        |")
        print("|program or batch file. |        |")
        print("|-----------------------|--------|")
        print("|other message          |93856898|")
        print("|-----------------------|--------|")
clear()
print("Loading...")
sleep(3)
clear()
print("******************** eBooker v" + version + " ********************")
print("*********************** Python " + str(sys.version_info[0]) + " ***********************")
print("Type in \"help\" at the prompt for, of course, help.")
print("")
sleep(1)

helpString = "eBooker v" + version + " Help\n==============" + ("=" * len(version)) + "\nhelp - show this help\nexit - quit the session\nabout - read about this tool\nedit - edit/create a file\nclear -  clear the screen\ndebug - give you a list of commonly occuring issues"
aboutString = "eBooker is a command-line application written in Python. With it, you don't have to learn programming or manage massive user interfaces to make great ebooks. So far, it can execute simple commands and also create and edit a file."

tests()

try:
    while True:
        cmd = get_input("eBooker > ")
        if cmd == "help":
            tests()
            print(helpString)
        elif cmd == "exit":
            tests()
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
        elif cmd == "about":
            tests()
            print(aboutString)
        elif cmd == "edit":
            tests()
            editloopBool = True
            while editloopBool:
                editBool = get_input("Would you like to create a new file? (y/n) ")
                if editBool == "y":
                    editloopBool = False
                    print("You want to create a new file.")
                    newnameblankBool = True
                    while newnameblankBool:
                        newfileString = get_input("What would you like it to be called? ")
                        if (newfileString == "") or (newfileString == None) or (newfileString == " "):
                            print("You must enter a filename.")
                        else:
                            print("Creating file...")
                            sleep(3)
                            newfileFile = codecs.open(newfileString, "a", "utf-8")
                            newfileFile.write("Press CTRL-O then hit return to save. Press CTRL-X to exit.\n")
                            newfileFile.write("Don't worry if you can't see part of your lines; they will\n")
                            newfileFile.write("be saved anyway.")
                            newfileFile.close()
                        print("Your file is created!")
                        newnameblankBool = False
                    sleep(2)
                    open_editor(newfileString)
                    print("If you got an error, use the \"debug\" command.")
                elif editBool == "n":
                    tests()
                    editloopBool = False
                    print("You want to edit an existing file!")
                    editnameblankBool = True
                    while editnameblankBool:
                        editfileString = get_input("Please type in the filename. ")
                        if (editfileString == "") or (editfileString == None) or (editfileString == " "):
                            print("You must enter a filename.")
                        else:
                            print("Opening file for editing...")
                            sleep(3)
                            editnameblankBool = False
                    open_editor(editfileString)
                    print("If you got an error, use the \"debug\" command.")
                else:
                    print("Please type in \"y\" or  \"n\".")
        elif cmd == "clear":
            tests()
            print("Clearing...")
            sleep(2)
            clear()
            print("******************** eBooker v" + version + " ********************")
            print("")
            sleep(1)
        elif cmd == "debug":
            tests()
            print("Debugging help for MacOS/*nix version:")
            print("Email me at archmaster@yahoo.com with the error code for the error message you encountered.")
            debug()
        else:
            tests()
            print("\"" + cmd + "\" is not a valid command. Type \"help\" for more options")
except KeyboardInterrupt:
    print("")
    if (tests()):
        sys.exit()