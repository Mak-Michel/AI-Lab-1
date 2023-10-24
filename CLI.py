from State import State
from DFS import DepthFirstSearch
from BFS import BreadthFirstSearch
from Astar import AstarSearch
from answerManager import AnswerManager
from SearchAlgorithm import SearchAlgorithm
import StateHeuristics
import time
import re


class CLI:

    def __init__(self):
        self.__manager = None
        self.__algorithm = None

    def __inputExchange(self, message: str, validator) -> str:
        print()
        while True:
            userInput = input(message)
            if (validator(userInput)):
                return userInput
            print("Invalid input! Try again.")

    def __stateValidator(self, userInput: str) -> bool:
        # Match input to regex pattern
        test = re.search("^(\s*[0-8]\s*){9}$", userInput)
        if test is None: return False
        # Make sure every number is present once
        found = [False]*9
        for character in test.string:
            if (not found[int(character)]): found[int(character)] = True
            else: return False
        return True

    def __4choiceValidator(self, userInput: str):
        test = re.search("^[1-4]{1}$", userInput.replace(" ", ""))
        return test is not None

    def startProgram(self):
        print("\n\n\n\nWELCOME TO THE 8-PUZZLE SOLVER!")
        # Take the starting state from the user
        startStateText = self.__inputExchange("Please enter a starting state...\n", self.__stateValidator)
        initialState = State(startStateText, startStateText.index("0"))
        # Take choice from the user about which algorithm to use
        choice = self.__inputExchange(
            "Pick an algorithm to search for the goal state:\n"
            "1. DFS\n"
            "2. BFS\n"
            "3. A* (using Manhattan distance)\n"
            "4. A* (using Euclidean distance)\n\n"
            "Choose a number: ",
            self.__4choiceValidator)

        match int(choice):
            case 1:
                self.__algorithm = DepthFirstSearch()
            case 2:
                self.__algorithm = BreadthFirstSearch()
            case 3:
                self.__algorithm = AstarSearch(StateHeuristics.initialManhattan , StateHeuristics.ManhattanDistance)
            case 4:
                self.__algorithm = AstarSearch(StateHeuristics.initialEuclidean, StateHeuristics.EucildeanDistance)
        
        start = time.time()
        found = self.__algorithm.execute(initialState)
        end = time.time()
        if found:
            print("Algorithm finished with a solution!\n")
            self.__manager = AnswerManager(self.__algorithm, end-start)
            while True:
                action = self.__inputExchange(
                    "1. Print the whole solution with steps\n"
                    "2. Get solution details\n"
                    "3. Restart program\n"
                    "4. Exit program\n\n"
                    "Choose a number: ", 
                    self.__4choiceValidator)
                match int(action):
                    case 1:
                        self.__manager.printWholeSolution()
                    case 2:
                        print(f"Time taken by the algorithm: {self.__manager.getRuntime()} seconds\n"
                              f"Total number of expanded nodes: {self.__manager.getExpandedNodes()} nodes\n"
                              f"Maximum depth the search reached: {self.__manager.getMaxDepth()}\n"
                              f"Cost of the path to the goal: {self.__manager.pathCost()}\n\n")
                    case 3:
                        return
                    case 4:
                        exit()
        else:
            print("No solution was found!")
            



cli = CLI()
while True:
    cli.startProgram()