from State import State
from collections import deque

class AnswerManager:

    def __init__(self, goalState: State, expandedNodes: int, runtime: float):
        currState = goalState
        # If we want to view next state, we pop from the forward stack.
        # If we want to view previous state, we pop from the backward stack.
        # Whenever we pop a state from one stack we put it into the other.
        self.__forwardStack = deque()
        self.__backwardStack = deque()
        # Keep stacking from goal to starting state in the forward stack.
        while(currState.parent != None):
            self.__forwardStack.append(currState)
            currState = currState.parent
        # Keep path length (goal depth).
        self.__pathLength = len(self.__forwardStack)-1
        # Keep current state and initialize it to starting state.
        self.__viewedState : State = self.__forwardStack.pop()
        # Number of expanded nodes.
        self.__expandedNodes : int = expandedNodes
        # Time it took the search to reach the goal.
        self.__runtime : float = runtime

    def nextState(self) -> State:
        # Check if there are any more next states, if not, we're at the goal state.
        if (len(self.__forwardStack) == 0): return None
        # Push current state into backward stack, pop from forward stack and set to current state.
        self.__backwardStack.append(self.__viewedState)
        self.__viewedState = self.__forwardStack.pop()
        return self.__viewedState

    def prevState(self) -> State:
        # Check if there are any previous states, if not, we're at the starting state.
        if (len(self.__backwardStack) == 0): return None
        # Push current state into forward stack, pop from backward stack and set to current state.
        self.__forwardStack.append(self.__viewedState)
        self.__viewedState = self.__backwardStack.pop()
        return self.__viewedState
    
    def currState(self) -> State:
        return self.__viewedState
    
    def pathCost(self) -> int:
        return self.__pathLength
    
    def getExpandedNodes(self) -> int:
        return self.__expandedNodes
    
    def getRuntime(self) -> float:
        return self.__runtime
    
    def printState(self, state : State = None):
        printedState = state if state != None else self.__viewedState
        strList = list(printedState.value)
        strList[strList.index("0")] = " "
        print(" ―――――――")
        for i in range(0, 9, 3):
            print(f"│ {strList[i]} │ {strList[i+1]} │ {strList[i+2]} │")
            print(" ―――――――")
        print()
