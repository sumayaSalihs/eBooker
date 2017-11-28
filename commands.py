# Imports
from tester import Tester
from extras import getInput, isPython3, isNix, augment, clear, openEditor
from internals import *
import sys, os, codecs, webbrowser, glob

# Define Com class
class Com(object):
    def printDebug(self):
        # Print debugging info (see printDebug() in extras.py)
        print("Debugging help for MacOS/*nix version:")
        debug()
        
    def clear(self):
        # Clear screen
        print("Clearing...")
        clear()
        print("******************** eBooker v" +
              __version__ + " ********************")
        print("")


    def serve(self):
        # Serve current book in a web browser
        print("Serving book...")
        
        # Get list of HTML files
        filenameArray = glob.glob(os.path.dirname(
            os.path.realpath(__file__)) + "/*.html")
        filebufferString = ""

        # For each HTML file...
        for filenameString in filenameArray:
            # Format filename
            newfilenameString = os.path.basename(filenameString)
            chapternameString = os.path.splitext(newfilenameString)[0]
            chapternameString = chapternameString.replace("-", " ", 1)
            chapternameString = chapternameString.capitalize()
            filebufferString += "<h1>" + chapternameString + "</h1>"
            
            # Open file and read contents
            filecontentsString = codecs.open(
                newfilenameString, "r", "utf-8").read()
            filebufferString += markdown.markdown(filecontentsString)
            
            # Add horizontal divider to end
            filebufferString += "<hr/>"
            
        # Add "THE END!"
        filebufferString += "<center><h1>THE END!</h1></center>"
        
        # Augment file (see augment() in extras.py)
        filebufferString = augment(filebufferString, "Your Book")
        
        # Write text to file
        reviewfileFile = codecs.open("review-book.html", "w", "utf-8")
        reviewfileFile.write(filebufferString)
        reviewfileFile.close()
        
        # Open in web browser
        webbrowser.open(
            "file://" + os.path.dirname(os.path.realpath(__file__)) + "/review-book.html")
        print(
            "Success! Your book is served. Press RETURN when you are done reviewing it."
        )

        # When user is done, delete the file
        getInput("")
        os.remove("review-book.html")

    def edit(self):
        # Edit or create a new file
        editloopBool = True

        while True:
            # Check whether user wants to create a new chapter or edit an existing one
            editBool = getInput(
                "Would you like to create a new chapter? (y/n) "
            )

            if editBool == "y":
                # User wants to create a new chapter
                editloopBool = False
                print("You want to create a new chapter.")

                while True:
                    # Ask for chapter number
                    newfileString = getInput(
                        "What would you like the chapter number to be? ")
                    
                    # Check if user entered something
                    if (newfileString == "") or (newfileString is None) or (newfileString == " "):
                        print("You must enter a chapter number.")
                    else:
                        # Check if user entered a number
                        try:
                            newfileString = int(newfileString)
                            break
                        except ValueError:
                            print("You must enter a number.")
                            
                # Create file
                print("Creating file...")

                newfileFile = codecs.open(
                    "chapter-" + str(newfileString) + ".html", "a", "utf-8"
                )
                newfileFile.write(
                    "Press CTRL-O then hit return to save. Press CTRL-X to exit.\n"
                )
                newfileFile.write(
                    "Don't worry if you can't see part of your lines; they will\n"
                )

                newfileFile.write("be saved anyway.")
                newfileFile.close()

                print("Your file is created!")
                
                # Open file for editing
                openEditor("chapter-" + str(newfileString) + ".html")

                # Notify user about debug command
                print("If you got an error, use the \"debug\" command.")

            elif editBool == "n":
                # User wants to create a new file
                editloopBool = False
                print("You want to edit an existing chapter!")

                while True:
                    # Ask for chapter number
                    editfileString = getInput(
                        "Please type in the chapter number. ")
                    
                    # Check if user entered something
                    if (editfileString == "") or (editfileString is None) or (editfileString == " "):
                        print("You must enter a chapter number.")
                    else:
                        # Check if user entered a number
                        try:
                            editfileString = int(editfileString)
                            break
                        except ValueError:
                            print("You must enter a number.")

                # Open file for editing
                print("Opening file for editing...")

                openEditor("chapter-" + str(editfileString) + ".html")

                # Notify user about debug command
                print("If you got an error, use the \"debug\" command.")
            else:
                # User didn't type in y or n
                print("Please type in \"y\" or  \"n\".")


    def about(self):
        # Display information about eBooker (see __about_string__ in internals.py)
        print(__about_string__)

    def exit(self):
        # Begin process to exit eBooker
        exitloopBool = True
        while exitloopBool:
            # Check if user wants to exit
            exitBool = getInput("Would you like to quit eBooker? (y/n) ")
            if exitBool == "y":
                # Yes, so...
                exitloopBool = False
                # Exit
                clear()
                sys.exit()
            elif exitBool == "n":
                # Nope. The user changed their mind.
                exitloopBool = False
                print("OK, not exited!")
            else:
                # User didn't type in y or n
                print("Please type in \"y\" or  \"n\".")

    def ehelp(self):
        # Print help (see __help_string__ in internals.py)
        print(__help_string__)

    def docs(self):
        # Display documentation in web browser
        print("Serving documentation...")
        
        # Find and read README.md
        docnameString = os.path.dirname(
            os.path.realpath(__file__)) + "/README.md"
        newdocnameString = os.path.basename(docnameString)
        doccontentsString = codecs.open(
            newdocnameString, "r", "utf-8").read()
        
        # Augment file (see augment() in extras.py)
        newdoccontentsString = markdown.markdown(doccontentsString)
        newdoccontentsString = augment(newdoccontentsString, "eBooker Documentation")
        
        # Write text to file
        docfileFile = codecs.open("docs.html", "w", "utf-8")
        docfileFile.write(newdoccontentsString)
        docfileFile.close()
        
        # Open in web browser
        webbrowser.open(
            "file://" + os.path.dirname(os.path.realpath(__file__)) + "/docs.html")
        print(
            "Success! The documentation has been served. Press RETURN when you are done reading it."
        )

        # When user is done, delete the file
        getInput("")
        os.remove("docs.html")