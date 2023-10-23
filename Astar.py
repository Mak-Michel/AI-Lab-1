from copy import copy
from SearchAlgorithm import SearchAlgorithm
import heapq
from State import State


class AstarSearch(SearchAlgorithm):

    def execute(self, initialState: State, initialFunc, heuristicFunc):
        initialFunc(initialState)
        heap: list[State] = []
        heapq.heapify(heap, key=lambda obj: obj.costPlusHeuristic)
        heapq.heappush(heap, initialState)
        explored = set()

        while heap:
            currState = heapq.heappop(heap)
            if currState.value in explored: continue
            if currState.value == self.goalTest:
                self.printPath(currState)
                return True
            neighbours = self.findNeighbours(currState)
            for neighbour in neighbours:
                if neighbour.value not in explored:
                    neighbour.cost = currState.cost + 1
                    neighbour.heuristics = copy(currState.heuristics)
                    heuristicFunc(neighbour, currState.indexOf0)
                    heapq.heappush(heap, neighbour)
                    explored.add(neighbour.value)
                    neighbour.parent = currState
                    #self.parentOf[neighbour] = currState

    def ManhattanDistance(self, state: State, i):
        tile = int(state.value[i])
        #state.Manhattans = [0, 1, 1, 0, 0, 1, 0, 0, 0]
        state.heuristics[tile] = abs(tile // 3 + tile % 3 - i // 3 - i % 3)
        state.heuristic = sum(state.heuristics)
        print(state.heuristics)

    def initialManhattan(self, initialstate: State):
        for i in range(initialstate.indexOf0):
            tile = int(initialstate.value[i])
            initialstate.heuristics[tile] = abs(tile // 3 + tile % 3 - i // 3 - i % 3)
        for i in range(initialstate.indexOf0 + 1, 9):
            tile = int(initialstate.value[i])
            initialstate.heuristics[tile] = abs(tile // 3 + tile % 3 - i // 3 - i % 3)
        initialstate.heuristic = sum(initialstate.heuristics)
        print(initialstate.heuristics)