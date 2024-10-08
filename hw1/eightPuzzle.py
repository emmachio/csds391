import random
import sys

# global functions that keep track of the puzzle and the location of the blank tile
puzzle = []
blankTile = -1

# setState command where it will set the puzzle into the desired state but inputting it into the
# global variable puzzle
def setState(puzzleState):
    global puzzle
    global blankTile
    # splitting the string of puzzleState by space so that each element within the string is its own value so it can be
    # inputting into the list
    elementsSplit = puzzleState.split()
    puzzle = [int(element) for element in elementsSplit]
    # checking to make sure that there are no duplicate values by using default property of sets
    # as well as checking that there are only 9 input values
    duplicatesCheck = len(puzzle) == len(set(puzzle))
    if duplicatesCheck != True or len(puzzle) > 9:
        print("Error: invalid puzzle state")
    # checking to make sure that none of the values are greater than 9 while also keeping track of
    # where the blank tile is within the gloabl variable blankTile
    else:
        for i in range(9):
            if puzzle[i] > 9:
                print("Error: invalid puzzle state")
                exit()
            elif(puzzle[i]==0):
                blankTile = i
        print("puzzle state set")

# printState function where it converts the puzzle into a 3x3 matrix where the empty tile is blank rather than a 0
def printState():
    global puzzle
    line1 = []
    line2 = []
    line3 = []
    for i in range(3):
        if puzzle[i]==0:
            line1.append(" ")
        else:
            line1.append(puzzle[i])
    for i in range(3,6):
        if puzzle[i]==0:
            line2.append(" ")
        else:
            line2.append(puzzle[i])
    for i in range(6,9):
        if puzzle[i]==0:
            line3.append(" ")
        else:
            line3.append(puzzle[i])
    board = [line1, line2, line3]
    print("Current state of board:")
    for row in board:
        print(row)
    print("")

# move function where it moves in the direction specified unless it is not possible
def move(direction):
    global puzzle
    global blankTile
    result = ""
    # if the tile goes up, then it's index decreases by 3 but if it goes below 0, then that means the blank
    # tile is on the first row and cannot be moved up, thus an invalid move, otherwise a switch of values will occur
    # which will act as the tile moving up
    if direction == "up":
        if blankTile-3 < 0:
            print("Error: Invalid move")
            return "Error: Invalid move"
        else:
            puzzle[blankTile]= puzzle[blankTile-3]
            puzzle[blankTile-3]=0
            blankTile = blankTile-3
            print("Blank tile successfully moved up:")
            printState()
    # if the tile goes down, then it's index increases by 3 but if it goes above 8, then that means the blank
    # tile is on the last row and cannot be moved down, thus an invalid move, otherwise a switch of values will occur
    # which will act as the tile moving down
    elif direction == "down":
        if blankTile+3 > 8:
             print("Error: Invalid move")
             return "Error: Invalid move"
        else:
            puzzle[blankTile]= puzzle[blankTile+3]
            puzzle[blankTile+3]=0
            blankTile = blankTile+3
            print("Blank tile successfully moved down:")
            printState()
    # if the tile goes left, then it's index decreases by 1 but if index modulo 3 is equal to 0, then that means the blank
    # tile is on the left most column and cannot be moved left, thus an invalid move, otherwise a switch of values will occur
    # which will act as the tile moving left
    elif direction == "left":
        if blankTile%3==0:
            print("Error: Invalid move")
            return "Error: Invalid move"
        else:
            puzzle[blankTile]= puzzle[blankTile-1]
            puzzle[blankTile-1]=0
            blankTile = blankTile-1
            print("Blank tile successfully moved left:")
            printState()
    # if the tile goes right, then it's index increases by 1 but if index modulo 3 is equal to 2, then that means the blank
    # tile is on the right most column and cannot be moved right, thus an invalid move, otherwise a switch of values will occur
    # which will act as the tile moving right
    elif direction == "right":
        if blankTile%3==2:
            print("Error: Invalid move")
            return "Error: Invalid move"
        else:
            puzzle[blankTile]= puzzle[blankTile+1]
            puzzle[blankTile+1]=0
            blankTile = blankTile+1
            print("Blank tile successfully moved right:")
            printState()
    else:
        print("Error: Invalid command: move " + direction)

