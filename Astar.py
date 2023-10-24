from copy import copy
from SearchAlgorithm import SearchAlgorithm
import heapq
from State import State


class AstarSearch(SearchAlgorithm):

    def execute(self, initialState: State, initialFunc, heuristicFunc):
        initialFunc(initialState)
        
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
                    self.initialManhattan(neighbour)
                    heapq.heappush(frontier, neighbour)
                    # frontierTable[neighbour.value] = neighbour
                elif neighbour.value not in self.nodesExpanded:
                    # existingNeighbour = frontierTable[neighbour.value]
                    self.initialManhattan(neighbour)
                    heapq.heappush(frontier, neighbour)
                    #self.parentOf[neighbour] = currState
            
        return False


    def pos(self, index):   return index // 3, index % 3


    def manhattanDistance(self, currentPos, desiredPos):
        desired_posy, desired_posx = self.pos(desiredPos)
        current_posy, current_posx = self.pos(currentPos)
        return abs(desired_posx - current_posx) + abs(desired_posy - current_posy)
        

    def ManhattanDistance(self, state: State, i):
        tile = int(state.value[i])
        #state.Manhattans = [0, 1, 1, 0, 0, 1, 0, 0, 0]
        state.heuristics[tile] = abs(tile // 3 + tile % 3 - i // 3 - i % 3)
        state.heuristic = sum(state.heuristics)
        

    def initialManhattan(self, initialstate: State):
        heuristics = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(9):
            if(initialstate.value[i] == '0'): continue
            heuristics[int(initialstate.value[i])] = self.manhattanDistance(i, int(initialstate.value[i]))
        initialstate.heuristic = sum(heuristics)