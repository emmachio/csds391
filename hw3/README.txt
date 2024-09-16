Exercise 4. Heuristic Function
	The heuristic function is within the eightPuzzle class and called heuristic. It takes an input of either h1 or h2 to determine which of the heuristic functions to use. Then it will calculate the heuristic function on the eightPuzzle object that it is called on. The in depth of how it is calculating this is further explained in the written homework. However, it does not print the heuristic value because the A* search calls it hundreds of times and it would print each time if I added the print function.

Exercise 5. Repeated State checking
	The repeated state checking is within the Asearch function, particularly the visited queue. It keeps track of the states that have already been visited and checked so that in the case that the state is reached again, the algorithm will know that it has already been searched and does not need to run the algorithm on it again. An in depth explanation of my implementation of the repeated state checking is on the written homework.

Exercise 6. A* Search
	The A* search algorithm is the Asearch function. However, it is called in the solve function so that it can be called from the testcmds.txt file. It inputs the desired heuristic function (either h1 or h2) and then works based off of that. A more in depth explanation of the code can be found in the written homework.

Exercise 7. Test File
	The test file is the testcmds.txt file. The contents and the expected output will be put into the written homework. Additionally, because the heuristic functions do not print their value, there is code in the python file to print the heuristic values that will print when it is run. Commands can be put in the way requested and the commands can be called by writing in the terminal:
	python3 eightPuzzle.py testcmds.txt 
	* there is a chance it might be python for you, it is python3 for me

