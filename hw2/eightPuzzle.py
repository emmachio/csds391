import random
import sys
from collections import deque
import copy

class Puzzle:
    # global functions that keep track of the puzzle and the location of the blank tile
    puzzle = []
    blankTile = -1

    def __init__(self, value=None):
        global puzzle
        self.puzzle=value

    # setState command where it will set the puzzle into the desired state but inputting it into the
    # global variable puzzle
    def setState(self, puzzleState):
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
    def printState(self):
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
    def move(self, direction):
        global puzzle
        global blankTile
        result = ""
        # if the tile goes up, then it's index decreases by 3 but if it goes below 0, then that means the blank
        # tile is on the first row and cannot be moved up, thus an invalid move, otherwise a switch of values will occur
        # which will act as the tile moving up
        if direction == "up":
            if blankTile-3 < 0:
                print("Error: Invalid move")
            else:
                puzzle[blankTile]= puzzle[blankTile-3]
                puzzle[blankTile-3]=0
                blankTile = blankTile-3
                print("Blank tile successfully moved up:")
                self.printState()
        # if the tile goes down, then it's index increases by 3 but if it goes above 8, then that means the blank
        # tile is on the last row and cannot be moved down, thus an invalid move, otherwise a switch of values will occur
        # which will act as the tile moving down
        elif direction == "down":
            if blankTile+3 > 8:
                print("Error: Invalid move")
            else:
                puzzle[blankTile]= puzzle[blankTile+3]
                puzzle[blankTile+3]=0
                blankTile = blankTile+3
                print("Blank tile successfully moved down:")
                self.printState()
        # if the tile goes left, then it's index decreases by 1 but if index modulo 3 is equal to 0, then that means the blank
        # tile is on the left most column and cannot be moved left, thus an invalid move, otherwise a switch of values will occur
        # which will act as the tile moving left
        elif direction == "left":
            if blankTile%3==0:
                print("Error: Invalid move")
            else:
                puzzle[blankTile]= puzzle[blankTile-1]
                puzzle[blankTile-1]=0
                blankTile = blankTile-1
                print("Blank tile successfully moved left:")
                self.printState()
        # if the tile goes right, then it's index increases by 1 but if index modulo 3 is equal to 2, then that means the blank
        # tile is on the right most column and cannot be moved right, thus an invalid move, otherwise a switch of values will occur
        # which will act as the tile moving right
        elif direction == "right":
            if blankTile%3==2:
                print("Error: Invalid move")
            else:
                puzzle[blankTile]= puzzle[blankTile+1]
                puzzle[blankTile+1]=0
                blankTile = blankTile+1
                print("Blank tile successfully moved right:")
                self.printState()
        else:
            print("Error: Invalid command: move " + direction)
            return "Error: Invalid move"

