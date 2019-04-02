class Experiment():

  def __init__(self, problems=None, solvers=None):
    self._results = {}
    self._problems = problems if problems != None else []
    self._solvers = solvers if solvers != None else []
    self.__invalid_solutions = []

  def add_problem(self, problem):
    self._problems.append(problem)

  def add_problems(self, problems):
    self._problems.extend(problems)
    
  def add_solver(self, sovler):
    self._solvers.append(sovler)
  
  def get_problem_names(self):
    return [i.name for i in self._problems]
  
  def get_solver_names(self):
    return [i._name for i in self._solvers]
  
  def get_invalid_solutions(self):
    return self.__invalid_solutions
  
  def has_any_invalid_solutions(self):
    return len(self.__invalid_solutions) > 0
  
  def get_problem_sizes(self):
    
    d = {}

    for problem in self._problems:
      d[problem.name] = problem.size
    
    return d

  def get_results(self):
    return self._results
  

  def verify_path(self, path):
    return len(path) == len(set(path)) + 1

  def run(self, epoch=5):

    self.__invalid_solutions = []

    self._problems = sorted(self._problems, key=lambda x: len(x._cities))

    self._results = {}

    self._results['details'] = {
      'problem_names':self.get_problem_names(),
      'solver_names':self.get_solver_names(),
      'problem_sizes':self.get_problem_sizes()
    }

    temp = {}
    

    for e in range(epoch):

      temp[e] = {}

      for problem in self._problems:

        temp[e][problem.name] = {}

        for solver in self._solvers:

          result = solver.run(problem)

          if self.verify_path(result['best_path']):
            temp[e][problem.name][solver._name] = result
          else:
            self.__invalid_solutions.append(result)
    
    self._results['epochs'] = temp

    return self._results
  


