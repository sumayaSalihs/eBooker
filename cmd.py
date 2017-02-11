#!/usr/bin/env python3
version = "0.1"

from time import sleep
import sys
import os
os.system("clear")
print("Loading...")
sleep(3)
os.system("clear")
print("******************** eBooker v" + version + " ********************")
print("")
sleep(1)

helpString = "eBooker v" + version + " Help\n==============" + ("=" * len(version)) + "\nhelp - show this help\nexit - quit this session\nabout - read about this tool\nedit - edit a file\nclear -  clear the screen"
aboutString = "eBooker\nA command-line tool written in Python for writing Kindle eBooks. So far, it will just execute simple commands like \"help\" and \"exit.\""
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
			elif editBool == "n":
				editloopBool = False
				print("You want to edit an existing file!")
			else:
				print("Please type in \"y\" or  \"n\".")
	elif cmd == "clear":
		print("Clearing...")
		sleep(2)
		os.system("clear")
		print("******************** eBooker v" + version + " ********************")
		print("")
		sleep(1)
	else:
		print("\"" + cmd + "\" is not a valid command. Type \"help\" for more options")