# a helper move function that returns error message so that the scrambleState can check it
    def helperMove(self, direction):
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

    # def moveResult(self, direction):
    #     global puzzle
    #     global blankTile
    #     referencePuzzle = copy.deepcopy(puzzle)
    #     referenceBlankTile = blankTile
    #     # if the tile goes up, then it's index decreases by 3 but if it goes below 0, then that means the blank
    #     # tile is on the first row and cannot be moved up, thus an invalid move, otherwise a switch of values will occur
    #     # which will act as the tile moving up
    #     if direction == "up":
    #         if referenceBlankTile-3 < 0:
    #             return "Error: Invalid move"
    #         else:
    #             referencePuzzle[referenceBlankTile]= referencePuzzle[referenceBlankTile-3]
    #             referencePuzzle[referenceBlankTile-3]=0
    #             return referencePuzzle
    #     # if the tile goes down, then it's index increases by 3 but if it goes above 8, then that means the blank
    #     # tile is on the last row and cannot be moved down, thus an invalid move, otherwise a switch of values will occur
    #     # which will act as the tile moving down
    #     elif direction == "down":
    #         if referenceBlankTile+3 > 8:
    #             return "Error: Invalid move"
    #         else:
    #             referencePuzzle[referenceBlankTile]= referencePuzzle[referenceBlankTile+3]
    #             referencePuzzle[referenceBlankTile+3]=0
    #             return referencePuzzle
    #     # if the tile goes left, then it's index decreases by 1 but if index modulo 3 is equal to 0, then that means the blank
    #     # tile is on the left most column and cannot be moved left, thus an invalid move, otherwise a switch of values will occur
    #     # which will act as the tile moving left
    #     elif direction == "left":
    #         if referenceBlankTile%3==0:
    #             return "Error: Invalid move"
    #         else:
    #             referencePuzzle[referenceBlankTile]= referencePuzzle[referenceBlankTile-1]
    #             referencePuzzle[referenceBlankTile-1]=0
    #             return referencePuzzle
    #     # if the tile goes right, then it's index increases by 1 but if index modulo 3 is equal to 2, then that means the blank
    #     # tile is on the right most column and cannot be moved right, thus an invalid move, otherwise a switch of values will occur
    #     # which will act as the tile moving right
    #     elif direction == "right":
    #         if referenceBlankTile%3==2:
    #             return "Error: Invalid move"
    #         else:
    #             referencePuzzle[referenceBlankTile]= referencePuzzle[referenceBlankTile+1]
    #             referencePuzzle[referenceBlankTile+1]=0
    #             return referencePuzzle
    #     else:
    #         return "Error: Invalid move"

    # command scrambleState which will move the blank tile in a random direction as generated by the random function
    # As the goal state is not always achievable, we begin with the goal state and move the blank tile from there
    # If it is the case where the blank tile cannot be moved (ex: moving down when the blank tile is on the last row),
    # it will add an iteration so that it will reattempt
    def scrambleState(self, n):
        self.setState("0 1 2 3 4 5 6 7 8")
        i=0
        random.seed(42)
        while(i < n):
            randomValue=random.randint(1,4)
            if randomValue % 4 == 0:
                if self.helperMove("up") == "Error: Invalid move":
                    n+=1
            elif randomValue % 4 == 1:
                if self.helperMove("down") == "Error: Invalid move":
                    n+=1
            elif randomValue % 4 == 2:
                if self.helperMove("left") == "Error: Invalid move":
                    n+=1
            elif randomValue % 4 == 3:
                if self.helperMove("right") == "Error: Invalid move":
                    n+=1
            i+=1
        self.printState()

    def getState(self):
        global puzzle
        return puzzle

    def equals(self, comparedPuzzle):
        global puzzle
        return puzzle == comparedPuzzle.getState

    # command function where it takes a command string and the required input as an input
    def cmd(self, commandString):
        # if there is a space in the command, then it will split it as the command and its input
        if " " in commandString:
            command, inputs = commandString.split(" ", 1)
        # otherwise, it is just a command
        else:
            command = commandString
            inputs = ""
        # if the command is setState, calling the function setState with the desired input
        if command == "setState":
            self.setState(inputs)
        # if the command is move, calling the function in the desired direction
        elif command == "move":
            self.move(inputs)
        # if the command is scrambleState, calling the function with the desired number of scrambled moves
        elif command == "scrambleState":
            self.scrambleState(int(inputs))
        # if the command is printState, calling the function printState
        # putting a space before so in the instance of two printState's they will not merge
        elif command == "printState":
            self.printState()
        # if the command is none of the above, error message is given with the invalid command
        else:
            print("Error: invalid command: " + commandString)

    # cmdfile function where it intakes the filename, reads its contents and does the
    # functions found within the file
    # if the file could not be found, catch the error and state that the file is nto found
    def cmdfile(self, filename):
        try:
            with open(filename, "r") as reader:
                for line in reader:
                    line = line.strip()
                    if line.charAt(1)!= '#' and line.substring(2) != "\\":
                        self.cmd(line)
        except FileNotFoundError:
            print("Error: file name " + filename + " not found")

class Node:
    currentState = Puzzle()
    nextNode = None
    previousNode = None
    moveDone = None

