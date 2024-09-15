import random
import sys
from collections import deque
import heapq

class Puzzle:
    # global functions that keep track of the puzzle and the location of the blank tile

    def __init__(self, givenArray=[0,0,0,0,0,0,0,0,0]):
        self.puzzle = givenArray.copy()
        for i in range(9):
            if self.puzzle[i] == 0:
                self.blankTile = i


    # setState command where it will set the puzzle into the desired state but inputting it into the
    # global variable puzzle
    def setState(self, puzzleState):
        # splitting the string of puzzleState by space so that each element within the string is its own value so it can be
        # inputting into the list
        elementsSplit = puzzleState.split()
        self.puzzle = [int(element) for element in elementsSplit]
        # checking to make sure that there are no duplicate values by using default property of sets
        # as well as checking that there are only 9 input values
        duplicatesCheck = len(self.puzzle) == len(set(self.puzzle))
        if duplicatesCheck != True or len(self.puzzle) > 9:
            print("Error: invalid puzzle state")
        # checking to make sure that none of the values are greater than 9 while also keeping track of
        # where the blank tile is within the gloabl variable blankTile
        else:
            for i in range(9):
                if self.puzzle[i] > 9:
                    print("Error: invalid puzzle state")
                    exit()
                elif(self.puzzle[i]==0):
                    self.blankTile = i

    # printState function where it converts the puzzle into a 3x3 matrix where the empty tile is blank rather than a 0
    def printState(self):
        self.puzzle
        line1 = []
        line2 = []
        line3 = []
        for i in range(3):
            if self.puzzle[i]==0:
                line1.append(" ")
            else:
                line1.append(self.puzzle[i])
        for i in range(3,6):
            if self.puzzle[i]==0:
                line2.append(" ")
            else:
                line2.append(self.puzzle[i])
        for i in range(6,9):
            if self.puzzle[i]==0:
                line3.append(" ")
            else:
                line3.append(self.puzzle[i])
        board = [line1, line2, line3]
        print("Current state of board:")
        for row in board:
            print(row)
        print("")

    # move function where it moves in the direction specified unless it is not possible
    def move(self, direction):
        blankTile = self.blankTile
        puzzle = self.puzzle
        # if the tile goes up, then it's index decreases by 3 but if it goes below 0, then that means the blank
        # tile is on the first row and cannot be moved up, thus an invalid move, otherwise a switch of values will occur
        # which will act as the tile moving up
        if direction == "up":
            if blankTile-3 < 0:
                print("Error: Invalid move")
                return "Error: Invalid move"
            else:
                self.puzzle[self.blankTile]= self.puzzle[self.blankTile-3]
                self.puzzle[blankTile-3]=0
                self.blankTile = self.blankTile-3
        # if the tile goes down, then it's index increases by 3 but if it goes above 8, then that means the blank
        # tile is on the last row and cannot be moved down, thus an invalid move, otherwise a switch of values will occur
        # which will act as the tile moving down
        elif direction == "down":
            if self.blankTile+3 > 8:
                 print("Error: Invalid move")
                 return "Error: Invalid move"
            else:
                self.puzzle[self.blankTile]= self.puzzle[self.blankTile+3]
                self.puzzle[self.blankTile+3]=0
                self.blankTile = self.blankTile+3
        # if the tile goes left, then it's index decreases by 1 but if index modulo 3 is equal to 0, then that means the blank
        # tile is on the left most column and cannot be moved left, thus an invalid move, otherwise a switch of values will occur
        # which will act as the tile moving left
        elif direction == "left":
            if self.blankTile%3==0:
                print("Error: Invalid move")
                return "Error: Invalid move"
            else:
                self.puzzle[self.blankTile]= self.puzzle[self.blankTile-1]
                self.puzzle[self.blankTile-1]=0
                self.blankTile = self.blankTile-1
        # if the tile goes right, then it's index increases by 1 but if index modulo 3 is equal to 2, then that means the blank
        # tile is on the right most column and cannot be moved right, thus an invalid move, otherwise a switch of values will occur
        # which will act as the tile moving right
        elif direction == "right":
            if self.blankTile%3==2:
                print("Error: Invalid move")
                return "Error: Invalid move"
            else:
                self.puzzle[self.blankTile]= self.puzzle[self.blankTile+1]
                self.puzzle[self.blankTile+1]=0
                self.blankTile = self.blankTile+1
        else:
            print("Error: Invalid command: move " + direction)

    def helperMove(self, direction):
        # if the tile goes up, then it's index decreases by 3 but if it goes below 0, then that means the blank
        # tile is on the first row and cannot be moved up, thus an invalid move, otherwise a switch of values will occur
        # which will act as the tile moving up
        if direction == "up":
            if self.blankTile-3 < 0:
                return "Error: Invalid move"
            else:
                self.puzzle[self.blankTile]= self.puzzle[self.blankTile-3]
                self.puzzle[self.blankTile-3]=0
                self.blankTile = self.blankTile-3
        # if the tile goes down, then it's index increases by 3 but if it goes above 8, then that means the blank
        # tile is on the last row and cannot be moved down, thus an invalid move, otherwise a switch of values will occur
        # which will act as the tile moving down
        elif direction == "down":
            if self.blankTile+3 > 8:
                return "Error: Invalid move"
            else:
                self.puzzle[self.blankTile]= self.puzzle[self.blankTile+3]
                self.puzzle[self.blankTile+3]=0
                self.blankTile = self.blankTile+3
        # if the tile goes left, then it's index decreases by 1 but if index modulo 3 is equal to 0, then that means the blank
        # tile is on the left most column and cannot be moved left, thus an invalid move, otherwise a switch of values will occur
        # which will act as the tile moving left
        elif direction == "left":
            if self.blankTile%3==0:
                return "Error: Invalid move"
            else:
                self.puzzle[self.blankTile]= self.puzzle[self.blankTile-1]
                self.puzzle[self.blankTile-1]=0
                self.blankTile = self.blankTile-1
        # if the tile goes right, then it's index increases by 1 but if index modulo 3 is equal to 2, then that means the blank
        # tile is on the right most column and cannot be moved right, thus an invalid move, otherwise a switch of values will occur
        # which will act as the tile moving right
        elif direction == "right":
            if self.blankTile%3==2:
                return "Error: Invalid move"
            else:
                self.puzzle[self.blankTile]= self.puzzle[self.blankTile+1]
                self.puzzle[self.blankTile+1]=0
                self.blankTile = self.blankTile+1
        else:
            return "Error: Invalid move"

    def moveResult(self, direction):
        referencePuzzle = self.puzzle.copy()
        referenceBlankTile = self.blankTile
        if direction == "up":
            if referenceBlankTile-3 < 0:
                return "Error: Invalid move"
            else:
                referencePuzzle[referenceBlankTile]= referencePuzzle[referenceBlankTile-3]
                referencePuzzle[referenceBlankTile-3]=0
                return referencePuzzle
        elif direction == "down":
            if referenceBlankTile+3 > 8:
                return "Error: Invalid move"
            else:
                referencePuzzle[referenceBlankTile]= referencePuzzle[referenceBlankTile+3]
                referencePuzzle[referenceBlankTile+3]=0
                return referencePuzzle
        elif direction == "left":
            if referenceBlankTile%3==0:
                return "Error: Invalid move"
            else:
                referencePuzzle[referenceBlankTile]= referencePuzzle[referenceBlankTile-1]
                referencePuzzle[referenceBlankTile-1]=0
                return referencePuzzle
        elif direction == "right":
            if referenceBlankTile%3==2:
                return "Error: Invalid move"
            else:
                referencePuzzle[referenceBlankTile]= referencePuzzle[referenceBlankTile+1]
                referencePuzzle[referenceBlankTile+1]=0
                return referencePuzzle
        else:
            return "Error: Invalid move"


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

    # command function where it takes a command string and the required input as an input
    def cmd(self, commandString):
        # if there is a space in the command, then it will split it as the command and its input
        if " " in commandString:
            command, inputs = commandString.split(" ", 1)
        # otherwise, it is just a command and there is no input
        else:
            command = commandString
            inputs = ""
        # determining if the line in the input file is a comment or a command
        if command[0:2] == "//" or command[0:1] == "#":
            print(inputs)
        else:
            # printing the command before doing it
            print("\nCOMMAND:", command, inputs)
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
            elif command == "solve":
                if "maxnodes" in inputs:
                    type = inputs[0:3]
                    parts = inputs.split("=")
                    maxNode = parts[1].strip()
                    self.solve(type, int(maxNode))
                else:
                    self.solve(inputs)
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
                    self.cmd(line)
        except FileNotFoundError:
            print("Error: file name " + filename + " not found")

    # returns the state of the puzzle as the state representation
    def getState(self):
        return self.puzzle

    # checks if two Puzzles are equal
    def equals(self, providedPuzzle):
        return self.puzzle == providedPuzzle.getState()

    # dsf recursion function
    def dsfRecursive(self, startState, goalState, limit, direction, visited, prevNode):
        current = Node(startState, direction)
        current.setPrev(prevNode)
        # if the state that was found is the desired end state, then return the state
        if goalState.equals(startState):
            return current, limit
        # if the maximum number of nodes have been created, then exit and return error
        elif limit == 0:
            return "Error: maxnodes limit", limit
        # current is the Node of the current state we are in and direction is waht the prior state
        # had to move in order to get to current
        # set that the state prior to current was the state
        current = Node(startState, direction)
        current.setPrev(prevNode)
        # if visited.contains(current):
        if current in visited:
            return Node(Puzzle([0,0,0,0,0,0,0,0,0]), "failed"), limit
        else:
            # add that now current has been visited
            visited.append(current)
            # making sure that if the state being checked is from moving the blank tile right,
            # we do not go back to the prior state by moving the blank tile left - will cause infinite loop
            if direction != "right":
                # checking that the direction of the move is possible
                leftArray = current.getState().moveResult("left")
                if not isinstance(leftArray, str):
                    leftPuzzle = Puzzle(leftArray)
                    result = self.dsfRecursive(leftPuzzle, goalState, limit-1, "left", visited, current)
                    if not isinstance(result, str):
                        return result

        # making sure that if the state being checked is from moving the blank tile left,
        # we do not go back to the prior state by moving the blank tile right - will cause infinite loop
        if direction != "left":
        # checking that the direction of the move is possible
            rightArray = current.getState().moveResult("right")
            if not isinstance(rightArray, str):
                rightPuzzle = Puzzle(rightArray)
                result = self.dsfRecursive(rightPuzzle, goalState, limit-1, "right", visited, current)
                if not isinstance(result, str):
                    return result

        # making sure that if the state being checked is from moving the blank tile down,
        # we do not go back to the prior state by moving the blank tile up - will cause infinite loop
        if direction != "down":
            # checking that the direction of the move is possible
            upArray = current.getState().moveResult("up")
            if not isinstance(upArray, str):
                upPuzzle = Puzzle(upArray)
                result = self.dsfRecursive(upPuzzle, goalState, limit-1, "up", visited, current)
                if not isinstance(result, str):
                    return result

        # making sure that if the state being checked is from moving the blank tile up,
        # we do not go back to the prior state by moving the blank tile down - will cause infinite loop
        if direction != "up":
            # checking that the direction of the move is possible
            downArray = current.getState().moveResult("down")
            if not isinstance(downArray, str):
                downPuzzle = Puzzle(downArray)
                result = self.dsfRecursive(downPuzzle, goalState, limit-1, "down", visited, current)
                if not isinstance(result, str):
                    return result
        return Node(Puzzle([0,0,0,0,0,0,0,0,0]), "failed")


    # bsf function
    def bsfSearchHelper(self, goalState, startState, maxNode):
        # a node of the initial state is made and marked as the initial state
        initialNode = Node(startState, "initial")
        finalNode = Node(Puzzle([0,0,0,0,0,0,0,0,0]), "failed")
        nodeCount = 1
        # checks if the state that we were given is equal to the desired goal state
        if goalState.equals(startState):
            return initialNode, nodeCount
        else:
            # frontier is a queue of Nodes
            frontier = deque()
            frontierSize = 0
            # reached is a linked list of Nodes
            reached = deque()
            # reached = linkedList(Node(Puzzle([0,0,0,0,0,0,0,0,0]), "testing"))
            # add the initialNode into the frontier and reached array
            frontier.append(initialNode)
            frontierSize = frontierSize+1
        while frontierSize > 0 and nodeCount <= maxNode:
            # current is the Node that was popped out of the queue
            current = frontier.popleft()
            frontierSize = frontierSize-1

            # out of the four states that are possible, checking the one that is left
            leftArray = current.getState().moveResult("left")
            if not isinstance(leftArray, str):
                leftPuzzle = Puzzle(leftArray)
                leftNode = Node(leftPuzzle, "left")
                nodeCount = nodeCount + 1
                leftNode.setPrev(current)
                if leftNode.getState().equals(goalState):
                    return leftNode, nodeCount
                elif not (leftNode in reached):
                    reached.append(leftNode)
                    frontier.append(leftNode)
                    frontierSize = frontierSize+1

            # out of the four states that are possible, checking the one that is right
            rightArray = current.getState().moveResult("right")
            if not isinstance(rightArray, str):
                rightPuzzle = Puzzle(rightArray)
                rightNode = Node(rightPuzzle, "left")
                nodeCount = nodeCount + 1
                rightNode.setPrev(current)
                if rightNode.getState().equals(goalState):
                    return rightNode, nodeCount
                elif not (rightNode in reached):
                    reached.append(rightNode)
                    frontier.append(rightNode)
                    frontierSize = frontierSize+1

            # out of the four states that are possible, checking up
            upArray = current.getState().moveResult("up")
            if not isinstance(upArray, str):
                upPuzzle = Puzzle(upArray)
                upNode = Node(upPuzzle, "up")
                nodeCount = nodeCount + 1
                upNode.setPrev(current)
                if upNode.getState().equals(goalState):
                    return upNode, nodeCount
                elif not (upNode in reached):
                    reached.append(upNode)
                    frontier.append(upNode)
                    frontierSize = frontierSize+1

            # out of the four states that are possible, checking the one that is down
            downArray = current.getState().moveResult("down")
            if not isinstance(downArray, str):
                downPuzzle = Puzzle(downArray)
                downNode = Node(downPuzzle, "down")
                nodeCount = nodeCount + 1
                downNode.setPrev(current)
                if downNode.getState().equals(goalState):
                    return downNode, nodeCount
                elif not (downNode in reached):
                    reached.append(downNode)
                    frontier.append(downNode)
                    frontierSize = frontierSize+1
        if nodeCount >= maxNode:
            return "Error: maxnodes limit", maxNode
        return finalNode, nodeCount

