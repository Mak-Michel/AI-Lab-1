class State:

    def __init__(self, value="", indexOf0=0):
        self.value = value
        self.parent: State = None
        self.cost = 0
        self.depth = 0
        self.heuristic = 0

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)