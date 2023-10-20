from BFS import BreadthFirstSearch
from DFS import DepthFirstSearch

if __name__ == '__main__':
    dfs = DepthFirstSearch()
    print(dfs.execute("1253406785"))

    bfs = BreadthFirstSearch()
    print(bfs.execute("1253406785"))