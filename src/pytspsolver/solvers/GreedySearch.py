from time import process_time
from math import inf as oo
from .SolverBase import SolverBase

class GreedySearch(SolverBase):
  
    def __init__(self, name='Greedy Search', time_limit=100):
        
        super().__init__(name)

        self._time = time_limit

    def run(self, tsp_problem):
        """Function to run Greedy search algorithm for the provided TSP instance
           Returns the path generated from the algorithm, including its cost and time taken"""
        
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
        """Executes the Greedy Search algorithm logic for the provided adjacency matrix"""

        n = len(mx)
        city_names = list(range(n)) # List of cities labelled [1,2,3,..,n]
        elapsed = 0
        time_cost = []

        t = process_time()

        path = [city_names[0]] # Start at city 0

        cost = 0
        
        # Iterate over all cities that need to be visited
        for i in range(n-1):

            possible_next_cities = list(set(city_names) - set(path)) # List of unvisited cities

            current_city = path[-1] # Last city in the current path

            next_city_cost = oo
            next_city = -1

            # Iterate over cities to visit from current city
            for index, city_cost in enumerate(mx[current_city]):

                # If the city is not itself and is unvisited
                if (city_cost != 0) and index in possible_next_cities:
                    
                    # If city cost is less than current best option
                    if city_cost < next_city_cost:

                        # Update next possible city and its cost
                        next_city_cost = city_cost
                        next_city = index

            # Update with resulting next city and cost
            path.append(next_city)
            cost += next_city_cost

            elapsed = process_time() - t # Record time taken
            time_cost.append((elapsed, cost))

        cost+=mx[path[-1]][0] #Add cost to go back
        elapsed = process_time() - t # Record time taken
        time_cost.append((elapsed, cost))
        
        path.append(city_names[0]) # Add starting city to end as well

        

        return (path, cost, elapsed, time_cost)

