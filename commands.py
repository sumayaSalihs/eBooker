# Imports
from tester import Tester
from extras import banner, getInput, isPython3, isNix, augment, clear, openEditor, chapNum, printDebug
import internals
import sys, os, codecs, webbrowser, glob

# Define Com class
class Com(object):
    def debug(self):
        # Print debugging info (see printDebug() in extras.py)
        print("Debugging help for MacOS/*nix version:")
        printDebug()

    def clear(self):
        # Clear screen
        print("Clearing...")
        clear()
        banner("eBooker", "#")

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

        while editloopBool:
            # Check whether user wants to create a new chapter or edit an existing one
            editBool = getInput(
                "Would you like to create a new chapter? (y/n) "
            )

            if editBool == "y":
                # User wants to create a new chapter
                editloopBool = False
                print("You want to create a new chapter.")

                newfileString = chapNum()

                # Create and open file unless file already exists
                print("Creating file...")

                newfileString = "chapter-" + str(newfileString) + ".html"
                if not os.path.exists(newfileString):
                    # File doesn't exist
                    newfileFile = codecs.open(
                        newfileString, "a", "utf-8"
                    )

                    # Put stuff in file based on OS
                    if isNix:
                        newfileFile.write(
                            "Press CTRL-O then hit return to save. Press CTRL-X to exit.\n"
                        )
                        newfileFile.write(
                            "Don't worry if you can't see part of your lines; they will\n"
                        )
                        newfileFile.write(
                            "be saved anyway."
                        )
                    else:
                        newfileFile.write(
                            "Press CTRL-S to save. Click on the X to exit.\n"
                        )

                    # Close file
                    newfileFile.close()

                    print("Your file is created!")

                    # Open file for editing
                    openEditor(newfileString)

                    # Notify user about debug command
                    print("If you got an error, use the \"debug\" command.")
                else:
                    # File does exist
                    print("That chapter already exists! Try running the edit command again but this time enter \"n\".")

            elif editBool == "n":
                # User wants to create a new file
                editloopBool = False

                print("You want to edit an existing chapter!")

                editfileString = chapNum();

                # Open file for editing unless file doesn't exist
                print("Opening file for editing...")

                editfileString = "chapter-" + str(editfileString) + ".html"
                if os.path.exists(editfileString):
                    # File exists
                    openEditor(editfileString)

                    # Notify user about debug command
                    print("If you got an error, use the \"debug\" command.")
                else:
                    # File doesn't exist
                    print("That file doesn't exist. Try running the edit command again but this time enter \"y\".")
            else:
                # User didn't type in y or n
                print("Please type in \"y\" or  \"n\".")


    def about(self):
        # Display information about eBooker (see __about_string__ in internals.py)
        print(internals.__about_string__)

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
        print(internals.__help_string__)

    def docs(self):
        # Display documentation in web browser
        print("Serving documentation...")

        # Find and read README.md
        docnameString = os.path.dirname(os.path.realpath(__file__)) + "/README.md"
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
