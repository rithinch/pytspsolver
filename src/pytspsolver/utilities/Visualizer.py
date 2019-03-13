import numpy as np

class Visualizer():

  def __init__(self, results):
    
    self._results = results
  
  def __get_n_vs_time_data(self, solverName, epoch=-1):

    filtered_results = {}

    for epoch in self._results:
      results = self._results[epoch]
      x = []
      y = []
      for prob in results:
        if solverName in results[prob]:
          result = results[prob][solverName]
          x.append(len(result['best_path'])-1)
          y.append(result['time'])
        
      filtered_results[epoch] = [x,y]
    
    if epoch>0:
      data_points = filtered_results[epoch]
    else:
      avg_y_values = sum([np.array(filtered_results[i][1]) for i in filtered_results])/len(filtered_results)
      data_points = [filtered_results[0][0], list(avg_y_values)]
    
    return data_points
  
  def plot_time_vs_cost(self, epoch=0, name=''):
    pass
  
  def plot_n_vs_time(self, plt, solverName, epoch=-1):

    data_points = self.__get_n_vs_time_data(solverName, epoch=epoch)
    
    plt.plot(data_points[0], data_points[1], 'ro-')
    plt.title("Problem Size (n) vs Time - "+solverName)
    plt.xlabel("No of cities n")
    plt.ylabel("Time Taken (s)")
    