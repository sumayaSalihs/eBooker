import os
os.system("clear");
print("******************** eBooker ********************")
print("")

while True:
	cmd = input("ebooker > ")
	if cmd == "help":
		print("Help is on the way!");
	else:
		print("You entered: " + cmd + ".")