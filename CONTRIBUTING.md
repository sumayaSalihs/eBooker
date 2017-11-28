# Contributing

## Branches

* Work in the `development` branch.
* When the code in `development` is stable and has made a signifigant change, merge `development` into `master`.
* I will periodically create backup branches such as `Backup`, `Backup2`, etc. The names of these and other protected branches will be capitalized at the beginning.
* Please do not create any other branches; if there is a specific reason why you have to, email me at [archmaster@yahoo.com](mailto:archmaster@yahoo.com).

## Conventions

* Internal variables such as `__version__` are surrounded by two underscores on both sides.
* Class names such as `Tester` have a capital letter at the beginning of each word.
* Other variables and functions such as `printDebug` have a capital letter at the beginning of every word but the first.
* Space everything out and add comments
* Work hard
* Have fun

## Files

* `ebooker.py` - the main file that brings everything else together.
* `commands.py` - all of the commands that can be run from the eBooker console.
* `internals.py` - internal variables.
* `extras.py` - extra functions run in the other Python programs.
* `tester.py` - tests run in CircleCI builds and in `ebooker.py`.
* `docs/` - the website.