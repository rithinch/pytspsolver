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

#problem3.visualize(plt)

symeteric_problems = [create_random_problem("Problem_Sym_"+str(i),i) for i in range(10,20)]
asymeteric_problems = [create_random_problem("Problem_Asym_"+str(i),i, asymeteric=True) for i in range(3,10)]

# Initialize Solvers
exhaustive_search = ExhaustiveSearch(time_limit=50)
#greedy_search = GreedySearch()
genetic_algorithm1 = GeneticAlgorithm(generations=100, mutation_rate=0.05, population_size=100, elite_size=20)
genetic_algorithm2 = GeneticAlgorithm(name="GA2", generations=100, mutation_rate=0.2, population_size=100, elite_size=20)

# Create Experiment
experiment = Experiment()

#experiment.add_problem(problem1)
experiment.add_problems(symeteric_problems)
#experiment.add_problems(asymeteric_problems)

# Add solvers to use in experiment
#experiment.add_solver(exhaustive_search)
#experiment.add_solver(greedy_search)
experiment.add_solver(genetic_algorithm1)
experiment.add_solver(genetic_algorithm2)

# Run the experiment desired number of times
experiment.run(epoch=3) 
results = experiment.get_results()

# Set up Visualizer with experiment results
visualizer = Visualizer(results)

# Show visualizations

#visualizer.plot_n_vs_time(plt, greedy_search._name)
#visualizer.plot_n_vs_time(plt, exhaustive_search._name)

visualizer.plot_n_vs_time_all(plt)
visualizer.plot_time_vs_cost_all(plt, 'Problem_Sym_19')
visualizer.plot_time_vs_cost(plt, genetic_algorithm1._name, 'Problem_Sym_19')
visualizer.plot_solver_vs_cost(plt, 'Problem_Sym_19')
visualizer.plot_problem_vs_cost_all(plt)
