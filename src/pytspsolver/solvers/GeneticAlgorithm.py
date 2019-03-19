from .SolverBase import SolverBase
from time import time
import random

class GeneticAlgorithm(SolverBase):

    def __init__(self, name, generations=1000, mutation_rate=0.5, population_size=100, elite_size=20):
        super().__init__(name)
        self.__generations = generations
        self.__mutation_rate = mutation_rate
        self.__population_size = population_size
        self.__elite_size = elite_size

    
    def run(self, tsp_problem):

        best_path, best_cost, elapsed, time_cost = self.__solve(tsp_problem.get_cities(), tsp_problem.get_size())

        result = {
        'name': self._name,
        'details': tsp_problem.get_details(), 
        'best_path':best_path, 
        'cost':best_cost, 
        'time':elapsed,
        'time_vs_cost':time_cost
        }

        return result
    
    def __create_initial_population(self, cities_mx, prob_size):
        
        population = []

        for i in range(self.__population_size):

            pop = random.sample(range(prob_size), prob_size)
            population.append(pop)

        return population
    
    def __next_generation(self, population):

        return population
    
    def __get_best(self, population):
        return population

    def __solve(self, cities_mx, prob_size):
        
        time_cost = []
        generation = 0

        population = self.__create_initial_population(cities_mx, prob_size)
        
        t = time()

        while generation < self.__generations:
            population = self.__next_generation(population)
            generation+=1
            
            best_path, best_cost = self.__get_best(population)
            elapsed = time() - t
            time_cost.append((elapsed, best_cost))

        return best_path, best_cost, elapsed, time_cost

    

