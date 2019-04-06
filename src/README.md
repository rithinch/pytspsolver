# pytspsolver

Easy to use package for rapid experimentation on the classic travelling salesman problem. Contains implementations of various optimization algorithms, cool visualizers and a plug-in architecture.

[![Build Status](https://dev.azure.com/rithinchalumuri/pytspsolver/_apis/build/status/pytspsolver-CI?branchName=master)](https://dev.azure.com/rithinchalumuri/pytspsolver/_build/latest?definitionId=7&branchName=master) 
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/rithinch)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)]()

## Installation

```bash
> pip install pytspsolver
```

 ## Usage
 
 This package is designed to provide an intutive pythonic interface; allowing you to conduct experiments with minimal code and maximum flexibility. 😅
 
 Here's how you can kick-start a travelling salesman problem experiment:
 
 ```python
from pytspsolver.entities import TSProblem
from pytspsolver.experiments import Experiment
from pytspsolver.solvers import *
from pytspsolver.utilities import create_random_problem, get_tsp_lib_problem, Visualizer
import matplotlib.pyplot as plt

# Create a few tsp problems (represented as an adjacency matrix)
problems = [create_random_problem("UniqueProblemName"+str(i), i) for i in range(3,12)]

# Pass in the location of TSPLIB95 dataset file
tsp_prob = get_tsp_lib_problem("gr17.tsp")

# Create a new Experiment
experiment = Experiment()

# Add the problems to the experiment (single or list of problems)
experiment.add_problem(tsp_prob)
experiment.add_problems(problems)

# Add solvers to use in the experiment
experiment.add_solver(ExhaustiveSearch(time_limit=50))
experiment.add_solver(GreedySearch(time_limit=100))

# Run the experiment desired number of times
results = experiment.run(epoch=10) 

# Set up Visualizer with experiment results
visualizer = Visualizer(results)

# Show visualizations - automatically averages the results from different epochs
visualizer.plot_n_vs_time_all(plt)

# Note: the visualizer has various plots available, they can be called in a similar fashion.
 ```
 
 It comes with a plug in architecture, therefore it is very customizable.

 ## Additional Examples

A few examples have been implemented using jupyter notebooks; found in the **examples** folder. These notebooks can be accessed by launching jupyter notebook from your current conda environment. 

```bash
> jupyter notebook
```

👉 Make sure you are in the right environment when launching jupyter notebook, otherwise, jupyter notebook kernel will be pointing to a different python version which won't have ```pytspsolver``` package installed.

##  Contributions

Contributions and pull requests are encouraged! 👏

If you spot any issues or would like to add a new feature, please discuss it in the GitHub issues section prior to writing code and submitting a pull request.

## Contributors

* [Venkata Rithin Chalumuri](https://github.com/rithinch)
* [Genaro Bedenko](https://github.coventry.ac.uk/bedenkog)
* [Ovidiu Mitroi](https://github.coventry.ac.uk/mitroio)
* [Rishi Mehangra](https://github.coventry.ac.uk/mehangrr)


