#!/usr/bin/env python3
version = "1.0.1"

from time import sleep
import sys
import os
import codecs;
os.system("clear")
print("Loading...")
sleep(3)
os.system("clear")
print("******************** eBooker v" + version + " ********************")
print("Type in \"help\" at the prompt for, of course, help.")
print("")
sleep(1)

helpString = "eBooker v" + version + " Help\n==============" + ("=" * len(version)) + "\nhelp - show this help\nexit - quit this session\nabout - read about this tool\nedit - edit a file\nclear -  clear the screen\ndebug - give you help"
aboutString = "eBooker is a command-line application written in Python. With it, you don't have to learn programming or manage massive user interfaces to make great eBooks. So far, it can execute simple commands and also create and edit a file. Version: MacOS/*nix"
while True:
    cmd = str(input("ebooker > "))
    if cmd == "help":
        print(helpString)
    elif cmd == "exit":
        exitloopBool = True
        while exitloopBool:
            exitBool = str(input("Would you like to quit? (y/n) "))
            if exitBool == "y":
                exitloopBool = False
                os.system("clear")
                sys.exit()
            elif exitBool == "n":
                exitloopBool = False
                print("OK, not exited!")
            else:
                print("Please type in \"y\" or  \"n\".")
    elif cmd == "about":
        print(aboutString)
    elif cmd == "edit":
        editloopBool = True
        while editloopBool:
            editBool = str(input("Would you like to create a new file? (y/n) "))
            if editBool == "y":
                editloopBool = False
                print("You want to create a new file.")
                newnameblankBool = True
                while newnameblankBool:
                    newfileString = input("What would you like it to be called? ")
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
                os.system("nano " + newfileString)
                print("If you got an error, use the \"debug\" command.")
            elif editBool == "n":
                editloopBool = False
                print("You want to edit an existing file!")
                editnameblankBool = True
                while editnameblankBool:
                    editfileString = input("Please type in the filename. ")
                    if (editfileString == "") or (editfileString == None) or (editfileString == " "):
                        print("You must enter a filename.")
                    else:
                        print("Opening file for editing...")
                        sleep(3)
                        editnameblankBool = False
                os.system("nano " + editfileString)
                print("If you got an error, use the \"debug\" command.")
            else:
                print("Please type in \"y\" or  \"n\".")
    elif cmd == "clear":
        print("Clearing...")
        sleep(2)
        os.system("clear")
        print("******************** eBooker v" + version + " ********************")
        print("")
        sleep(1)
    elif cmd == "debug":
        print("Debugging help for MacOS/*nix version:")
        print("Email me at ebooker.support@zoho.com with the error code for the error message you encountered.")
        print("|-----------------------|--------|")
        print("|Message                |Code    |")
        print("|-----------------------|--------|")
        print("|nano: command not found|42912246|")
        print("|-----------------------|--------|")
        print("|'nano' is not          |53461349|")
        print("|recognized as an       |        |")
        print("|internal or external   |        |")
        print("|command, operable      |        |")
        print("|program or batch file. |        |")
        print("|-----------------------|--------|")
        print("|other message          |87376634|")
        print("|-----------------------|--------|")
    else:
        print("\"" + cmd + "\" is not a valid command. Type \"help\" for more options")
