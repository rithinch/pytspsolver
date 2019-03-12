import matplotlib.pyplot as plt

class Visualizer():

  def __init__(self, results):
    
    self._results = results
  
  def plot_time_vs_cost(self, epoch=0, name=''):
    pass
  
  def plot_n_vs_time(self, epoch=0):

    if epoch in self._results:

      results = self._results[epoch]

      x = []
      y = []

      for result in results:
        x.append(len(result['best_path']))
        y.append(result['time'])
      
      plt.plot(x, y, 'ro-')
      plt.show()
    