from State import State
from collections import deque
from SearchAlgorithm import SearchAlgorithm

class AnswerManager:

    def __init__(self, algorithm: SearchAlgorithm, runtime: float = -1):
        currState = algorithm.goal
        # If we want to view next state, we pop from the forward stack.
        # If we want to view previous state, we pop from the backward stack.
        # Whenever we pop a state from one stack we put it into the other.
        self.__forwardStack = deque()
        self.__backwardStack = deque()
        # Default instance variable values
        self.__viewedState = None
        self.__expandedNodes = -1
        self.__runtime = -1
        self.__maxDepth = -1
        self.__pathLength = -1
        # Keep stacking from goal to starting state in the forward stack.
        if algorithm.goal is not None:
            while currState is not None:
                self.__forwardStack.append(currState)
                currState = currState.parent
            # Keep current state and initialize it to starting state.
            self.__viewedState : State = self.__forwardStack.pop()
            # Number of expanded nodes.
            self.__expandedNodes : int = len(algorithm.nodesExpanded)
            # Time it took the search to reach the goal.
            self.__runtime : float = runtime
            # Max depth the search reached until it reached the goal.
            self.__maxDepth : int = algorithm.maxDepth
            # Keep path length (goal depth).    
            self.__pathLength = len(self.__forwardStack)-1
    
    def hasAnswer(self) -> bool:
        """
        Returns whether a solution was reached or not.
        """
        return self.__viewedState is not None

    def nextState(self) -> State:
        """
        Moves the current state inside the object to the next state.\n
        Returns the new current state which was advanced to as a list.
        """
        # Check if there are any more next states, if not, we're at the goal state.
        if not self.__forwardStack: return None
        # Push current state into backward stack, pop from forward stack and set to current state.
        self.__backwardStack.append(self.__viewedState)
        self.__viewedState = self.__forwardStack.pop()
        return self.__viewedState

    def prevState(self) -> State:
        """
        Moves the current state inside the object to the previous state.\n
        Returns the new current state which was reverted to as a list.
        """
        # Check if there are any previous states, if not, we're at the starting state.
        if not self.__backwardStack: return None
        # Push current state into forward stack, pop from backward stack and set to current state.
        self.__forwardStack.append(self.__viewedState)
        self.__viewedState = self.__backwardStack.pop()
        return self.__viewedState
    
    def currState(self) -> State:
        """
        Retrieves the current state we're viewing. \n
        Returns: Starting state (after initialization), current state (after using next or previous state), null (if no answer was found).
        """
        return self.__viewedState
    
    def currStateList(self) -> list[int]:
        """
        Returns the current state as a list of integers
        """
        if self.__viewedState is None: return None
        stateList : list[int] = []
        for element in list(self.__viewedState.value):
            stateList.append(int(element))
        return stateList
    
    def printState(self, state : State = None):
        """
        Prints the state passed to it, \n
        and prints the current state if no argument is passed, \n
        and prints an error message if no solution was found.
        """
        printedState = state if state != None else self.__viewedState
        if printedState is None:
            print("No solution was found!")
        strList = list(printedState.value)
        strList[strList.index("0")] = " "
        print(" ―――――――")
        for i in range(0, 9, 3):
            print(f"│ {strList[i]} │ {strList[i+1]} │ {strList[i+2]} │")
            print(" ―――――――")
        print()
    
    def printWholeSolution(self) -> None:
        if self.__viewedState is None:
            print("No solution was found.")
            return
        while self.__backwardStack: self.prevState()
        print("\nSolution steps:\n")
        self.printState()
        while self.__forwardStack:
            self.nextState()
            self.printState()
        # Revert to beginning state
        while self.__backwardStack: self.prevState()

    def pathCost(self) -> int:
        """
        Returns the total cost/length of the path from start to goal, \n
        and -1 if there was no answer.
        """
        return self.__pathLength
    
    def getExpandedNodes(self) -> int:
        """
        Returns number of nodes expanded until a solution was reached, \n
        and -1 if no solution was reached.
        """
        return self.__expandedNodes
    
    def getRuntime(self) -> float:
        """
        Returns time taken by algorithm until a solution was reached, \n
        and -1 if no solution was reached.
        """
        return self.__runtime
    
    def getMaxDepth(self) -> int:
        """
        Returns the max depth that was reached by the algorithm until a solution was reached, \n
        and -1 if no solution was reached.
        """
        return self.__maxDepth
    
