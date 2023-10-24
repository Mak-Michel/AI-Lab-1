from copy import copy
from SearchAlgorithm import SearchAlgorithm
import heapq
from State import State
import StateHeuristics


class AstarSearch(SearchAlgorithm):

    def __init__(self, heuristicFunc):
        self.__heuristicFunc = heuristicFunc


    def execute(self, initialState: State):
        self.__heuristicFunc(initialState)
        
        frontier = []
        self.nodesExpanded = set() 
        frontierUexplored = set()
        heapq.heappush(frontier, initialState)
        frontierUexplored.add(initialState.value)

        while frontier:
            currState: State = heapq.heappop(frontier)

            if currState.value in self.nodesExpanded:
                continue

            self.nodesExpanded.add(currState.value)
            self.maxDepth = max(self.maxDepth, currState.cost)

            if currState.value == self.goalTest:
                # self.printPath(currState)
                self.goal = currState
                return True
            
            for neighbour in self.findNeighbours(currState):
                if neighbour.value not in frontierUexplored:
                    self.__heuristicFunc(neighbour)
                    heapq.heappush(frontier, neighbour)
                    frontierUexplored.add(neighbour.value)
                    # frontierTable[neighbour.value] = neighbour
                elif neighbour.value not in self.nodesExpanded:
                    # existingNeighbour = frontierTable[neighbour.value]
                    self.__heuristicFunc(neighbour)
                    heapq.heappush(frontier, neighbour)
                    frontierUexplored.add(neighbour.value)
                    #self.parentOf[neighbour] = currState
            
        return False