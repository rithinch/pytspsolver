class Experiment():

  def __init__(self, problems=[], solvers=[]):
    self._results = {}
    self._problems = problems
    self._solvers = solvers

  def add_problem(self, problem):
    self._problems.append(problem)
    
  def add_solver(self, sovler):
    self._solvers.append(sovler)
  
  def get_problem_names(self):
    return [i.name for i in self._problems]
  
  def get_solver_names(self):
    return [i._name for i in self._solvers]

  def get_results(self):
    return self._results

  def run(self, epoch=5):

    self._results = {}

    for epoch in range(epoch):

      if epoch not in self._results:

        self._results[epoch] = {}

      for problem in self._problems:

        if problem.name not in self._results[epoch]:

          self._results[epoch][problem.name] = {}

        for solver in self._solvers:

          result = solver.run(problem)

          self._results[epoch][problem.name][solver._name] = result
    
    return self._results
  


