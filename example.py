from pytspsolver.entities import TSProblem
from pytspsolver.experiments import Experiment
from pytspsolver.solvers import *
from pytspsolver.utilities import create_random_problem, Visualizer

# Create the problem
problem = create_random_problem(3) 
print(problem)

# Initialize Solvers
exhaustive_search = ExhaustiveSearch(time_limit=50) 

# Create Experiment
experiment = Experiment() 

# Add problems to solve in experiment
experiment.add_problem(problem)

# Add solvers to use in experiment
experiment.add_solver(exhaustive_search)

# Run the experiment desired number of times
experiment.run(epoch=1) 

# Visualize results
visualizer = Visualizer(experiment.get_results())

