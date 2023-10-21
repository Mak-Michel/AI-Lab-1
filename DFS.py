from collections import deque
from SearchAlgorithm import SearchAlgorithm

class DepthFirstSearch(SearchAlgorithm):

    def execute(self, initialState: str):
        self.parentOf.clear()
        self.parentOf[initialState] = None
        stack = deque()
        stack.append(initialState)
        stackUnionExplored = set()
        stackUnionExplored.add(initialState)

        while stack:
            currState = stack.pop()
            if currState == self.goalTest:
                self.printPath(currState)
                return True
            neighbours = self.findNeighbours(currState)
            for neighbour in neighbours:
                if neighbour not in stackUnionExplored:
                    stack.append(neighbour)
                    stackUnionExplored.add(neighbour)
                    self.parentOf[neighbour] = currState
        return False