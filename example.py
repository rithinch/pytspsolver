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
problem3 = create_random_problem("Prob_Sym_40",40)  

#problem3.visualize(plt)

symeteric_problems = [create_random_problem("Problem_Sym_"+str(i),i) for i in range(3,30)]
symeteric_problems.extend([create_random_problem("Problem_Sym_2_"+str(i),i) for i in range(3,130)])
symeteric_problems.extend([create_random_problem("Problem_Sym_3_"+str(i),i) for i in range(3,130)])
symeteric_problems.extend([create_random_problem("Problem_Sym_4_"+str(i),i) for i in range(3,130)])
symeteric_problems.extend([create_random_problem("Problem_Sym_5_"+str(i),i) for i in range(3,130)])
#asymeteric_problems = [create_random_problem("Problem_Asym_"+str(i),i, asymeteric=True) for i in range(3,10)]

# Initialize Solvers
exhaustive_search = ExhaustiveSearch(time_limit=50)
greedy_search = GreedySearch()
genetic_algorithm1 = GeneticAlgorithm(generations=1000, mutation_rate=0.05, population_size=200, elite_size=20, selection_operator='tournament')
genetic_algorithm2 = GeneticAlgorithm(name="GA2", generations=1000, mutation_rate=0.01, population_size=200, elite_size=20, selection_operator='tournament')
genetic_algorithm3 = GeneticAlgorithm(name="GA Roulette", generations=1000, mutation_rate=0.01, population_size=200, elite_size=20, selection_operator='roulette')
# Create Experiment
experiment = Experiment()

experiment.add_problems(symeteric_problems)
#experiment.add_problems(asymeteric_problems)

# Add solvers to use in experiment
#experiment.add_solver(exhaustive_search)
experiment.add_solver(greedy_search)
# experiment.add_solver(genetic_algorithm1)
# experiment.add_solver(genetic_algorithm2)
# experiment.add_solver(genetic_algorithm3)

# Run the experiment desired number of times
experiment.run(epoch=10) 
results = experiment.get_results()

# Set up Visualizer with experiment results
visualizer = Visualizer(results)

# Show visualizations

#visualizer.plot_n_vs_time(plt, greedy_search._name)
#visualizer.plot_n_vs_time(plt, exhaustive_search._name)
# visualizer.n_vs_time_all_table()

visualizer.plot_n_vs_time_all(plt)
# visualizer.plot_time_vs_cost_all(plt, 'Prob_Sym_40')
# visualizer.plot_time_vs_cost(plt, genetic_algorithm2._name, 'Prob_Sym_40')
# visualizer.plot_solver_vs_cost(plt, 'Prob_Sym_40')
# visualizer.plot_problem_vs_cost_all(plt)
