from collections import deque


class SearchAlgorithm:

    def __init__(self):
        self.goalTest = "0123456780"
        self.parentOf = dict()

    def swapAndAppend(self, currState: str, index1, index2, neighbours):
        temp = list(currState)
        temp[index1], temp[index2] = temp[index2], temp[index1]
        temp[9] = str(index2)
        neighbours.append(''.join(temp))
        # self.parentOf[neighbours[-1]] = currState

    def findNeighbours(self, currState: str):
        neighbours = []
        indexOf0 = int(currState[9])
        if indexOf0 % 3 != 0: self.swapAndAppend(currState, indexOf0, indexOf0 - 1, neighbours)
        if indexOf0 % 3 != 2: self.swapAndAppend(currState, indexOf0, indexOf0 + 1, neighbours)
        if indexOf0 < 6: self.swapAndAppend(currState, indexOf0, indexOf0 + 3, neighbours)
        if indexOf0 > 2: self.swapAndAppend(currState, indexOf0, indexOf0 - 3, neighbours)
        return neighbours

    def printState(self, state: str):
        strList = list(state)
        strList[int(strList[9])] = " "
        print(" ―――――――")
        for i in range(0, 9, 3):
            print(f"│ {strList[i]} │ {strList[i+1]} │ {strList[i+2]} │")
            print(" ―――――――")
        print()

    def printPath(self, state: str):
        stackPath = deque()
        stackPath.append(state)
        parent = self.parentOf[state]
        while parent is not None:
            stackPath.append(parent)
            parent = self.parentOf[parent]

        while stackPath:
            self.printState(stackPath.pop())