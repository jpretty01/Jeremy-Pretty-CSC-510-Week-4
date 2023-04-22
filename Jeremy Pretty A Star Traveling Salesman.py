# Jeremy Pretty 
# CSC 510 Week 4

# Import required modules from SimpleAI library
from simpleai.search import SearchProblem, astar

# Define the PackageDeliveryProblem class, which inherits from the SearchProblem class
class PackageDeliveryProblem(SearchProblem):
    def __init__(self, initial_state, goal_state):
        super().__init__(initial_state)
        self.goal = goal_state

    # Define the available actions for the agent
    def actions(self, state):
        return ['UP', 'DOWN', 'LEFT', 'RIGHT']

    # Define the result function to update the state based on the chosen action
    def result(self, state, action):
        x, y = state
        if action == 'UP':
            return x, y - 1
        elif action == 'DOWN':
            return x, y + 1
        elif action == 'LEFT':
            return x - 1, y
        else:
            return x + 1, y

    # Define the goal test function to check if the current state is the goal state
    def is_goal(self, state):
        return state == self.goal

    # Define the cost function to calculate the cost of moving from one state to another
    def cost(self, state, action, state2):
        return 1

    # Define the heuristic function to estimate the remaining cost to reach the goal state
    def heuristic(self, state):
        x, y = state
        gx, gy = self.goal
        return abs(x - gx) + abs(y - gy)

# Set the initial state and goal state for the problem
initial_state = (0, 0)
goal_state = (5, 5)

# Instantiate the PackageDeliveryProblem with the initial state and goal state
problem = PackageDeliveryProblem(initial_state, goal_state)

# Solve the problem using the A* search algorithm
result = astar(problem)

# Extract the path (sequence of actions) from the result
path = result.path()

# Print the path to deliver the package
print("Path to deliver the package:")
for step in path:
    print(step)
