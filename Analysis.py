from Astar import AstarSearch
from BFS import BreadthFirstSearch
from DFS import DepthFirstSearch
from State import State
from StateHeuristics import *
from generateStates import generate

states = generate()
for state in states:
    bfs = BreadthFirstSearch()
    bfs.execute(State(state, state.index('0')))

    dfs = DepthFirstSearch()
    dfs.execute(State(state, state.index('0')))

    astarManhattan = AstarSearch()
    astarManhattan.execute(State(state, state.index('0')), initialManhattan, ManhattanDistance)

    astarEuclidean = AstarSearch()
    astarEuclidean.execute(State(state, state.index('0')), initialEuclidean, EucildeanDistance)

    # print(list(map(int, list(state))), "\t",
    #       bfs.goal.cost, "\t", dfs.goal.cost, "\t", astarManhattan.goal.cost, "\t", astarEuclidean.goal.cost, "\t",
    #       len(bfs.nodesExpanded), "\t", len(dfs.nodesExpanded), "\t", len(astarManhattan.nodesExpanded), "\t", len(astarEuclidean.nodesExpanded), "\t",
    #       bfs.maxDepth, "\t", dfs.maxDepth, "\t", astarManhattan.maxDepth, "\t", astarEuclidean.maxDepth, "\t",
    #       bfs.runningTime, "\t", dfs.runningTime, "\t", astarManhattan.runningTime, "\t", astarEuclidean.runningTime)

    # print(list(map(int, list(state))), "\t",
    #       len(bfs.nodesExpanded), "\t", len(dfs.nodesExpanded), "\t", len(astarManhattan.nodesExpanded), "\t", len(astarEuclidean.nodesExpanded), "\t",
    #       bfs.maxDepth, "\t", dfs.maxDepth, "\t", astarManhattan.maxDepth, "\t", astarEuclidean.maxDepth, "\t",
    #       bfs.runningTime, "\t", dfs.runningTime, "\t", astarManhattan.runningTime, "\t", astarEuclidean.runningTime)