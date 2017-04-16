#!/usr/bin/env python3
version = "1.0.3"

from time import sleep
import sys
import os
import codecs
import webbrowser
from tester import tests

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

def augment(fileString):
    editfileFile = codecs.open("chapter-" + fileString + ".html", "r", "utf-8")
    editfileBuffer = "<!DOCTYPE html><html><head><title>" + "Chapter: " + fileString + "</title></head>"
    editfileBuffer += editfileFile.read()
    editfileBuffer += "</body></html>"
    editfileFile.close()
    editfileFile = codecs.open("chapter-" + fileString + ".html", "w", "utf-8")
    editfileFile.write(editfileBuffer)
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
aboutString = "eBooker is a command-line tool which lets you create ebooks and other text files from command line with ease. You don't have to be a programming expert or a nerd to use this. Anyone with a basic knowledge in computers can use this tool very easily. We provide just one script to run, so run it! So far, it can execute simple commands and also create and edit a file."

tests()

try:
    while True:
        cmd = get_input("eBooker > ")
        if cmd == "help":
            tests()
            print(helpString)
            tests()
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
            tests()
        elif cmd == "about":
            tests()
            print(aboutString)
            tests()
        elif cmd == "edit":
            tests()
            editloopBool = True
            while editloopBool:
                editBool = get_input("Would you like to create a new chapter? (y/n) ")
                if editBool == "y":
                    editloopBool = False
                    print("You want to create a new chapter.")
                    newnameblankBool = True
                    while newnameblankBool:
                        newfileString = get_input("What would you like it to be called? ")
                        if (newfileString == "") or (newfileString == None) or (newfileString == " "):
                            print("You must enter a filename.")
                        else:
                            print("Creating file...")
                            sleep(3)
                            newfileFile = codecs.open("chapter-" + newfileString + ".html", "a", "utf-8")
                            newfileFile.write("Press CTRL-O then hit return to save. Press CTRL-X to exit.\n")
                            newfileFile.write("Don't worry if you can't see part of your lines; they will\n")
                            newfileFile.write("be saved anyway.")
                            newfileFile.close()
                        print("Your file is created!")
                        newnameblankBool = False
                    sleep(2)
                    open_editor("chapter-" + newfileString + ".html")
                    print("If you got an error, use the \"debug\" command.")
                elif editBool == "n":
                    tests()
                    editloopBool = False
                    print("You want to edit an existing chapter!")
                    editnameblankBool = True
                    while editnameblankBool:
                        editfileString = get_input("Please type in the name. ")
                        if (editfileString == "") or (editfileString == None) or (editfileString == " "):
                            print("You must enter a filename.")
                        else:
                            print("Opening file for editing...")
                            sleep(3)
                            editnameblankBool = False
                    open_editor("chapter-" + editfileString + ".html")
                    print("If you got an error, use the \"debug\" command.")
                else:
                    print("Please type in \"y\" or  \"n\".")
            tests()
        elif cmd == "serve":
            tests()
            print("Serving book...")
            sleep(2)
            webbrowser.open("https://www.python.org")
            # Loop here
            # Put contents of all HTML files into one
            # augment() that file
            # Open in default web browser
            # CODE
            # print("Sucess! Your file is served. Press ENTER when you are done reviewing.")
            # doneloopBool = True
            # while doneloopBool:
            #   doneBool = get_input("")
            # END CODE
            # Delete that file
            # For now:
            print("This feature is coming soon. It's not here yet!")
            tests()
        elif cmd == "clear":
            tests()
            print("Clearing...")
            sleep(2)
            clear()
            print("******************** eBooker v" + version + " ********************")
            print("")
            sleep(1)
            tests()
        elif cmd == "debug":
            tests()
            print("Debugging help for MacOS/*nix version:")
            print("Email me at archmaster@yahoo.com with the error code for the error message you encountered.")
            debug()
            tests()
        else:
            tests()
            print("\"" + cmd + "\" is not a valid command. Type \"help\" for more options")
            tests()
except KeyboardInterrupt:
    print("")
    if tests():
        sys.exit()