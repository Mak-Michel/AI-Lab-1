from BFS import BreadthFirstSearch
from DFS import DepthFirstSearch
from State import State
from Astar import AstarSearch


def processInput():
    print("enter initial state")
    strInput = ""
    for i in range(3): strInput += input()
    value = strInput.replace(" ", "")
    indexOf0 = value.find('0')
    return value, indexOf0

if __name__ == '__main__':
    value, indexOf0 = processInput()
    initialState = State(value, indexOf0)
    astar = AstarSearch()
    print(astar.execute(initialState, astar.initialManhattan, astar.ManhattanDistance))
    # dfs = DepthFirstSearch()
    # print(dfs.execute(initialState))
    # bfs = BreadthFirstSearch()
    # print(bfs.execute(initialState))
    # d = AstarSearch()
    # d.initialManhattan(State("125340678", 5))
    # d.ManhattanDistance(State("120345678", 2), 5)