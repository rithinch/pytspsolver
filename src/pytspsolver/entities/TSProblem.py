class TSProblem():
  
  def __init__(self, cities_mx=None):

    if cities_mx:
      self._cities = cities_mx
    else:
      self._cities = []

  def get_cities(self):
    return self._cities
  
  def get_details(self):
    pass

  def __str__(self):

    n = len(self._cities)
    
    to_print = ""
    
    for i in range(n):
        to_print+= '{:3}'.format(i)
    to_print+= '\n    '+"----"*n
    
    for i in range(n):
        to_print+='{:2} | '.format(i)
        for j in range(n):
            to_print+='{:3}'.format(self._cities[i][j])
        to_print+="\n"
    
    return to_print


