from collections import deque
from SearchAlgorithm import SearchAlgorithm
from State import State


class DepthFirstSearch(SearchAlgorithm):

    def execute(self, initialState: State):
        # self.parentOf.clear()
        # self.parentOf[initialState] = None
        stack = deque()
        stack.append(initialState)
        stackUnionExplored = set()
        stackUnionExplored.add(initialState.value)

        while stack:
            currState: State = stack.pop()
            if currState.value == self.goalTest:
                self.printPath(currState)
                return True
            neighbours = self.findNeighbours(currState)
            for neighbour in neighbours:
                if neighbour.value not in stackUnionExplored:
                    stack.append(neighbour)
                    stackUnionExplored.add(neighbour.value)
                    neighbour.parent = currState
                    # self.parentOf[neighbour] = currState
        return False