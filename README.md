# :truck: pytspsolver

Easy to use package for rapid experimentation on the classic travelling salesman problem. Contains implementations of various optimization algorithms, cool visualizers and a plug-in architecture.

[![Build Status](https://dev.azure.com/rithinchalumuri/pytspsolver/_apis/build/status/pytspsolver-CI?branchName=master)](https://dev.azure.com/rithinchalumuri/pytspsolver/_build/latest?definitionId=6&branchName=master) 
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/rithinch)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)


## Installation

```bash
> pip install -i https://test.pypi.org/simple/ pytspsolver
```

##  Local Setup (Development Purposes)

Let's first create a new python environment with the name **your_env_name** using Anaconda Prompt/Terminal; this allows us to manage all package dependencies for this project in isolation. 

```bash
> conda create -n your_env_name
```

We can now activate the created environment using the command below:

```bash
> conda activate your_env_name
```

We need to install a few dependencies. We can do this by running the following:

```bash
> conda install jupyter
> pip install -r ./src/requirements.txt
```

Then, we need to install the ```pytspsolver``` package. Everytime a code change is made to the package, this needs to be called. Otherwise newly added changes wouldn't reflect in places where this package is being used. 

```bash
> pip install ./src
```

 That's it, we're good to start using the package now! 👏
 
 ## Usage
 
 This package is designed to provide an intutive pythonic interface; allowing you to conduct experiments with minimal code. 😅
 
 Here's how you can kick-start a travelling salesman problem experiment:
 
 ```python
from pytspsolver.entities import TSProblem
from pytspsolver.experiments import Experiment
from pytspsolver.solvers import *
from pytspsolver.utilities import create_random_problem, Visualizer
import matplotlib.pyplot as plt

# Create a few tsp problems (represented as an adjacency matrix)
problems = [create_random_problem("UniqueProblemName"+str(i), i) for i in range(3,12)]

# Create a new Experiment
experiment = Experiment()

# Add the problems to the experiment (single or list of problems)
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
