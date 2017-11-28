#!/usr/bin/env python3

#Imports
import os
import sys
from extras import getInput, isPython3, isNix

# Define Tester class
class Tester(object):
    def test(self, n):
        try:
            assert (
                # Test for README.md, tester.py, and ebooker.py
                os.path.exists("README.md") and
                os.path.exists("tester.py") and
                os.path.exists("ebooker.py") and
                type(self) is Tester
            )
            if n:
                assert (
                    # If running in CircleCI...
                    # Test for docs/ and contents.
                    os.path.exists("docs/stylesheet.css") and
                    os.path.exists("docs/index.html") and
                    os.path.exists("docs") and
                    type(self) is Tester
                )
        except:
            # Tests failed
            print("\nAn internal error occurred!")
            print("Program execution stopped. Type RETURN to exit.")
            print("If you didn't, always cd into eBooker's folder before running this program.")
            
            # Wait for RETURN, then exit
            getInput("")
            sys.exit(1)

if __name__ == "__main__":
    # Running in CircleCI
    Tester().test(1)
    sys.exit(0)