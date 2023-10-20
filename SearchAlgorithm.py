class SearchAlgorithm:

    def __init__(self): self.goalTest = "0123456780"

    def swapAndAppend(self, currState: str, index1, index2, neighbours):
        temp = list(currState)
        temp[index1], temp[index2] = temp[index2], temp[index1]
        temp[9] = str(index2)
        neighbours.append(''.join(temp))

    def findNeighbours(self, currState: str):
        neighbours = []
        indexOf0 = int(currState[9])
        if indexOf0 % 3 != 0: self.swapAndAppend(currState, indexOf0, indexOf0 - 1, neighbours)
        if indexOf0 % 3 != 2: self.swapAndAppend(currState, indexOf0, indexOf0 + 1, neighbours)
        if indexOf0 < 6: self.swapAndAppend(currState, indexOf0, indexOf0 + 3, neighbours)
        if indexOf0 > 2: self.swapAndAppend(currState, indexOf0, indexOf0 - 3, neighbours)
        return neighbours