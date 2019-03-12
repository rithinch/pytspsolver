from random import randint
from pytspsolver.entities import TSProblem

def create_random_problem(n):
    
    dist_matrix = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        
        for j in range(i+1,n):
            v = randint(1,100)
            dist_matrix[i][j] = v
            dist_matrix[j][i] = v
            
    return TSProblem(dist_matrix)