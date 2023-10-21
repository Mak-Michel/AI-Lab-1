from queue import Queue
from SearchAlgorithm import SearchAlgorithm

class BreadthFirstSearch(SearchAlgorithm):

    def execute(self, initialState: str):
        self.parentOf.clear()
        self.parentOf[initialState] = None
        queue = Queue()
        queue.put(initialState)
        queueUnionExplored = set()
        queueUnionExplored.add(initialState)

        while not queue.empty():
            currState = queue.get()
            if currState == self.goalTest:
                self.printPath(currState)
                return True
            neighbours = self.findNeighbours(currState)
            for neighbour in neighbours:
                if neighbour not in queueUnionExplored:
                    queue.put(neighbour)
                    queueUnionExplored.add(neighbour)
                    self.parentOf[neighbour] = currState
        return False