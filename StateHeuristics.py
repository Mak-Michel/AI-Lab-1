from State import State

def __pos(index):   return index // 3, index % 3


def __manhattanDistance(currentPos, desiredPos):
    desired_posy, desired_posx = __pos(desiredPos)
    current_posy, current_posx = __pos(currentPos)
    return abs(desired_posx - current_posx) + abs(desired_posy - current_posy)
    

def __ManhattanDistance(state: State, i):
    tile = int(state.value[i])
    #state.Manhattans = [0, 1, 1, 0, 0, 1, 0, 0, 0]
    state.heuristics[tile] = abs(tile // 3 + tile % 3 - i // 3 - i % 3)
    state.heuristic = sum(state.heuristics)
    

def StateManhattenHeuristic(state: State):
    heuristics = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(9):
        if(state.value[i] == '0'): continue
        heuristics[int(state.value[i])] = __manhattanDistance(i, int(state.value[i]))
    state.heuristic = sum(heuristics)

def StateEuclideanHeuristic(state: State):
    #todo
    return