from time import time
from math import inf as oo

class GreedySearch():
  
    def __init__(self, time_limit=100):
        self._time = time_limit
        self._name = 'GreedySearch'

    def run(self, tsp_problem, time_limit=None):

        if time_limit == None:
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

    def solve(self, mx, time_limit=50):

        n = len(mx)
        city_names = list(range(n)) # List of cities labelled [1,2,3,..,n]
        elapsed = 0
        time_cost = []

        t = time()

        path = [city_names[0]]

        cost = 0
        
        for i in range(n-1):

            possible_next_cities = list(set(city_names) - set(path)) # List of unvisited cities

            current_city = path[-1] # Last city in the current path

            next_city_cost = oo
            next_city = -1

            for index, city in enumerate(mx[current_city]):

                if (city != 0) and index in possible_next_cities:
                    
                    if city < next_city_cost:
                        next_city_cost = city
                        next_city = index

            path.append(next_city)
            cost += next_city_cost

        path.append(city_names[0])

        elapsed = time() - t

        time_cost.append((elapsed, cost))

        return (path, cost, elapsed, time_cost)

