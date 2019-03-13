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

    self._problems = sorted(self._problems, key=lambda x: len(x._cities))

    self._results = {}

    self._results['details'] = {
      'problem_names':self.get_problem_names(),
      'solver_names':self.get_solver_names()
    }

    temp = {}

    for e in range(epoch):

      temp[e] = {}

      for problem in self._problems:

        temp[e][problem.name] = {}

        for solver in self._solvers:

          result = solver.run(problem)

          temp[e][problem.name][solver._name] = result
    
    self._results['epochs'] = temp

    return self._results
  


