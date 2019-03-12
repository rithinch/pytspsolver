# pytspsolver

[![Build Status](https://dev.azure.com/rithinchalumuri/pytspsolver/_apis/build/status/pytspsolver-CI?branchName=master)](https://dev.azure.com/rithinchalumuri/pytspsolver/_build/latest?definitionId=6&branchName=master)

🚚 Easy to use python package for rapid experimentation on the classic travelling salesman problem. Contains implementations of various optimization algorithms, cool visualizers and a plug-in architecture.

## Getting Started - Local Setup

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

problems = [create_random_problem(i) for i in range(3,12)]

experiment = Experiment(problems)

experiment.add_solver(ExhaustiveSearch(time_limit=50))
experiment.add_solver(GreedySearch(time_limit=100))

results = experiment.run(epoch=10) 

visualizer = Visualizer(results)
visualizer.plot_n_vs_time(plt)
plt.show()
 ```
 
 It comes with a plug in architecture, therefore it is very customizable.
 
 ## Additional Examples

A few examples have been implemented using jupyter notebooks; found in the **examples** folder. These notebooks can be accessed by launching jupyter notebook from your current conda environment. 

```bash
> jupyter notebook
```

👉 Make sure you are in the right environment when launching jupyter notebook, otherwise, jupyter notebook kernel will be pointing to a different python version which won't have ```pytspsolver``` package installed.
