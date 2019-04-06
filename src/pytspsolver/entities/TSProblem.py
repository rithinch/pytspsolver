import networkx as nx
import numpy as np

class TSProblem():
  
  def __init__(self, name, cities_mx=[], optimal=-1):
    self._cities = cities_mx
    self.name = name
    self.size = len(cities_mx)
    self.optimal = -1
    
  def get_cities(self):
    return self._cities
  
  def get_details(self):
    return self.name

  def visualize(self, plt, show=True):
    G = nx.from_numpy_matrix((np.array(self._cities)))
    
    pos = nx.circular_layout(G)
    
    nx.draw_networkx(G, pos=pos, with_labels=True)
    
    labels = nx.get_edge_attributes(G,'weight')
    
    nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=labels)
    
    plt.title("{0} - Visualization".format(self.name))
    plt.axis('off')

    if show:
      plt.show()
    
  def __str__(self):

    n = len(self._cities)
    
    to_print = "    "
    
    for i in range(n):
        to_print+= '{:3}'.format(i)
    to_print+= '\n    '+"----"*n+"\n"
    
    for i in range(n):
        to_print+='{:2} | '.format(i)
        for j in range(n):
            to_print+='{:3}'.format(self._cities[i][j])
        to_print+="\n"
    
    return to_print


