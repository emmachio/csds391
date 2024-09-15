Exercise 5:
The eightPuzzle.py file is the file with all the code regarding implementing DFS and BFS as well as the actual function solve which takes in which type of search to do as an input.
In order to input a maxnode limit, it has to be put into the test file such as:
	solve dfs maxnodes=(1000)
where 1000 would be the desired input of maximum number of nodes. either dfs or bfs could be inputting and it will work.
without the check that a node has been previously visited, the code will give a recursion error that the maximum number recursion calls have been reached. As a result of this, I have set the default to be 900 (which has shown to be able to work without crashing out the computer, however without the check it will not provide a result)

Exercise 6:
I have created a test file to ensure that it will run both dfs and bfs with the default amount of maximum nodes (1000), as well as running with a given maximum number of nodes. I have annotated within the testfile to explain what each command is hoping to test.
In order to run the file, put the following into the termina.
	python3 eightPuzzle.py testcmds.txt
* There is a chance that it may be python instead of python3 for you, it just happens for me that I need to write python3 in the terminal in order for it to run
What the expected output is and why it is is listed in the HW PDF file.

Exercise 7:
I have added lines into the cmd function so that it can recognize which lines should be treated as comments. These lines are then identified and printed.
Additionally, the lines that have been recognized as commands, have also been printed.