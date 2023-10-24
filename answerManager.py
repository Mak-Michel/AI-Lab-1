from State import State
from collections import deque

class AnswerManager:

    def __init__(self, goalState: State):
        currState = goalState
        # If we want to view next state, we pop from the forward stack.
        # If we want to view previous state, we pop from the backward stack.
        # Whenever we pop a state from one stack we put it into the other.
        self.forwardStack = deque()
        self.backwardStack = deque()
        # Keep stacking from goal to starting state in the forward stack.
        while(currState.parent != None):
            self.forwardStack.append(currState)
            currState = currState.parent
        # Keep path length (goal depth) and keep track of viewed states.
        self.pathLength = len(self.forwardStack)-1
        self.viewedState : State = self.forwardStack.pop()
        self.backwardStack.append(self.viewedState)

    def nextState(self) -> State:
        # Check if there are any more next states, if not, we're at the goal state.
        if (len(self.forwardStack) == 0): return None
        # Pop from forward stack, set current state, and push into backward stack.
        temp = self.forwardStack.pop()
        self.viewedState = temp
        self.backwardStack.append(temp)

    def prevState(self) -> State:
        # Check if there are any previous states, if not, we're at the starting state.
        if (len(self.backwardStack) == 0): return None
        # Pop from backward stack, set current state, and push into forward stack.
        temp = self.backwardStack.pop()
        self.viewedState = temp
        self.forwardStack.append(temp)
