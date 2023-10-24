from collections import deque
from SearchAlgorithm import SearchAlgorithm
from State import State


class DepthFirstSearch(SearchAlgorithm):

    def execute(self, initialState: State):
        stack = deque()
        stack.append(initialState)
        stackUnionExplored = set()
        stackUnionExplored.add(initialState.value)

        while stack:
            currState: State = stack.pop()
            self.nodesExpanded.add(currState.value)
            self.maxDepth = max(self.maxDepth, currState.cost)
            if currState.value == self.goalTest:
                self.goal = currState
                self.printPath(currState)
                print(currState.cost)
                return True
            neighbours = self.findNeighbours(currState)
            for neighbour in neighbours:
                if neighbour.value not in stackUnionExplored:
                    stack.append(neighbour)
                    stackUnionExplored.add(neighbour.value)
                    neighbour.parent = currState

        return False