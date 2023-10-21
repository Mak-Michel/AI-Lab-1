from BFS import BreadthFirstSearch
from DFS import DepthFirstSearch

def readInput():
    print("enter initial state")
    strInput = ""
    for i in range(3): strInput += input()
    initialState = strInput.replace(" ", "")
    initialState += str(initialState.find('0'))
    return initialState

if __name__ == '__main__':
    initialState = readInput()
    dfs = DepthFirstSearch()
    print(dfs.execute(initialState))
    bfs = BreadthFirstSearch()
    print(bfs.execute(initialState))