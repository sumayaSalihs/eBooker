About
-----
This will currently be pseudo-code.
This file will contain code for a file structure (e.g. project files, etc.).

Goal
----
Home directory:
    ebooker.db
    eBooker Projects:
        My Awesome Book:
            chapter-1.html
            chapter-2.html
            etc.
            toc.txt
            meta.txt
            Media:
                image1.png
                image2.jpeg
                etc.
        Logs:
            log1.log
            log2.log
    Desktop:
        eBooker:
            docs:
                index.html
                stylesheet.css
                etc.
            ebooker.py
            etc.

Pseudo-code
-----------
Find user home dir
Does ebooker.db exist?
Yes:
    Load it
No:
    Create it; loop
Does eBooker Projects exist?
Yes:
    Look for projects
    If some list them and give the option to open one
    Ask user if they want to create a new project
    Load regular ebooker.py but inside project folder
No:
    Create it; loop
    
Within ebooker
--------------
Add info to log file whenever something happens.

Note
----
Eventually, after I have replaced this with real code, I will write the rest of this pseudo code.
And after that-- of course-- I will replace THAT with real code.
And then all I have to do is continue sending Amazon annoyed emails :P