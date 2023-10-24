class State:

    def __init__(self, value="", indexOf0=0, cost=0, parent=None):
        self.value = value
        self.indexOf0 = indexOf0
        self.cost = cost
        self.parent: State = parent
        self.heuristic = 0
        self.heuristics = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)