def helperMove(direction):
    global puzzle
    global blankTile
    result = ""
    # if the tile goes up, then it's index decreases by 3 but if it goes below 0, then that means the blank
    # tile is on the first row and cannot be moved up, thus an invalid move, otherwise a switch of values will occur
    # which will act as the tile moving up
    if direction == "up":
        if blankTile-3 < 0:
            return "Error: Invalid move"
        else:
            puzzle[blankTile]= puzzle[blankTile-3]
            puzzle[blankTile-3]=0
            blankTile = blankTile-3
    # if the tile goes down, then it's index increases by 3 but if it goes above 8, then that means the blank
    # tile is on the last row and cannot be moved down, thus an invalid move, otherwise a switch of values will occur
    # which will act as the tile moving down
    elif direction == "down":
        if blankTile+3 > 8:
            return "Error: Invalid move"
        else:
            puzzle[blankTile]= puzzle[blankTile+3]
            puzzle[blankTile+3]=0
            blankTile = blankTile+3
    # if the tile goes left, then it's index decreases by 1 but if index modulo 3 is equal to 0, then that means the blank
    # tile is on the left most column and cannot be moved left, thus an invalid move, otherwise a switch of values will occur
    # which will act as the tile moving left
    elif direction == "left":
        if blankTile%3==0:
            return "Error: Invalid move"
        else:
            puzzle[blankTile]= puzzle[blankTile-1]
            puzzle[blankTile-1]=0
            blankTile = blankTile-1
    # if the tile goes right, then it's index increases by 1 but if index modulo 3 is equal to 2, then that means the blank
    # tile is on the right most column and cannot be moved right, thus an invalid move, otherwise a switch of values will occur
    # which will act as the tile moving right
    elif direction == "right":
        if blankTile%3==2:
            return "Error: Invalid move"
        else:
            puzzle[blankTile]= puzzle[blankTile+1]
            puzzle[blankTile+1]=0
            blankTile = blankTile+1
    else:
        return "Error: Invalid move"
# command scrambleState which will move the blank tile in a random direction as generated by the random function
# As the goal state is not always achievable, we begin with the goal state and move the blank tile from there
# If it is the case where the blank tile cannot be moved (ex: moving down when the blank tile is on the last row),
# it will add an iteration so that it will reattempt
def scrambleState(n):
    setState("0 1 2 3 4 5 6 7 8")
    i=0
    random.seed(42)
    while(i < n):
        randomValue=random.randint(1,4)
        if randomValue % 4 == 0:
            if helperMove("up") == "Error: Invalid move":
                n+=1
        elif randomValue % 4 == 1:
            if helperMove("down") == "Error: Invalid move":
                n+=1
        elif randomValue % 4 == 2:
            if helperMove("left") == "Error: Invalid move":
                n+=1
        elif randomValue % 4 == 3:
            if helperMove("right") == "Error: Invalid move":
                n+=1
        i+=1
    printState()

# command function where it takes a command string and the required input as an input
def cmd(commandString):
    # if there is a space in the command, then it will split it as the command and its input
    if " " in commandString:
        command, inputs = commandString.split(" ", 1)
    # otherwise, it is just a command
    else:
        command = commandString
        inputs = ""
    # if the command is setState, calling the function setState with the desired input
    if command == "setState":
        setState(inputs)
    # if the command is move, calling the function in the desired direction
    elif command == "move":
        move(inputs)
    # if the command is scrambleState, calling the function with the desired number of scrambled moves
    elif command == "scrambleState":
        scrambleState(int(inputs))
    # if the command is printState, calling the function printState
    # putting a space before so in the instance of two printState's they will not merge
    elif command == "printState":
        printState()
    # if the command is none of the above, error message is given with the invalid command
    else:
        print("Error: invalid command: " + commandString)

# cmdfile function where it intakes the filename, reads its contents and does the
# functions found within the file
# if the file could not be found, catch the error and state that the file is nto found
def cmdfile(filename):
    try:
        with open(filename, "r") as reader:
            for line in reader:
                line = line.strip()
                cmd(line)
    except FileNotFoundError:
        print("Error: file name " + filename + " not found")

# main function that takes it so that the file name can be given in the terminal
# checks to make sure that there are two arguments in the terminal before calling on the second
# input of the terminal which is the command file
def main():
    if len(sys.argv) > 1:
        commandFile = sys.argv[1]
        cmdfile(commandFile)

if __name__ == "__main__":
    main()
