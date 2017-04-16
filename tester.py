import os
import sys
py3 = False
if sys.version_info[0] >= 3:
	py3 = True
def get_input(message):
	if py3 == True:
		return str(input(message))
	else:
		return raw_input(message)
def tests():
    try:
        assert os.path.exists("docs/stylesheet.css")
        assert os.path.exists("README.md")
        assert os.path.exists("docs/index.html")
        assert os.path.exists("ebooker.py")
        assert os.path.exists("docs")
        return
    except:
        print("")
        print("An internal error occurred!")
        print("Program execution stopped. Type RETURN to exit.")
        errorloopBool = True
        while errorloopBool:
            errorBool = get_input("")
            sys.exit(1)
if __name__ == "__main__":
    try:
        assert os.path.exists("docs/stylesheet.css")
        assert os.path.exists("README.md")
        assert os.path.exists("docs/index.html")
        assert os.path.exists("ebooker.py")
        assert os.path.exists("docs")
    except:
        sys.exit(1)
    sys.exit(0)