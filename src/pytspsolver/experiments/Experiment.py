class Experiment():

  def __init__(self, problems=[], solvers=[]):
    self._results = {}
    self._problems = problems
    self._solvers = solvers

  def run(self, epoch=5):
    for epoch in range(epoch):
      if epoch not in self._results:
        self._results[epoch] = []
      for problem in self._problems:
        for solver in self._solvers:
          result = solver.run(problem)
          self._results[epoch].append(result)
  


