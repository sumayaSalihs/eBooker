#!/usr/bin/python3
version = "0.1"

import os
os.system("clear");
print("******************** eBooker v" + version + " ********************")
print("")

helpString = "eBooker v" + version + " Help\n==============" + ("=" * len(version)) + "\nOptions:\nhelp - show this help\nexit - quit this session"

while True:
	cmd = str(input("ebooker > "))
	if cmd == "help":
		print(helpString)
	else:
		print("That is not a valid command.")