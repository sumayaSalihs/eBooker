import sys, os, internals

# Check Python version
isPython3 = sys.version_info[0] >= 3

# Check if OS is Unix-based
isNix = os.name == "posix"

# Get user input
getInput = (lambda message: str(input(message))) if isPython3 \
                                                else raw_input

# Add HTML stuff to served book
def augment(filecontentsString, title):
    return "<!DOCTYPE html><html><head><title>" + title + \
        "</title></head>" + filecontentsString + "</body></html>"

# Print possible errors
def printDebug():
    print(
        "If you got an error message, send the developer an email at archmaster@yahoo.com with the appropriate error code as the subject. There is a list of errors and error codes below.\n"
        "|-----------------------|--------|\n"
        "|Message                |Code    |\n"
        "|-----------------------|--------|"
    )

    if isNix:
        print(
            "|An important project   |39672039|\n"
            "|file is missing!       |        |\n"
            "|Program execution      |        |\n"
            "|stopped.               |        |\n"
            "|-----------------------|--------|\n"
            "|An internal error      |40603285|\n"
            "|occurred. Program      |        |\n"
            "|execution stopped.     |        |\n"
            "|-----------------------|--------|\n"
            "|nano: command not found|42912246|\n"
            "|-----------------------|--------|\n"
            "|other message          |87376634|\n"
            "|-----------------------|--------|"
        )
    else:
        print(
            "|An important project   |70954281|\n"
            "|file is missing!       |        |\n"
            "|Program execution      |        |\n"
            "|stopped.               |        |\n"
            "|-----------------------|--------|\n"
            "|An internal error      |89322810|\n"
            "|occurred! Program      |        |\n"
            "|execution stopped.     |        |\n"
            "|-----------------------|--------|\n"
            "|'notepad' is not       |64485253|\n"
            "|recognized as an       |        |\n"
            "|internal or external   |        |\n"
            "|command, operable      |        |\n"
            "|program or batch file. |        |\n"
            "|-----------------------|--------|\n"
            "|other message          |93856898|\n"
            "|-----------------------|--------|"
        )

# Open the correct editor
def openEditor(fileString):
    if isNix:
        os.system("nano " + fileString)
    else:
        os.system("notepad " + fileString)

# Clear the terminal
def clear():
    if isNix:
        os.system("clear")
    else:
        os.system("cls")

def chapNum():
    while True:
        # Ask for chapter number
        chapnumString = getInput(
            "Please type in the chapter number. ")

        # Check if user entered something
        if (chapnumString == "") or (chapnumString is None) or (chapnumString == " "):
            print("You must enter a chapter number.")
        else:
            # Check if user entered a number
            try:
                chapnumString = int(chapnumString)
                break
            except ValueError:
                print("You must enter a number.")
    return chapnumString

# print banner
def banner(title, border='#'):
       v = internals.__version__
       frame_line =  border * (len(title) + len(v) + 8)
       print(frame_line.center(70))
       print('{0} {1} - v{2} {0}'.format(border, title, v).center(70))
       print(frame_line.center(70) + "\n")
