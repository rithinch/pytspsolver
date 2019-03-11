class TSProblem():
  
  def __init__(self, cities_mx=None):

    if cities_mx:
      self._cities = cities_mx
    else:
      self._cities = []

  def print_cities_matrix(self):

    n = len(self._cities)
    print("     ", end='')
    for i in range(n):
        print('{:3}'.format(i), end='')
    print('\n    '+"----"*n)
    for i in range(n):
        print('{:2} | '.format(i), end='')
        for j in range(n):
            print('{:3}'.format(self._cities[i][j]), end='')
        print()


