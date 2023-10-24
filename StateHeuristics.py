import math
from copy import copy
from State import State

# finds Manhattan distance for a state by using the Manhattan values of its parent
def ManhattanDistance(self, state: State, i):   # i is index of empty blank in parent state
    state.heuristics = copy(state.parent.heuristics)
    tile = int(state.value[i])
    newHeuristic = abs(tile // 3 - i // 3) + abs(tile % 3 - i % 3)
    if newHeuristic < state.heuristics[tile]:       # if new Manhattan distance of a given tile smaller than Manhattan distance of the same tile in parents state
        state.heuristic = state.parent.heuristic - 1    # update heuristic value of the state
    else:
        state.heuristic = state.parent.heuristic + 1    # update heuristic value of the state
    state.heuristics[tile] = newHeuristic   # update heuristic value of the tile

def initialManhattan(self, initialstate: State):    # Manhattan function finds the heuristic value for the initial state only
    for i in range(9):
        tile = int(initialstate.value[i])
        if tile != 0:   # skip empty blank
            initialstate.heuristics[tile] = abs(tile // 3 - i // 3) + abs(tile % 3 - i % 3) #Manhattan equation
            # tile // 3 is goal.x, tile % 3 is goal.y, i // 3 is currPos.x, i % 3 is currPos.y
    initialstate.heuristic = sum(initialstate.heuristics)   #heuristic value of the state is the sum of the heuristic value for all tiles

def pos(self, index): return index // 3, index % 3  # given index it returns the x,y coordinates

def initialEuclidean(self, initialState: State): # find initial Euclidean distance for the initial state
    for i in range(9):
        tile = int(initialState.value[i])
        if tile != 0:
            if tile != i:   # if tile == its index then skip
                tilePosx, tilPosy = self.pos(tile)  # goal position
                iPosx, iPosy = self.pos(i)          # current position
                initialState.heuristics[tile] = math.sqrt((tilePosx - iPosx) ** 2 + (tilPosy - iPosy) ** 2) # Euclidean equation
    initialState.heuristic = sum(initialState.heuristics)   # heuristic value of the state is the sum of the heuristic value for all tiles

# finds Euclidean distance for a state by using the Euclidean values of its parent
def EucildeanDistance(self, state: State, i):
    state.heuristics = copy(state.parent.heuristics)
    tile = int(state.value[i])
    tilePosx, tilPosy = self.pos(tile)  # goal position
    iPosx, iPosy = self.pos(i)          # current position
    state.heuristics[tile] = math.sqrt((tilePosx - iPosx) ** 2 + (tilPosy - iPosy) ** 2)    # Euclidean equation
    state.heuristic = sum(state.heuristics) # heuristic value of the state is the sum of the heuristic value for all tiles