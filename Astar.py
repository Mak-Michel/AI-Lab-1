from SearchAlgorithm import SearchAlgorithm
import heapq
from State import State


class AstarSearch(SearchAlgorithm):

    # takes the initial state and two heuristic functions
    def execute(self, initialState: State, initialFunc, heuristicFunc):
        initialFunc(initialState)   # find the heuristic value of initial state
        heap: list[State] = []  # the frontier
        heapq.heappush(heap, initialState)
        exploredUnionHeap = set()      # set will contain states that are explored or in the frontier
        exploredUnionHeap.add(initialState.value)

        while heap:     # explore states as long as the heap is not empty
            currState = heapq.heappop(heap)
            if currState.value in self.nodesExpanded: continue  # if that state was explored before then skip
            self.maxDepth = max(self.maxDepth, currState.cost)  # Update the maximum depth reached in the search tree
            self.nodesExpanded.add(currState.value) # Add the current state's value to the set of explored nodes
            if currState.value == self.goalTest:    # if success
                self.printPath(currState)
                self.goal = currState       # Set the goal state to the current state
                return True
            neighbours = self.findNeighbours(currState) # find the neighbours of the current state
            for neighbour in neighbours:
                if neighbour.value not in exploredUnionHeap:    # if neighbour neither explored nor in the heap
                    heuristicFunc(neighbour, currState.indexOf0)    # find heuristic value of the neighbour
                    heapq.heappush(heap, neighbour)                # push the neighbour to the heap
                    exploredUnionHeap.add(neighbour.value)
                elif neighbour.value not in self.nodesExpanded:     # if neighbour is in frontier but not in explored yet so it may have cost less than the cost of the state already in the frontier
                    heuristicFunc(neighbour, currState.indexOf0)    # find heuristic value of the neighbour
                    heapq.heappush(heap, neighbour)
        # If the goal state is not found after exploring all reachable states, return False
        return False