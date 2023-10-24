from collections import deque
from State import State


class SearchAlgorithm:

    def __init__(self):
        self.goalTest = "012345678"
        self.nodesExpanded = set()
        self.maxDepth = 0
        self.goal: State = None
    
    def swapAndAppend(self, state: State, index1, index2, neighbours):
        temp = list(state.value)
        temp[index1], temp[index2] = temp[index2], temp[index1]
        newState = State(''.join(temp), index2)
        #temp[9] = str(index2)
        neighbours.append(newState)
        newState.parent = state
        newState.cost = state.cost + 1

    def findNeighbours(self, currState: State):
        neighbours: list[State] = []
        #indexOf0 = int(currState[9])
        indexOf0 = currState.indexOf0
        if indexOf0 % 3 != 0: self.swapAndAppend(currState, indexOf0, indexOf0 - 1, neighbours)
        if indexOf0 % 3 != 2: self.swapAndAppend(currState, indexOf0, indexOf0 + 1, neighbours)
        if indexOf0 < 6: self.swapAndAppend(currState, indexOf0, indexOf0 + 3, neighbours)
        if indexOf0 > 2: self.swapAndAppend(currState, indexOf0, indexOf0 - 3, neighbours)
        return neighbours
