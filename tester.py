#!/usr/bin/env python3

import os
import sys

is_python_3 = sys.version_info[0] >= 3

# define get_input
get_input = (lambda message: str(input(message))) if is_python_3 \
                                                else raw_input
class Tester(object):
    def test(self):
        try:
            assert (
                os.path.exists("docs/stylesheet.css") and
                os.path.exists("README.md") and
                os.path.exists("docs/index.html") and
                os.path.exists("ebooker.py") and
                os.path.exists("docs") and
                type(self) is Tester
            )
        except:
            print("\nAn internal error occurred!")
            print("Program execution stopped. Type RETURN to exit.")

            get_input("")
            sys.exit(1)

if __name__ == "__main__":
    Tester().test()
    sys.exit(0)