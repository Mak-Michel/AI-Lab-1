from queue import Queue
from SearchAlgorithm import SearchAlgorithm
from State import State


class BreadthFirstSearch(SearchAlgorithm):
    def execute(self, initialState: State):
        # Initialize a queue to store states and act as frontier.
        queue = Queue()
        queue.put(initialState)

        # Create a set to keep track of explored states and those in the frontier
        queueUnionExplored = set()
        queueUnionExplored.add(initialState.value)

        # Continue BFS until the frontier is empty.
        while not queue.empty():
            currState: State = queue.get()

            # Update the maximum depth reached in the search tree.
            self.maxDepth = max(self.maxDepth, currState.cost)

            # Add the current state's value to the set of explored nodes.
            self.nodesExpanded.add(currState.value)

            # Check if the current state is the goal state.
            if currState.value == self.goalTest:
                # Set the goal state to the current state.
                self.goal = currState
                self.printPath(currState)
                return True

            # If the current state is not the goal find neighboring states of the current state.
            neighbours = self.findNeighbours(currState)

            for neighbour in neighbours:
                # Check if the neighbor's table has not been explored before.
                if neighbour.value not in queueUnionExplored:
                    # Add the neighbor to the frontier.
                    queue.put(neighbour)
                    queueUnionExplored.add(neighbour.value)
                    # Set the parent of the neighbor to the current state for tracking the path.
                    neighbour.parent = currState

        # If the goal state is not found after exploring all reachable states, return False.
        return False