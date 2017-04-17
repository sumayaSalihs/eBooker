#!/usr/bin/env python3
version = "1.0.3"

from time import sleep
import sys
import os
import codecs
import webbrowser
import glob
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

def augment(filecontentsString):
    editfileBuffer = "<!DOCTYPE html><html><head><title>" + "Your Book" + "</title></head>"
    editfileBuffer += filecontentsString
    editfileBuffer += "</body></html>"
    return editfileBuffer
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

helpString = "eBooker v" + version + " Help\n==============" + ("=" * len(version)) + "\nhelp - show this help\nexit - quit the session\nabout - read about this tool\nedit - edit/create a file\nclear -  clear the screen\ndebug - give you a list of commonly occurring issues\nserve - open your book in a web browser for reviewing"
aboutString = "eBooker is a command-line tool which lets you create ebooks and other text files from command line with ease. You don't have to be a programming expert or a nerd to use this. Anyone with a basic knowledge in computers can use this tool very easily."

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
                    tests()
                    editloopBool = False
                    print("You want to create a new chapter.")
                    while True:
                        newfileString = get_input("What would you like the chapter number to be? ")
                        if (newfileString == "") or (newfileString == None) or (newfileString == " "):
                            print("You must enter a chapter number.")
                        else:
                            try:
                                newfileString = int(newfileString)
                                break
                            except ValueError:
                                print("You must enter a number.")
                    print("Creating file...")
                    sleep(3)
                    newfileFile = codecs.open("chapter-" + str(newfileString) + ".html", "a", "utf-8")
                    newfileFile.write("Press CTRL-O then hit return to save. Press CTRL-X to exit.\n")
                    newfileFile.write("Don't worry if you can't see part of your lines; they will\n")
                    newfileFile.write("be saved anyway.")
                    newfileFile.close()
                    print("Your file is created!")
                    newnameblankBool = False
                    sleep(2)
                    open_editor("chapter-" + str(newfileString) + ".html")
                    print("If you got an error, use the \"debug\" command.")
                    tests()
                elif editBool == "n":
                    tests()
                    editloopBool = False
                    print("You want to edit an existing chapter!")
                    editnameblankBool = True
                    while True:
                        editfileString = get_input("Please type in the chapter number. ")
                        if (editfileString == "") or (editfileString == None) or (editfileString == " "):
                            print("You must enter a chapter number.")
                        else:
                            try:
                                editfileString = int(editfileString)
                                break
                            except ValueError:
                                print("You must enter a number.")
                    print("Opening file for editing...")
                    sleep(3)
                    open_editor("chapter-" + str(editfileString) + ".html")
                    print("If you got an error, use the \"debug\" command.")
                    tests()
                else:
                    tests()
                    print("Please type in \"y\" or  \"n\".")
                    tests()
            tests()
        elif cmd == "serve":
            tests()
            print("Serving book...")
            sleep(2)
            filenameArray = glob.glob(os.path.dirname(os.path.realpath(__file__)) + "/*.html")
            filebufferString = ""
            for filenameString in filenameArray:
                newfilenameString = os.path.basename(filenameString)
                chapternameString = os.path.splitext(newfilenameString)[0]
                chapternameString = chapternameString.replace("-", " ", 1)
                chapternameString = chapternameString.capitalize()
                filebufferString += "<h1>" + chapternameString + "</h1>"
                filecontentsString = codecs.open(newfilenameString, "r", "utf-8").read()
                filebufferString += filecontentsString
                filebufferString += "<hr/>"
            filebufferString += "<center><h1>THE END!</h1></center>"
            filebufferString = augment(filebufferString)
            reviewfileFile = codecs.open("review-book.html", "w", "utf-8")
            reviewfileFile.write(filebufferString)
            reviewfileFile.close()
            webbrowser.open("file://" + os.path.dirname(os.path.realpath(__file__)) + "/review-book.html")
            print("Success! Your book is served. Press RETURN when you are done reviewing it.")
            doneloopBool = True
            while doneloopBool:
                doneBool = get_input("")
                break
            os.remove("review-book.html")
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