from collections import deque
from SearchAlgorithm import SearchAlgorithm

class DepthFirstSearch(SearchAlgorithm):

    def execute(self, initialState: str):
        stack = deque()
        stack.append(initialState)
        stackUnionExplored = set()
        stackUnionExplored.add(initialState)

        while stack:
            currState = stack.pop()
            if currState == self.goalTest: return True
            for neighbour in self.findNeighbours(currState):
                if neighbour not in stackUnionExplored:
                    stack.append(neighbour)
                    stackUnionExplored.add(neighbour)
        return False