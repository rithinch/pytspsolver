from pytspsolver.entities import TSProblem
from pytspsolver.experiments import Experiment
from pytspsolver.solvers import *
from pytspsolver.utilities import create_random_problem, Visualizer

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# Create the problemw
#problem1 = create_random_problem(3)
#problem2 = create_random_problem(4) 
#problem3 = create_random_problem(5)  

problems = [create_random_problem("Problem_"+str(i),i) for i in range(3,12)]

# Initialize Solvers
exhaustive_search = ExhaustiveSearch(time_limit=50)
greedy_search = GreedySearch()

# Create Experiment
experiment = Experiment(problems) 

# Add solvers to use in experiment
experiment.add_solver(exhaustive_search)
experiment.add_solver(greedy_search)

# Run the experiment desired number of times
experiment.run(epoch=1) 
results = experiment.get_results()

# Set up Visualizer with experiment results
visualizer = Visualizer(results)

# Show visualizations
visualizer.plot_n_vs_time(plt)

plt.show()

