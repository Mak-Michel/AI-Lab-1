class State:

    def __init__(self, value="", indexOf0=0, cost=0, parent=None):
        self.value = value                              # the configuration of the state for example "1253450678"
        self.indexOf0 = indexOf0                        # index of the empty tile
        self.cost = cost                                # the depth in the search tree
        self.parent: State = parent                     # pointer to its parent
        self.heuristic = 0                              # heuristic value for a give state
        self.heuristics = [0, 0, 0, 0, 0, 0, 0, 0, 0]   # heuristic value for each tile

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
    # implement this to make the object comparable