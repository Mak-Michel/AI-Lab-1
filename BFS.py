from queue import Queue
from SearchAlgorithm import SearchAlgorithm

class BreadthFirstSearch(SearchAlgorithm):

    def execute(self, initialState: str):
        queue = Queue()
        queue.put(initialState)
        queueUnionExplored = set()
        queueUnionExplored.add(initialState)

        while not queue.empty():
            currState = queue.get()
            if currState == self.goalTest: return True
            for neighbour in self.findNeighbours(currState):
                if neighbour not in queueUnionExplored:
                    queue.put(neighbour)
                    queueUnionExplored.add(neighbour)
        return False