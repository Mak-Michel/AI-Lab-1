from collections import deque
from State import State


class SearchAlgorithm:

    def __init__(self):
        self.goalTest = "012345678"
        self.maxDepth = 0
        self.nodesExpanded = set()  # will store all explored nodes
        self.goal: State = None     # will store the final State object of the goal test

    def swapAndAppend(self, state: State, index1, index2, neighbours):
        temp = list(state.value)
        temp[index1], temp[index2] = temp[index2], temp[index1]     # swap the tile with the empty tile
        newState = State(''.join(temp), index2, state.cost + 1, state)  # create new state
        neighbours.append(newState)

    def findNeighbours(self, currState: State):
        neighbours: list[State] = []    # list of the neighbours of current State
        indexOf0 = currState.indexOf0   # index of the empty tile
        if indexOf0 % 3 != 0: self.swapAndAppend(currState, indexOf0, indexOf0 - 1, neighbours) # move left
        if indexOf0 % 3 != 2: self.swapAndAppend(currState, indexOf0, indexOf0 + 1, neighbours) # move right
        if indexOf0 > 2: self.swapAndAppend(currState, indexOf0, indexOf0 - 3, neighbours)  # move up
        if indexOf0 < 6: self.swapAndAppend(currState, indexOf0, indexOf0 + 3, neighbours)  # move down
        return neighbours