from collections import deque
from SearchAlgorithm import SearchAlgorithm
from State import State


class DepthFirstSearch(SearchAlgorithm):

    def execute(self, initialState: State):
        # self.parentOf.clear()
        # self.parentOf[initialState] = None
        frontier = deque()
        frontier.append(initialState)
        frontierUexplored = set()
        frontierUexplored.add(initialState.value)

        while frontier:
            currState: State = frontier.pop()
            self.nodesExpanded.add(currState.value)
            self.maxDepth = max(self.maxDepth, currState.cost)
            
            if currState.value == self.goalTest:
                self.goal = currState
                return True
            
            neighbours = self.findNeighbours(currState)
            for neighbour in neighbours:
                if neighbour.value not in frontierUexplored:
                    frontier.append(neighbour)
                    frontierUexplored.add(neighbour.value)
                    neighbour.parent = currState
                    # self.parentOf[neighbour] = currState
        return False