# solve function that incorporates both bsf and dsf, depending on the input
    def solve(self, type, maxNode = 1000):
        goalState = Puzzle([0,1,2,3,4,5,6,7,8])
        result = Node(Puzzle([0,0,0, 0,0,0, 0,0,0]), "failed")
        nodeCount = 0
        resultStack = deque()
        if type == "bsf":
            result, nodeCount = self.bsfSearchHelper(goalState, self, maxNode)
        elif type == "dsf":
            # making a node for the given puzzle
            selfNode = Node(self, None)
            # creating an empty linked list for the nodes that have been visited
            visited = deque()
            # visited = linkedList(selfNode)
            result, nodeCount = self.dsfRecursive(self, goalState, maxNode, None, visited, None)
            nodeCount = maxNode - nodeCount
        # checks if it is an error due to the maximum number of nodes being reached
        if result=="Error: maxnodes limit":
            print("Error: maxnodes limit", maxNode, "reached")
        # given the last node, go through the prior states that brough it here until the initial state is reached
        # print the moves onto terminal backwards
        else:
            while result.hasPrev():
                move = result.getMove()
                resultStack.append(move)
                result = result.getPrev()
            # nodeCount is the number of nodes that were created
            print("Nodes created during search:", nodeCount)
            # resultStack is the stack of the solution states and therefore the solution length
            print("Solution length:", len(resultStack))
            print("Move sequence:")
            while len(resultStack) > 0:
                moveDone = resultStack.pop()
                print("move", moveDone)

    def heuristic(self, htype):
        if htype == "h1":
            displacedTiles = 0
            for i in range(9):
                if self.puzzle[i] != i and self.puzzle[i] != 0:
                    displacedTiles += 1
            return displacedTiles
        elif htype == "h2":
            totalMoves = 0
            for i in range(9):
                if self.puzzle[i] != 0:
                    upDown = abs(int(self.puzzle[i]/3) - int(i/3))
                    leftRight = abs((self.puzzle[i]%3) - (i%3))
                    totalMoves += upDown
                    totalMoves += leftRight
            return totalMoves

    def Asearch(self, heuristicType, maxNodes=1000):
        # keeping track of the amount of nodes made
        nodeCount = 0
        counter = 0
        # using the heuristic to keep track of cost
        cost = self.heuristic(heuristicType)
        # making a priority queue for the possible states
        possibleStates = []
        # making a queue to keep track of all the visited nodes
        visited = deque()
        # adding the first state into the possibleStates queue
        counter+=1
        possibleStates.append((0,-1,Node(self)))
        # adding one to the amount of nodes creates
        nodeCount =+ 1
        goalState = Puzzle([0,1,2,3,4,5,6,7,8])
        while len(possibleStates) != 0:
            current = heapq.heappop(possibleStates)
            currentCost = current[0]
            currentNode = current[2]
            print(currentNode.getState().printState())
            if currentNode.getState().equals(goalState):
                return currentNode
            # adding state of moving left
            leftArray = currentNode.getState().moveResult("left")
            if not isinstance(leftArray, str):
                leftPuzzle = Puzzle(leftArray)
                cost = leftPuzzle.heuristic(heuristicType)
                leftNode = Node(leftPuzzle)
                leftNode.setPrev(currentNode)
                counter+=1
                index=-1
                i = -1
                for item in possibleStates:
                    i+=1
                    if item[2].getState().equals(leftPuzzle):
                        index = i
                print(index)
                print("left puzzle:", leftPuzzle.getState(), currentCost)
                if index != -1:
                    if possibleStates[index][0] > cost+currentCost:
                        possibleStates[index][0] = cost+currentCost
                        possibleStates[index][2] = leftNode
                else:
                    possibleStates.append((cost+1, 1, leftNode))
                heapq.heapify(possibleStates)
            # adding state of moving right
            rightArray = currentNode.getState().moveResult("right")
            # print("right array:",rightArray)
            if not isinstance(rightArray, str):
                rightPuzzle = Puzzle(rightArray)
                cost = rightPuzzle.heuristic(heuristicType)
                rightNode = Node(rightPuzzle)
                rightNode.setPrev(currentNode)
                counter+=1
                index = -1
                i = -1
                for item in possibleStates:
                    i+=1
                    if item[2].getState().equals(rightPuzzle):
                        index = i
                # print(index)
                # print("right puzzle:", rightPuzzle.getState(), currentCost)
                if index != -1:
                    if possibleStates[index][0] > cost+currentCost:
                        possibleStates[index][0] = cost+currentCost
                        possibleStates[index][2] = rightNode
                else:
                    possibleStates.append((cost+1, 2, rightNode))
                for item in possibleStates:
                    print(item[0])
                    print(item[1])
                    print(item[2].getState().getState())
                heapq.heapify(possibleStates)
            # adding state of moving up
            # print("up")
            upArray = currentNode.getState().moveResult("up")
            if not isinstance(upArray, str):
                upPuzzle = Puzzle(upArray)
                cost = upPuzzle.heuristic(heuristicType)
                upNode = Node(upPuzzle)
                upNode.setPrev(currentNode)
                counter+=1
                index = -1
                i = -1
                for item in possibleStates:
                    i+=1
                    if item[2].getState().equals(upPuzzle):
                        index = i
                # print(index)
                # print("up puzzle:", upPuzzle.getState(), currentCost)
                if index != -1:
                    if possibleStates[index][0] > cost+currentCost:
                        possibleStates[index][0] = cost+currentCost
                        possibleStates[index][2] = upNode
                else:
                    possibleStates.append((cost+1, 3, upNode))
                heapq.heapify(possibleStates)
            # adding state of moving down
            downArray = currentNode.getState().moveResult("down")
            if not isinstance(downArray, str):
                downPuzzle = Puzzle(downArray)
                # upPuzzle.printState()
                cost = downPuzzle.heuristic(heuristicType)
                downNode = Node(downPuzzle)
                downNode.setPrev(currentNode)
                counter+=1
                index = -1
                i = -1
                for item in possibleStates:
                    i+=1
                    if item[2].getState().equals(downPuzzle):
                        index = i
                print(index)
                print("right puzzle:", downPuzzle.getState(), currentCost)
                if index != -1:
                    if possibleStates[index][0] > cost+currentCost:
                        possibleStates[index][0] = cost+currentCost
                        possibleStates[index][2] = downNode
                else:
                    possibleStates.append((cost+1, 4, downNode))
                heapq.heapify(possibleStates)


