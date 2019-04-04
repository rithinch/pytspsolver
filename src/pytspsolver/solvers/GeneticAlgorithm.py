from .SolverBase import SolverBase
from time import process_time
import random

class GeneticAlgorithm(SolverBase):

    def __init__(self, name="Genetic Algorithm", generations=500, mutation_rate=0.05, population_size=100, elite_size=20, selection_operator='roulette', crossover_operator='ordered'):
        super().__init__(name)
        self.__generations = generations
        self.__mutation_rate = mutation_rate
        self.__population_size = population_size
        self.__elite_size = elite_size
        self.__crossover = self.__ordered_crossover if crossover_operator == 'ordered' else self.__two_point_crossover
        self.__selection = self.__roulette_wheel_selection if selection_operator == 'roulette' else self.__tournament_selection
        self.__cost_cache = {}

    def __breedPopulation(self, parents):
        
        children = []
        
        for parent1, parent2 in parents:
            child1 = self.__crossover(parent1, parent2)
            child2 = self.__crossover(parent2, parent1)
            children.append(child1)
            children.append(child2)
        
        return children

    def __cost(self, mx, path):
        
        x = tuple(path)
        
        if x in self.__cost_cache:
            return self.__cost_cache[x]
        
        c = 0

        for a,b in zip([0]+path[1:], path[1:]+[0]):
            c += mx[a][b]
        
        self.__cost_cache[x] = c

        return c
    
    def __calc_fitness(self, mx, path):
        return 1/float(self.__cost(mx, path))

    def __create_initial_population(self, prob_size):
        
        population = []

        for i in range(self.__population_size):

            pop = [0] + random.sample(range(1, prob_size), prob_size-1)
            population.append(pop)

        return population
    
    def __get_best(self, mx, population):
        
        best_path = self.__rank_population(mx, population)[0]
        best_cost = self.__cost(mx, best_path)

        return best_path+[0], best_cost
    
    def __mutatePopulation(self, population):

        mutatedPop = []
    
        for ind in range(0, len(population)):
            mutatedInd = self.__swap_mutation(population[ind])
            mutatedPop.append(mutatedInd)

        return mutatedPop

    def __next_generation(self, mx, population):
        popRanked = self.__rank_population(mx, population)
        mating_pool = self.__tournament_selection(mx, popRanked)
        children = self.__breedPopulation(mating_pool)
        newPopulation =  self.__rank_population(mx, children)[:self.__population_size - self.__elite_size]
        nextGeneration = popRanked[:self.__elite_size] + self.__mutatePopulation(newPopulation)
        return nextGeneration


    def __ordered_crossover(self, parent1, parent2):
        """Implements ordered crossover"""

        size = len(parent1)

        # Choose random start/end position for crossover
        child = [-1] * size
        start, end = sorted([random.randrange(1, size, 1) for _ in range(2)])

        # Replicate mum's sequence for alice, dad's sequence for bob
        child_inherited = set()
        for i in range(start, end + 1):
            child[i] = parent1[i]
            child_inherited.add(parent1[i])

        #Fill the remaining position with the other parents' entries
        current_dad_position = 0

        fixed_pos = set(range(start, end + 1))       
        i = 0
        while i < size:
            if i in fixed_pos:
                i += 1
                continue

            test_child = child[i]
            if test_child==-1: #to be filled
                dad_trait = parent2[current_dad_position]
                while dad_trait in child_inherited:
                    current_dad_position += 1
                    dad_trait = parent2[current_dad_position]
                child[i] = dad_trait
                child_inherited.add(dad_trait)
            

            i +=1

        return child

    def __rank_population(self, mx, population):
        return sorted(population, key=lambda x: self.__cost(mx, x))

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

        total_fitness = sum([self.__cost(mx,sol) for sol in population])

        while len(selectedPop) < (self.__population_size):

            pick1 = random.uniform(0,total_fitness)
            pick2 = random.uniform(0,total_fitness)

            curr1 = 0
            curr2 = 0
            
            for sol in population:
                curr1+= self.__cost(mx,sol)
                if curr1 > pick1:
                    parent1 = sol
                    break

            for sol in population:
                curr2+=self.__cost(mx,sol)
                if curr2 > pick2:
                    parent2 = sol
                    break

            selectedPop.append((parent1,parent2))


        return selectedPop
   
    def run(self, tsp_problem, reset_cache=True):

        if reset_cache:
            self.__cost_cache = {}
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
        
        t = process_time()

        while (generation < self.__generations):
            
            population = self.__next_generation(cities_mx, population)
            generation+=1
            
            best_path, best_cost = self.__get_best(cities_mx, population)

            elapsed = process_time() - t
            time_cost.append((elapsed, best_cost))

        return best_path, best_cost, elapsed, time_cost

    def __swap_mutation(self,individual):

        for swapped in range(1,len(individual)):

            if(random.random() < self.__mutation_rate):
                swapWith = random.randint(1,len(individual)-1)
                
                city1 = individual[swapped]
                city2 = individual[swapWith]
                
                individual[swapped] = city2
                individual[swapWith] = city1

        return individual

    def __tournament_selection(self, mx, population):
        """
        Function to select some 'good' parents from the population using tournament selection.
        This implementation selection n pairs of parents, where n = population size
        Parameters:
            population (list) - list of solutions.
            popSize (int) - population size.
        Returns:
            selectedPop (list) - list of tuples that contain pairs of 'good' parents.
        """

        selectedPop = []

        #Until fill the selectedPop upto the size we want
        while len(selectedPop) < (self.__population_size):

            #Select 4 parents
            player1 = random.choice(population)
            player2 = random.choice(population)
            player3 = random.choice(population)
            player4 = random.choice(population)

            #Pick the winner of player 1 and 2 to be parent1.
            if self.__cost(mx, player1) < self.__cost(mx, player2):
                parent1 = player1
            else:
                parent1 = player2

            #Pick the winner of player 3 and 4 to be parent2.
            if self.__cost(mx, player3) < self.__cost(mx, player4):
                parent2 = player3
            else:
                parent2 = player4

            #Add the tuple (parent1,parent2) to the selected population list.
                
            selectedPop.append([parent1,parent2])

        return selectedPop
    
    def __two_point_crossover(self, parent1, parent2):
        start = [parent1[0]]
        child = []
        childP1 = start
        childP2 = []

        geneA = random.randint(1,len(parent1)-1)
        geneB = random.randint(1,len(parent1)-1)
    
        startGene = min(geneA, geneB)
        endGene = max(geneA, geneB)

        for i in range(startGene, endGene):
            childP1.append(parent1[i])
        
        childP2 = [item for item in parent2 if item not in childP1]

        child = childP1 + childP2
        return child