# constructor that sets the currentState to the provided Node and everything else as none
    def __init__(self, givenState, move):
        global currentState
        global nextNode
        global previousNode
        global moveDone
        currentState = givenState
        nextNode = None
        previousNode = None
        moveDone = move

# function that sets the current state as given state
    def setState(self, givenState):
        global currentState
        currentState = givenState

# function that sets the previous state as given state
    def setPrev(self, givenState):
        global previousNode
        previousNode = givenState

# function that sets the next state as given state
    def setNext(self, givenState):
        global nextNode
        nextNode = givenState

# function that sets the next move as given move
    def setMove(self, move):
        global moveDone
        moveDone = move

# function that returns the state
    def getState(self):
        global currentState
        return  currentState

# function that returns the previous state
    def getPrev(self):
        global previousNode
        return previousNode

# function that returns the next state
    def getNext(self):
        global nextNode
        return nextNode

    def getMove(self):
        global moveDone
        return moveDone

# function that returns whether or not the Node has next
    def hasNext(self):
        global nextNode
        return nextNode != None

class linkedList:
    first = Node(Puzzle(), -1)
    size = -1

    def __init__(self, firstState):
        global first
        global size
        first = firstState
        first.setMove(-1)
        size = 1

    def add(self, addedNode):
        global first
        global size
        current = first
        while (current.hasNext):
            current = current.getNext()
        current.setNext(addedNode)
        size = size + 1

# main function that takes it so that the file name can be given in the terminal
# checks to make sure that there are two arguments in the terminal before calling on the second
# input of the terminal which is the command file
def main():
    testPuzzle = Puzzle()
    if len(sys.argv) > 1:
        commandFile = sys.argv[1]
        testPuzzle.cmdfile(commandFile)

if __name__ == "__main__":
    main()

def moveResult(referencePuzzle, direction):
    referenceBlankTile = -1
    for i in range(9):
        if referencePuzzle[i]==0:
            referenceBlankTile = i
    print(referenceBlankTile)
    # if the tile goes up, then it's index decreases by 3 but if it goes below 0, then that means the blank
    # tile is on the first row and cannot be moved up, thus an invalid move, otherwise a switch of values will occur
    # which will act as the tile moving up
    if direction == "up":
        if referenceBlankTile-3 < 0:
            return "Error: Invalid move"
        else:
            referencePuzzle[referenceBlankTile]= referencePuzzle[referenceBlankTile-3]
            referencePuzzle[referenceBlankTile-3]=0
            return referencePuzzle
    # if the tile goes down, then it's index increases by 3 but if it goes above 8, then that means the blank
    # tile is on the last row and cannot be moved down, thus an invalid move, otherwise a switch of values will occur
    # which will act as the tile moving down
    elif direction == "down":
        if referenceBlankTile+3 > 8:
            return "Error: Invalid move"
        else:
            referencePuzzle[referenceBlankTile]= referencePuzzle[referenceBlankTile+3]
            referencePuzzle[referenceBlankTile+3]=0
            return referencePuzzle
    # if the tile goes left, then it's index decreases by 1 but if index modulo 3 is equal to 0, then that means the blank
    # tile is on the left most column and cannot be moved left, thus an invalid move, otherwise a switch of values will occur
    # which will act as the tile moving left
    elif direction == "left":
        if referenceBlankTile%3==0:
            return "Error: Invalid move"
        else:
            referencePuzzle[referenceBlankTile]= referencePuzzle[referenceBlankTile-1]
            referencePuzzle[referenceBlankTile-1]=0
            return referencePuzzle
    # if the tile goes right, then it's index increases by 1 but if index modulo 3 is equal to 2, then that means the blank
    # tile is on the right most column and cannot be moved right, thus an invalid move, otherwise a switch of values will occur
    # which will act as the tile moving right
    elif direction == "right":
        if referenceBlankTile%3==2:
            return "Error: Invalid move"
        else:
            referencePuzzle[referenceBlankTile]= referencePuzzle[referenceBlankTile+1]
            referencePuzzle[referenceBlankTile+1]=0
            return referencePuzzle
    else:
        return "Error: Invalid move"