class Node:

    # constructor that sets the currentState to the provided Node and everything else as none
    def __init__(self, givenState, move="none"):
        self.currentState = givenState
        self.nextNode = None
        self.previousNode = None
        self.moveDone = move

    # function that sets the current state as given state
    def setState(self, givenState):
        self.currentState = givenState

    # function that sets the previous state as given state
    def setPrev(self, givenState):
        self.previousNode = givenState

    # function that sets the next state as given state
    def setNext(self, givenState):
        self.nextNode = givenState

    # function that sets the next move as given move
    def setMove(self, move):
        self.moveDone = move

    def setCost(self, cost):
        self.cost = cost

    # function that returns the state
    def getState(self):
        return  self.currentState

    # function that returns the previous state
    def getPrev(self):
        return self.previousNode

    # function that returns the next state
    def getNext(self):
        return self.nextNode

    def getMove(self):
        return self.moveDone

    def getCost(self):
        return self.cost

    # function that returns whether or not the Node has next
    def hasNext(self):
        return self.nextNode != None

    # function that returns whether or not the Node has next
    def hasPrev(self):
        return self.previousNode != None

    def equals(self, otherNode):
        return self.getState().equals(otherNode.getState())

class linkedList:

    # initializing it with the first node
    def __init__(self, firstNode):
        self.first = firstNode
        self.first.setMove(-1)
        self.size = 1

    # adding into the linked list with the first node
    def add(self, addedNode):
        current = self.first
        while (current.hasNext()):
            current = current.getNext()
        current.setNext(addedNode)
        self.size = self.size + 1
    # checks if a specific node is within the linked list
    def contains(self, givenNode):
        current = self.first
        while (current.hasNext()):
            current = current.getNext()
            if current.getState().equals(givenNode.getState()):
                return True
        return False

# main function that takes it so that the file name can be given in the terminal
# checks to make sure that there are two arguments in the terminal before calling on the second
# input of the terminal which is the command file
def main():
    if len(sys.argv) > 1:
        commandFile = sys.argv[1]
        testing = Puzzle([0,0,0,0,0,0,0,0,0])
        testing.cmdfile(commandFile)

if __name__ == "__main__":
    main()

# testing1 = Puzzle([0,1,2,3,4,5,6,7,8])
# testing1.move("down")
# testing1.move("down")
# testing1.move("right")
# testing1.printState()
# # testing1.scrambleState(20)
# testing1.solve("dsf")
# testing2 = Puzzle([4,3,2,1,0,5,6,7,8])
# testing2.move("left")
# testing2.move("up")
# testing2.move("left")
# testing2.move("down")
# testing2.move("left")
# testing2.move("up")
# testing2.printState()

# testing1.printState()
# print(testing1.Asearch("h2").getState().getState())
# testing2 = Puzzle([3,1,2,6,4,5,7,0,8])
# testing2.heuristic("h2")
#
# testing3 = Puzzle([3,1,2,6,4,5,7,0,8])
# testing2.heuristic("h2")