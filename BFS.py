from queue import Queue
from SearchAlgorithm import SearchAlgorithm
from State import State


class BreadthFirstSearch(SearchAlgorithm):

    def execute(self, initialState: State):
        queue = Queue()
        queue.put(initialState)
        queueUnionExplored = set()
        queueUnionExplored.add(initialState.value)

        while not queue.empty():
            currState: State = queue.get()
            self.maxDepth = max(self.maxDepth, currState.cost)
            self.nodesExpanded.add(currState.value)
            if currState.value == self.goalTest:
                self.goal = currState
                self.printPath(currState)
                return True
            neighbours = self.findNeighbours(currState)
            for neighbour in neighbours:
                if neighbour.value not in queueUnionExplored:
                    queue.put(neighbour)
                    queueUnionExplored.add(neighbour.value)
                    neighbour.parent = currState
        return False