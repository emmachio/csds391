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
                heuristicType = ""
                maxNodes = 1000
                if "h" in inputs:
                    heuristicIndex = inputs.find("h")
                    heuristicType = inputs[heuristicIndex:heuristicIndex+2]
                if "maxnodes" in inputs:
                    maxNodesIndex = inputs.find("maxnodes")
                    maxNodes = inputs[maxNodesIndex+9:]
                type = inputs.split(" ", 1)[0]
                self.solve(type, heuristicType, int(maxNodes))
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
                # creating the Puzzle and Node for the state if the blank is moved left
                leftPuzzle = Puzzle(leftArray)
                leftNode = Node(leftPuzzle, "left")
                # incrementing the number of nodes created
                nodeCount = nodeCount + 1
                leftNode.setPrev(current)
                # if this state is the goalState, then return the node
                if leftNode.getState().equals(goalState):
                    return leftNode, nodeCount
                # if the state has not been reached before, then add it to reached and frontier
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
    def solve(self, type, heuristic = None ,maxNode = 1000):
        goalState = Puzzle([0,1,2,3,4,5,6,7,8])
        result = Node(Puzzle([0,0,0, 0,0,0, 0,0,0]), "failed")
        nodeCount = 0
        resultStack = deque()
        if type == "BSF":
            result, nodeCount = self.bsfSearchHelper(goalState, self, maxNode)
        elif type == "DSF":
            # creating an empty linked list for the nodes that have been visited
            visited = deque()
            # visited = linkedList(selfNode)
            result, nodeCount = self.dsfRecursive(self, goalState, maxNode, None, visited, None)
            nodeCount = maxNode - nodeCount
        elif type == "A*":
            if heuristic == None or heuristic == "":
                result = "heuristic not provided for A* search"
            else:
                result, steps, nodeCount = self.Asearch(heuristic, maxNode)
        # checks if it is an error due to the maximum number of nodes being reached
        if result == "Error: maxnodes limit":
            print("Error: maxnodes limit", maxNode, "reached")
        elif result == "heuristic not provided for A* search":
            print("Error: Heuristic required for A* search and not provided")
        # given the last node, go through the prior states that brough it here until the initial state is reached
        # print the moves onto terminal backwards
        else:
            while result.hasPrev():
                move = result.getMove()
                resultStack.append(move)
                result = result.getPrev()
            # nodeCount is the number of nodes that were created during the solution
            print("Nodes created during search:", nodeCount)
            # resultStack is the stack of the solution states and therefore the solution length
            print("Solution length:", len(resultStack))
            print("Move sequence:")
            while len(resultStack) > 0:
                moveDone = resultStack.pop()
                print("move", moveDone)
        print()

    # heuristic function that gives estimate of how far a state is from goal state by designated algorithms
    def heuristic(self, htype):
        # heuristic function that gives estimate based off of how many tiles are displaced excluding the blank
        if htype == "h1":
            displacedTiles = 0
            for i in range(9):
                if self.puzzle[i] != i and self.puzzle[i] != 0:
                    displacedTiles += 1
            return displacedTiles
        # heuristic function that gives estimate based off of sum of how many moves a tile is away from its
        # target spot of every tile except the blank
        elif htype == "h2":
            totalMoves = 0
            for i in range(9):
                if self.puzzle[i] != 0:
                    # upDown determines the number of vertical moves required
                    upDown = abs(int(self.puzzle[i]/3) - int(i/3))
                    # leftRight determines the number of horizontal moves required
                    leftRight = abs((self.puzzle[i]%3) - (i%3))
                    totalMoves += upDown
                    totalMoves += leftRight
            return totalMoves
        else:
            return 0

    def Asearch(self, heuristicType, maxNodes=1000):
        # keeping track of the amount of nodes made
        nodeCount = 0
        # using the heuristic to keep track of cost
        heuristic = self.heuristic(heuristicType)
        # making a priority queue for the possible states
        possibleStates = []
        # making a queue to keep track of all the visited nodes
        visited = deque()
        # keeping a step variable to keep track of the number of steps for comparison
        steps=0
        # adding the first state into the possibleStates queue
        nodeCount =+ 1
        # creating the first node based off of the first state and adding it to the possibleStates queue
        firstNode = Node(self)
        # priority queue keeps track of: f(n), direction, nodeCount, number of steps, added node
        possibleStates.append((heuristic,-1,nodeCount,steps,firstNode))
        # a goal state puzzle made so that we can determine when we reach the goal state
        goalState = Puzzle([0,1,2,3,4,5,6,7,8])
        # while there are still possible states to check through
        while len(possibleStates) != 0 and nodeCount <= maxNodes:
            # pop out the first one - lowest f(n)
            current = heapq.heappop(possibleStates)
            # taking out the current node and the number of steps
            steps = current[3]
            currentNode = current[4]
            # this is the shortest path to the node so add it to the visited queue for repeated state checking
            visited.append(currentNode.getState().getState())
            # if the node popped out is equal to the goal state then that means that is the shortest path to the goalState
            if currentNode.getState().equals(goalState):
                return currentNode, steps, nodeCount
            # adding state of moving left if it is possible and not an already visited state
            leftArray = currentNode.getState().moveResult("left")
            if (not isinstance(leftArray, str)) and (leftArray not in visited):
                leftPuzzle = Puzzle(leftArray)
                # determining the heuristic of the state
                heuristic = leftPuzzle.heuristic(heuristicType)
                nodeCount = nodeCount+1
                # creating the node based off the state of moving the blank tile left
                leftNode = Node(leftPuzzle, "left")
                leftNode.setPrev(currentNode)
                index=-1
                i = -1
                # checking to see if the state created is already within the possibleStates PQ
                for item in possibleStates:
                    i+=1
                    if item[4].getState().equals(leftPuzzle):
                        index = i
                if index != -1:
                    # if the state is already in the PQ and the cost is less, then replace the value
                    if possibleStates[index][3] > steps+1:
                        possibleStates[index] = (heuristic+steps,possibleStates[index][1],possibleStates[index][2],steps+1,leftNode)
                else:
                    # if the state is not in PQ, add the state into the PQ
                    possibleStates.append((heuristic+steps, 1,nodeCount,steps+1, leftNode))
                # sort the heap so that everything is in order
                heapq.heapify(possibleStates)
            # adding state of moving right if it is possible
            rightArray = currentNode.getState().moveResult("right")
            if (not isinstance(rightArray, str)) and (rightArray not in visited):
                rightPuzzle = Puzzle(rightArray)
                # determining the heuristic of the state
                heuristic = rightPuzzle.heuristic(heuristicType)
                nodeCount = nodeCount+1
                # creating the node based off the state of moving the blank tile right
                rightNode = Node(rightPuzzle, "right")
                rightNode.setPrev(currentNode)
                index = -1
                i = -1
                # checking to see if the state created is already within the possibleStates PQ
                for item in possibleStates:
                    i+=1
                    if item[4].getState().equals(rightPuzzle):
                        index = i
                if index != -1:
                    # if the state is already in the PQ and the cost is less, then replace the value
                    if possibleStates[index][3] > steps+1:
                        possibleStates[index] = (heuristic+steps,possibleStates[index][1],possibleStates[index][2],steps+1,rightNode)
                else:
                    # if the state is not in PQ, add the state into the PQ
                    possibleStates.append((heuristic+steps, 2,nodeCount, steps+1, rightNode))
                # sort the heap so that everything is in order
                heapq.heapify(possibleStates)
            # adding state of moving up if it is possible
            upArray = currentNode.getState().moveResult("up")
            if (not isinstance(upArray, str)) and (upArray not in visited):
                upPuzzle = Puzzle(upArray)
                heuristic = upPuzzle.heuristic(heuristicType)
                nodeCount = nodeCount+1
                # creating the node based off the state of moving the blank tile up
                upNode = Node(upPuzzle, "up")
                upNode.setPrev(currentNode)
                index = -1
                i = -1
                # checking to see if the state created is already within the possibleStates PQ
                for item in possibleStates:
                    i+=1
                    if item[4].getState().equals(upPuzzle):
                        index = i
                if index != -1:
                    # if the state is already in the PQ and the cost is less, then replace the value
                    if possibleStates[index][3] > steps+1:
                        possibleStates[index] = (heuristic+steps,possibleStates[index][1],possibleStates[index][2],steps+1,upNode)
                else:
                    # if the state is not in PQ, add the state into the PQ
                    possibleStates.append((heuristic+steps, 3,nodeCount, steps+1,upNode))
                # sort the heap so that everything is in order
                heapq.heapify(possibleStates)
            # adding state of moving down if it is possible
            downArray = currentNode.getState().moveResult("down")
            if (not isinstance(downArray, str)) and (downArray not in visited):
                downPuzzle = Puzzle(downArray)
                heuristic = downPuzzle.heuristic(heuristicType)
                # creating the node based off the state of moving the blank tile down
                nodeCount = nodeCount+1
                downNode = Node(downPuzzle, "down")
                downNode.setPrev(currentNode)
                index = -1
                i = -1
                # checking to see if the state created is already within the possibleStates PQ
                for item in possibleStates:
                    i+=1
                    if item[4].getState().equals(downPuzzle):
                        index = i
                if index != -1:
                    # if the state is already in the PQ and the cost is less, then replace the value
                    if possibleStates[index][3] > steps+1:
                        possibleStates[index] = (heuristic+steps,possibleStates[index][1],possibleStates[index][2],steps+1,downNode)
                else:
                    # if the state is not in PQ, add the state into the PQ
                    possibleStates.append((heuristic+steps, 4, nodeCount,steps+1,downNode))
                # sort the heap so that everything is in order
                heapq.heapify(possibleStates)
        if nodeCount > maxNodes:
            return "Error: maxnodes limit", 0, maxNodes


class Node:

    # constructor that sets the currentState to the provided Node and everything else as none
    def __init__(self, givenState, move="none", heuristic=0):
        self.currentState = givenState
        self.nextNode = None
        self.previousNode = None
        self.moveDone = move
        self.heuristic = heuristic

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

    def setHeuristic(self, newHeuristic):
        self.heuristic = newHeuristic
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

    def getHeuristic(self):
        return self.heuristic

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

# testing1 = Puzzle([3, 1, 2, 6, 0, 5, 7, 4, 8])
# testing1.solve("A*", "h1")

print("\nHEURISTIC TESTING")
print("testing heuristics in eightPuzzle file because heuristics do not have print function")
testingHeuristics = Puzzle()
print("scrambleState 20 times")
testingHeuristics.scrambleState(20)
print("testing heuristic h1:", testingHeuristics.heuristic("h1"))
print("testing heuristic h2:", testingHeuristics.heuristic("h2"))