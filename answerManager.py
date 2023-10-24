from State import State
from collections import deque

class AnswerManager:

    def __init__(self, goalState: State, expandedNodes: int = -1, runtime: float = -1):
        currState = goalState
        # If we want to view next state, we pop from the forward stack.
        # If we want to view previous state, we pop from the backward stack.
        # Whenever we pop a state from one stack we put it into the other.
        self.__forwardStack = deque()
        self.__backwardStack = deque()
        # Keep stacking from goal to starting state in the forward stack.
        if (goalState is not None):
            while(currState.parent is not None):
                self.__forwardStack.append(currState)
                currState = currState.parent
        # Keep path length (goal depth).
        self.__pathLength = len(self.__forwardStack)-1
        # Keep current state and initialize it to starting state.
        self.__viewedState : State = self.__forwardStack.pop() if goalState is not None else None
        # Number of expanded nodes.
        self.__expandedNodes : int = expandedNodes if goalState is not None else -1
        # Time it took the search to reach the goal.
        self.__runtime : float = runtime if goalState is not None else -1

    def nextState(self) -> State:
        """
        Moves the current state inside the object to the next state.\n
        Returns the new current state which was advanced to.
        """
        # Check if there are any more next states, if not, we're at the goal state.
        if (len(self.__forwardStack) == 0): return None
        # Push current state into backward stack, pop from forward stack and set to current state.
        self.__backwardStack.append(self.__viewedState)
        self.__viewedState = self.__forwardStack.pop()
        return self.__viewedState

    def prevState(self) -> State:
        """
        Moves the current state inside the object to the previous state.\n
        Returns the new current state which was reverted to.
        """
        # Check if there are any previous states, if not, we're at the starting state.
        if (len(self.__backwardStack) == 0): return None
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
    
    def hasAnswer(self) -> bool:
        """
        Returns whether a solution was reached or not.
        """
        return self.__viewedState is not None
    
    def printState(self, state : State = None):
        """
        Prints the state passed to it, \n
        and prints the current state if no argument is passed, \n
        and prints an error message if no solution was found.
        """
        printedState = state if state != None else self.__viewedState
        if (printedState is None):
            print("No solution was found!")
        strList = list(printedState.value)
        strList[strList.index("0")] = " "
        print(" ―――――――")
        for i in range(0, 9, 3):
            print(f"│ {strList[i]} │ {strList[i+1]} │ {strList[i+2]} │")
            print(" ―――――――")
        print()