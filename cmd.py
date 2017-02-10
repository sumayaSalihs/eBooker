#!/usr/bin/python3
version = "0.1"

import sys
import os
os.system("clear");
print("******************** eBooker v" + version + " ********************")
print("")

helpString = "eBooker v" + version + " Help\n==============" + ("=" * len(version)) + "\nhelp - show this help\nexit - quit this session\nabout - read about this tool"
aboutString = "eBooker\nA command-line tool written in Python for writing Kindle eBooks. So far, it will just execute simple commands like \"help\" and \"exit\"."

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
	else:
		print("\"" + cmd + "\" is not a valid command. Type \"help\" for more options")
