from itertools import permutations
from math import inf as oo
from time import process_time
from .SolverBase import SolverBase

class ExhaustiveSearch(SolverBase):
  
  def __init__(self, name='Exhaustive Search', time_limit=100):
    
    super().__init__(name)

    self._time = time_limit
    
  
  def cost(self, mx, path):
    c = 0
    for a,b in zip([0]+path, path+[0]):
        c += mx[a][b]
    return c

  def run(self, tsp_problem):

    time_limit = self._time

    best_path, best_cost, elapsed, time_cost = self.solve(tsp_problem.get_cities(), time_limit)

    result = {
      'name': self._name,
      'details': tsp_problem.get_details(), 
      'best_path':best_path, 
      'cost':best_cost, 
      'time':elapsed,
      'time_vs_cost':time_cost
      }

    return result

  def solve(self, mx, time_limit):

    n = len(mx)
    city_names = list(range(n))
    best_cost = oo
    best_path = []
    elapsed = 0
    time_cost = []

    t = process_time()

    for path in permutations(city_names[1:]):

      path=list(path)

      c = self.cost(mx, path)
      if c< best_cost:
          best_cost = c
          best_path = [0]+path+[0]
      
      elapsed = process_time() - t

      time_cost.append((elapsed, best_cost))

      if (time_limit > -1) and (elapsed > time_limit):
        break

    return (best_path, best_cost, elapsed, time_cost)





  

  
