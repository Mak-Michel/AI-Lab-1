import math
from copy import copy
from SearchAlgorithm import SearchAlgorithm
import heapq
from State import State


class AstarSearch(SearchAlgorithm):

    def execute(self, initialState: State, initialFunc, heuristicFunc):
        initialFunc(initialState)
        heap: list[State] = []
        heapq.heappush(heap, initialState)
        explored = set()
        exploredUnionHeap = set()
        exploredUnionHeap.add(initialState.value)

        while heap:
            currState = heapq.heappop(heap)
            if currState.value in explored: continue
            self.maxDepth = max(self.maxDepth, currState.cost)
            explored.add(currState.value)
            if currState.value == self.goalTest:
                self.printPath(currState)
                self.goal = currState
                return True
            neighbours = self.findNeighbours(currState)
            for neighbour in neighbours:
                if neighbour.value not in exploredUnionHeap:
                    heuristicFunc(neighbour, currState.indexOf0)
                    heapq.heappush(heap, neighbour)
                    exploredUnionHeap.add(neighbour.value)
                elif neighbour.value not in explored:
                    heuristicFunc(neighbour, currState.indexOf0)
                    heapq.heappush(heap, neighbour)
        return False

    def ManhattanDistance(self, state: State, i):
        state.heuristics = copy(state.parent.heuristics)
        tile = int(state.value[i])
        newHeuristic = abs(tile // 3 - i // 3) + abs(tile % 3 - i % 3)
        if newHeuristic < state.heuristics[tile]:
            state.heuristic = state.parent.heuristic - 1
        else:
            state.heuristic = state.parent.heuristic + 1
        state.heuristics[tile] = newHeuristic

    def initialManhattan(self, initialstate: State):
        for i in range(9):
            tile = int(initialstate.value[i])
            if tile != 0:
                initialstate.heuristics[tile] = abs(tile // 3 - i // 3) + abs(tile % 3 - i % 3)
        initialstate.heuristic = sum(initialstate.heuristics)

    def pos(self, index): return index // 3, index % 3

    def initialEuclidean(self, initialState: State):
        for i in range(9):
            tile = int(initialState.value[i])
            if tile != 0:
                if tile != i:
                    tilePosx, tilPosy = self.pos(tile)
                    iPosx, iPosy = self.pos(i)
                    initialState.heuristics[tile] = math.sqrt((tilePosx - iPosx) ** 2 + (tilPosy - iPosy) ** 2)
        initialState.heuristic = sum(initialState.heuristics)

    def EucildeanDistance(self, state: State, i):
        tile = int(state.value[i])
        tilePosx, tilPosy = self.pos(tile)
        iPosx, iPosy = self.pos(i)
        state.heuristics[tile] = math.sqrt((tilePosx - iPosx) ** 2 + (tilPosy - iPosy) ** 2)
        state.heuristic = sum(state.heuristics)