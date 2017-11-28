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
            "|An internal error      |89322810|\n"
            "|occurred. Program      |        |\n"
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