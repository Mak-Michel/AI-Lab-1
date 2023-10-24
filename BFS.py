from queue import Queue
from SearchAlgorithm import SearchAlgorithm
from State import State


class BreadthFirstSearch(SearchAlgorithm):

    def execute(self, initialState: State):
        #self.parentOf.clear()
        #self.parentOf[initialState] = None
        frontier = Queue()
        frontier.put(initialState)
        frontierUexplored = set()
        frontierUexplored.add(initialState.value)

        while not frontier.empty():
            currState: State = frontier.get()
            self.nodesExpanded.add(currState.value)
            self.maxDepth = max(self.maxDepth, currState.cost)

            if currState.value == self.goalTest:
                self.goal = currState
                return True

            neighbours = self.findNeighbours(currState)
            for neighbour in neighbours:
                if neighbour.value not in frontierUexplored:
                    frontier.put(neighbour)
                    frontierUexplored.add(neighbour.value)
                    neighbour.parent = currState
                    #self.parentOf[neighbour] = currState
        return False