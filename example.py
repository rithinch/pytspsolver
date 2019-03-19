from pytspsolver.entities import TSProblem
from pytspsolver.experiments import Experiment
from pytspsolver.solvers import *
from pytspsolver.utilities import create_random_problem, Visualizer

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# Create the problems
#problem1 = create_random_problem("TestProb",3)
#problem2 = create_random_problem(4) 
problem3 = create_random_problem("Prob_Asym_",5, asymeteric=True)  

problem3.visualize(plt)

symeteric_problems = [create_random_problem("Problem_Sym_"+str(i),i) for i in range(3,10)]
asymeteric_problems = [create_random_problem("Problem_Asym_"+str(i),i, asymeteric=True) for i in range(3,10)]
# Initialize Solvers
exhaustive_search = ExhaustiveSearch(time_limit=50)
greedy_search = GreedySearch()

# Create Experiment
experiment = Experiment()

#experiment.add_problem(problem1)
#experiment.add_problems(symeteric_problems)
experiment.add_problems(asymeteric_problems)

# Add solvers to use in experiment
experiment.add_solver(exhaustive_search)
experiment.add_solver(greedy_search)

# Run the experiment desired number of times
experiment.run(epoch=2) 
results = experiment.get_results()

# Set up Visualizer with experiment results
visualizer = Visualizer(results)

# Show visualizations

visualizer.plot_n_vs_time(plt, greedy_search._name)
visualizer.plot_n_vs_time(plt, exhaustive_search._name)

visualizer.plot_n_vs_time_all(plt)
visualizer.plot_time_vs_cost_all(plt, 'Problem_Asym_9')
visualizer.plot_time_vs_cost(plt, exhaustive_search._name, 'Problem_Asym_9')
visualizer.plot_solver_vs_cost(plt, 'Problem_Asym_9')
visualizer.plot_problem_vs_cost_all(plt)
