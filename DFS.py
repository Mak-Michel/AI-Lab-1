from collections import deque
from SearchAlgorithm import SearchAlgorithm
from State import State


class DepthFirstSearch(SearchAlgorithm):

    def execute(self, initialState: State):
        stack = deque()     # initialize stack that act as frontier
        stack.append(initialState)
        stackUnionExplored = set()  # set will contain states that are explored or in the stack
        stackUnionExplored.add(initialState.value)

        while stack:    # Continue DFS until the frontier is empty
            currState: State = stack.pop()  # pop the current state
            self.nodesExpanded.add(currState.value)             # Add the current state's value to the set of explored nodes
            self.maxDepth = max(self.maxDepth, currState.cost)  # Update the maximum depth reached in the search tree
            if currState.value == self.goalTest:    # if success
                self.goal = currState    # Set the goal state to the current state
                self.printPath(currState)
                return True
            neighbours = self.findNeighbours(currState) # find neighboring states of the current state.
            for neighbour in neighbours:    # iterate over all the neighbour states
                if neighbour.value not in stackUnionExplored:   # Check if the neighbor's table has not been explored before
                    stack.append(neighbour)     # Add the neighbor to the stack
                    stackUnionExplored.add(neighbour.value)
                    neighbour.parent = currState    # Set the parent of the neighbor to the current state for tracking the path
        # If the goal state is not found after exploring all reachable states, return False
        return False