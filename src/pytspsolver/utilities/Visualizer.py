import numpy as np

class Visualizer():

  def __init__(self, results):
    
    self.__run_details = results['details']
    self._results = results['epochs']
  

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
    
    if epoch>-1:
      data_points = filtered_results[epoch]
    else:
      avg_y_values = sum([np.array(filtered_results[i][1]) for i in filtered_results])/len(filtered_results)
      data_points = [filtered_results[0][0], list(avg_y_values)]
    
    return data_points
  

  def __get_time_vs_cost_data(self, problemName, solverName, epoch=-1):

    if epoch>-1:
      data_points = [[],[]]
      for pair in self._results[epoch][problemName][solverName]['time_vs_cost']:
        data_points[0].append(pair[0])
        data_points[1].append(pair[1])
    else:
      temp = []
      for epoch in self._results:
        temp.append(np.array(self._results[epoch][problemName][solverName]['time_vs_cost']))
      avg_results = sum(temp)/len(self._results)
      datapoints = [list(avg_results[:,0]), list(avg_results[:,1])]
    
    return datapoints
  

  def plot_time_vs_cost(self, plt, solverName, problemName, epoch=-1):

    datapoints = self.__get_time_vs_cost_data(problemName, solverName, epoch=epoch)

    plt.plot(datapoints[0], datapoints[1])
    plt.plot(datapoints[0][-1], datapoints[1][-1], '^')
    plt.title("Time (s) vs Cost - "+problemName)
    plt.xlabel("Time Taken (s)")
    plt.ylabel("Path Cost (units)")
    plt.legend([solverName, 'Minimum Cost'], loc='upper right')
  

  def plot_time_vs_cost_all(self, plt, problemName, epoch=-1):

    data_points = {}
    legend = []
    for solverName in self.__run_details['solver_names']:
      data_points[solverName] = self.__get_time_vs_cost_data(problemName, solverName, epoch=epoch)
    
    for solverName in self.__run_details['solver_names']:
      legend.append(solverName)
      legend.append("Minimum Cost - "+solverName)
      plt.plot(data_points[solverName][0], data_points[solverName][1])
      plt.plot(data_points[solverName][0][-1], data_points[solverName][1][-1], '^')
    
    plt.title("Time (s) vs Cost - All Solvers for "+problemName)
    plt.xlabel("Time Taken (s)")
    plt.ylabel("Path Cost (units)")

    
    plt.legend(legend, loc='upper right')


  def plot_n_vs_time(self, plt, solverName, epoch=-1):

    data_points = self.__get_n_vs_time_data(solverName, epoch=epoch)
    
    plt.plot(data_points[0], data_points[1], 'ro-')
    plt.title("Problem Size (n) vs Time - "+solverName)
    plt.xlabel("No of cities n")
    plt.ylabel("Time Taken (s)")
    plt.legend([solverName], loc='upper left')
  

  def plot_n_vs_time_all(self, plt, epoch=-1):

    data_points = {}

    for solverName in self.__run_details['solver_names']:

      data_points[solverName] = self.__get_n_vs_time_data(solverName, epoch=epoch)
    
    for solverName in self.__run_details['solver_names']:
      print(data_points[solverName][0][-1], data_points[solverName][1][-1])
      plt.plot(data_points[solverName][0], data_points[solverName][1])

    plt.title("Problem Size (n) vs Time - All Solvers")
    plt.xlabel("No of cities n")
    plt.ylabel("Time Taken (s)")
    plt.legend(self.__run_details['solver_names'], loc='upper left')

    