from collections import deque
from State import State


class SearchAlgorithm:

    def __init__(self):
        self.goalTest = "012345678"
        #self.parentOf = dict()

    def swapAndAppend(self, state: State, index1, index2, neighbours):
        temp = list(state.value)
        temp[index1], temp[index2] = temp[index2], temp[index1]
        newState = State(''.join(temp), index2)
        #temp[9] = str(index2)
        neighbours.append(newState)

    def findNeighbours(self, currState: State):
        neighbours: list[State] = []
        #indexOf0 = int(currState[9])
        indexOf0 = currState.indexOf0
        if indexOf0 % 3 != 0: self.swapAndAppend(currState, indexOf0, indexOf0 - 1, neighbours)
        if indexOf0 % 3 != 2: self.swapAndAppend(currState, indexOf0, indexOf0 + 1, neighbours)
        if indexOf0 < 6: self.swapAndAppend(currState, indexOf0, indexOf0 + 3, neighbours)
        if indexOf0 > 2: self.swapAndAppend(currState, indexOf0, indexOf0 - 3, neighbours)
        return neighbours

    def printState(self, tuple):
        strList = list(tuple[0])
        strList[tuple[1]] = " "
        print(" ―――――――")
        for i in range(0, 9, 3):
            print(f"│ {strList[i]} │ {strList[i+1]} │ {strList[i+2]} │")
            print(" ―――――――")
        print()

    def printPath(self, state: State):
        stackPath = deque()
        stackPath.append((state.value, state.indexOf0))
        #parent = self.parentOf[state]
        currState = state.parent
        while currState is not None:
            stackPath.append((currState.value, currState.indexOf0))
            currState = currState.parent
            #parent = self.parentOf[parent]

        while stackPath:
            self.printState(stackPath.pop())