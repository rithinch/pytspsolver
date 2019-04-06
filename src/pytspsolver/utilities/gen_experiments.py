from random import randint
from pytspsolver.entities import TSProblem

import tsplib95
import networkx as nx

def create_random_problem(name, size, low=1, high=100, asymeteric=False):
    
    dist_matrix = [[0 for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        
        for j in range(i+1,size):
            v = randint(low,high)
            v2 = v

            if asymeteric:
                    v2 = randint(low, high)

            dist_matrix[i][j] = v
            dist_matrix[j][i] = v2
            
    return TSProblem(name, dist_matrix)
    

def get_tsp_lib_problem(name, folder="datasets", size=-1):

        problem = tsplib95.load_problem(f'{folder}/{name}')

        node_list = list(problem.get_nodes())

        G = problem.get_graph()
        cities_mx = nx.to_numpy_matrix(G, nodelist=node_list).tolist()

        return TSProblem(name, cities_mx)