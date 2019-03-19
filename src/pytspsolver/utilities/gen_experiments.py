from random import randint
from pytspsolver.entities import TSProblem

def create_random_problem(name, size, low=1, high=100):
    
    dist_matrix = [[0 for _ in range(size)] for _ in range(size)]
    
    for i in range(size):
        
        for j in range(i+1,size):
            v = randint(low,high)
            dist_matrix[i][j] = v
            dist_matrix[j][i] = v
            
    return TSProblem(name, dist_matrix)