# startState and goalState input should both be Puzzle object
def solveBFS(startState, goalState, maxNode):
    firstState = Node(startState, -1)
    if(startState.equals(goalState)):
        return firstState
    # frontier and reached states are queues of Nodes
    frontier = deque()
    reachedStates = deque()
    frontier.append(firstState)
    reachedStates.append(firstState)
    while len(frontier) != 0:
        current = frontier.popleft()
        currentValue = current.getState().getState().copy()
        currentMove = current.getMove()
        # # making the puzzle state where it moves
        # moveUpResult = current.moveResult("up")
        # if moveUpResult != "Error: Invalid move":
        #     moveUp = Puzzle(moveUpResult("up"))
        #     moveUpNode = Node(moveUp, "up")
        #     moveUpNode.setPrev(current)
        #     # possibleStates.add(moveUpNode)
        #     print("1")
        #     # checking the move up state
        #     if moveUp.equals(goalState):
        #         return moveUpNode
        #     if moveUp not in reachedStates:
        #         frontier.append(moveUp)
        #         reachedStates.append(moveUp)
        #
        # moveDownResult = current.moveResult("down")
        # if moveDownResult != "Error: Invalid move":
        #     moveDown = Puzzle(current.moveResult("down"))
        #     moveDownNode = Node(moveDown, "down")
        #     moveDownNode.setPrev(current)
        #     # possibleStates.add(moveDownNode)
        #     print("2")
        #     # checking the move down state
        #     if moveDown.equals(goalState):
        #         return moveDownNode
        #     if moveDown not in reachedStates:
        #         frontier.append(moveDown)
        #         reachedStates.append(moveDown)
        # current is a puzzle
        moveLeftResult = moveResult(current.getState().getState(), "left")
        current = Node(Puzzle(currentValue), currentMove)
        if moveLeftResult != "Error: Invalid move":
            leftPuzzle = Puzzle([8, 7,6, 5, 4, 3, 2, 1, 0])
            moveLeftNode = Node(Puzzle(), "left")
            moveLeft = Puzzle()
            moveLeft.printState()
            moveLeftNode.setPrev(current)
            moveLeftNode.setState(moveLeft)
            # checking the move left state
            if moveLeft.getState()==goalState.getState():
                return moveLeftNode
            if moveLeft not in reachedStates:
                # moveLeft.printState()
                frontier.append(moveLeftNode)
                reachedStates.append(moveLeftNode)

        # moveRightResult = current.moveResult("right")
        # if moveRightResult != "Error: Invalid move":
        #     moveRight = Puzzle(current.moveResult("right"))
        #     moveRightNode = Node(moveRight, "right")
        #     moveRightNode.setPrev(current)
        #     # possibleStates.add(moveRightNode)
        #     print("4")
        #     # checking the move right state
        #     if moveRight.equals(goalState):
        #         return moveRightNode
        #     if moveRight not in reachedStates:
        #         frontier.append(moveRight)
        #         reachedStates.append(moveRight)
    return None

goalPuzzle = Puzzle()
goalPuzzle.setState("0 1 2 3 4 5 6 7 8")
testPuzzle = Puzzle()
testPuzzle.setState ("1 0 2 3 4 5 6 7 8")
testPuzzle.printState()
print("solveBFS result")
solveBFS(testPuzzle, goalPuzzle, 1000)
testing = solveBFS(testPuzzle, goalPuzzle, 1000)
print("end")
testing.getState().printState()
testing = testing.getPrev()
print("prev")
testing.getState().printState()

# testPuzzle = Puzzle()
# testPuzzle.setState ("1 0 2 3 4 5 6 7 8")
# print(testPuzzle.getState())
# print(testPuzzle.moveResult("left"))
# print(testPuzzle.getState())
# print("testing")
# print(moveResult([1, 0, 2, 3, 4, 5, 6, 7, 8], "left"))