from .SolverBase import SolverBase
from time import time
import random

class GeneticAlgorithm(SolverBase):

    def __init__(self, name="Genetic Algorithm", generations=1000, mutation_rate=0.5, population_size=100, elite_size=20):
        super().__init__(name)
        self.__generations = generations
        self.__mutation_rate = mutation_rate
        self.__population_size = population_size
        self.__elite_size = elite_size

    def __calc_fitness(self, mx, path):
        c = 0
        for a,b in zip([0]+path, path+[0]):
            c += mx[a][b]
        return c
    
    def __create_initial_population(self, prob_size):
        
        population = []

        for i in range(self.__population_size):

            pop = random.sample(range(prob_size), prob_size)
            population.append(pop)

        return population
    
    def __get_best(self, mx, population):
        
        best_path = self.__rank_population(mx, population)[0]
        best_cost = self.__calc_fitness(mx, best_path)

        return best_path, best_cost
    
    def __next_generation(self, population):

        return population

    def __rank_population(self, mx, population):
        return sorted(population, key=lambda x: self.__calc_fitness(mx, x), reverse=True)

    def __roulette_wheel_selection(self, mx, population):
        """
        Implementation of roulette wheel selection.
        This implementation selection n pairs of parents, where n = population size // 2
        
        Parameters:
            population (list) - list of solutions.
            mx(2d list) - adjacency matrix repesenting cities
        Returns:
            selectedPop (list) - list of tuples that contain pairs of 'good' parents.
        """

        selectedPop = []

        total_fitness = sum([self.__calc_fitness(mx,sol) for sol in population])

        while len(selectedPop) < (self.__population_size//2):

            pick1 = random.uniform(0,total_fitness)
            pick2 = random.uniform(0,total_fitness)

            curr1 = 0
            curr2 = 0
            
            for sol in population:
                curr1+= self.__calc_fitness(mx,sol)
                if curr1 > pick1:
                    parent1 = sol
                    break

            for sol in population:
                curr2+=self.__calc_fitness(mx,sol)
                if curr2 > pick2:
                    parent2 = sol
                    break

            selectedPop.append((parent1,parent2))


        return selectedPop
   
    def run(self, tsp_problem):

        best_path, best_cost, elapsed, time_cost = self.__solve(tsp_problem.get_cities())

        result = {
        'name': self._name,
        'details': tsp_problem.get_details(), 
        'best_path':best_path, 
        'cost':best_cost, 
        'time':elapsed,
        'time_vs_cost':time_cost
        }

        return result

    def __solve(self, cities_mx):
        
        time_cost = []
        generation = 0

        population = self.__create_initial_population(len(cities_mx))
        
        t = time()

        while generation < self.__generations:
            
            population = self.__next_generation(population)
            generation+=1
            
            best_path, best_cost = self.__get_best(cities_mx, population)
            elapsed = time() - t
            time_cost.append((elapsed, best_cost))

        return best_path, best_cost, elapsed, time_cost

    def __swap_mutation(self,individual):
        
        for swapped in range(len(individual)):

            if(random.random() < self.__mutation_rate):
                swapWith = int(random.random() * len(individual))
                
                city1 = individual[swapped]
                city2 = individual[swapWith]
                
                individual[swapped] = city2
                individual[swapWith] = city1

        return individual

    def __tournament_selection(self, population):
        """
        Function to select some 'good' parents from the population using tournament selection.
        This implementation selection n pairs of parents, where n = population size // 2
        Parameters:
            population (list) - list of solutions.
            popSize (int) - population size.
        Returns:
            selectedPop (list) - list of tuples that contain pairs of 'good' parents.
        """

        selectedPop = []

        #Until fill the selectedPop upto the size we want
        while len(selectedPop) < (self.__population_size//2):

            #Select 4 parents
            player1 = random.choice(population)
            player2 = random.choice(population)
            player3 = random.choice(population)
            player4 = random.choice(population)

            #Pick the winner of player 1 and 2 to be parent1.
            if player1 < player2:
                parent1 = player1
            else:
                parent1 = player2

            #Pick the winner of player 3 and 4 to be parent2.
            if player3 < player4:
                parent2 = player3
            else:
                parent2 = player4

            #Add the tuple (parent1,parent2) to the selected population list.
                
            selectedPop.append([parent1,parent2])

        return selectedPop

