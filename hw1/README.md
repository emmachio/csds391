Exercise 3/4/5:
The eightPuzzle.py file is the file with all the code regarding the 8-puzzle project including all the different functions and the state representation.
It is also within the eightPuzzle.py file that the command cmdfile is written, making it so that the command file can be inputting in the terminal.

Exercise 6:
There are three test files, to ensure that every part of the functions are working as expected. The three test files are
	testcmds.txt
	testcmds2.txt
	testcmds3.text
In order to run these files, put the following into the terminal
	python3 eightPuzzle.py testcmds.txt
	python3 eightPuzzle.py testcmds2.txt	
	python3 eightPuzzle.py testcmds3.txt
* There is a chance that it may be python instead of python3 for you, it just happens for me that I need to write python3 in the terminal in order for it to run
Each of the test files are focused on testing different parts of the function such as, making sure that they work when they are supposed to and catching error in cases of invalid commands. What each test case specifically tests is listed in the HW PDF file, however listed below is a summary of what each test case tests
	testcmds.txt - general function (in cases where it should work, how it is working
	testcmds2.txt - invalid moves directions (in cases where the blank tile cannot move - the move function should recognize that)
	testcmds3.txt - invalid commands and states (in cases where the command is not one that is listed or the state is not a valid state such as duplicate values, value over 9, or more than 9 tiles)
