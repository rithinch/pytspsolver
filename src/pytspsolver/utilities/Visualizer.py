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

  
  def __get_solver_vs_cost_data(self, problemName, epoch=-1):
    data = []

    if epoch>-1:
      for solver in self.__run_details['solver_names']:
        data.append(self._results[epoch][problemName][solver]['cost'])
    else:
      for solver in self.__run_details['solver_names']:
        avg=sum([self._results[epoch][problemName][solver]['cost'] for epoch in self._results])/len(self._results)
        data.append(avg)

    datapoints = [self.__run_details['solver_names'], data]
    
    return datapoints

  
  def plot_solver_vs_cost(self, plt, problemName, epoch=-1):

    datapoints = self.__get_solver_vs_cost_data(problemName, epoch=epoch)
    
    index = np.arange(len(datapoints[0]))
    
    plt.bar(index, datapoints[1], width=0.7, edgecolor='blue')

    for i, v in enumerate(datapoints[1]):
      plt.text(i-.05, v+(0.05*v), " "+str(v), color='blue', va='center', fontweight='bold')

    plt.xlabel('Solvers')
    plt.ylabel('Minimum Path Cost')
    plt.xticks(index, datapoints[0], rotation=0)
    plt.title('Comparision of Solvers by Min Cost - '+problemName)
    plt.ylim(0, max(datapoints[1])*2)

    plt.show()
    

  def plot_time_vs_cost(self, plt, solverName, problemName, epoch=-1):

    datapoints = self.__get_time_vs_cost_data(problemName, solverName, epoch=epoch)
    
    init_x, init_y = datapoints[0][0], datapoints[1][0]
    min_x, min_y = datapoints[0][-1], datapoints[1][-1]
    
    point_label = "({0:.2f},{1:.2f})"

    plt.plot(datapoints[0], datapoints[1])
    
    
    for x,y in [(init_x, init_y), (min_x, min_y)]:
      plt.plot(x, y, '^')
      plt.text(x-(0.05*x), y+(0.05*y),point_label.format(x, y), color='blue', va='center', fontweight='bold')
    
    plt.xlim(-0.005, min_x+(0.25*min_x))
    plt.ylim(0, init_y+(0.25*init_y))

    plt.title("Time (s) vs Cost - "+problemName)
    plt.xlabel("Time Taken (s)")
    plt.ylabel("Path Cost (units)")
    plt.legend([solverName, "Final Cost"], loc='upper right')

    plt.show()
  

  def plot_time_vs_cost_all(self, plt, problemName, epoch=-1):

    data_points = {}
    legend = []
    point_label = "({0:.5f},{1:.2f})"
    xlim, ylim = 0, 0

    for solverName in self.__run_details['solver_names']:
      data_points[solverName] = self.__get_time_vs_cost_data(problemName, solverName, epoch=epoch)
    
    for solverName in self.__run_details['solver_names']:
      legend.append(solverName)
      legend.append("Initial Cost - "+solverName)
      legend.append("Final Cost - "+solverName)

      plt.plot(data_points[solverName][0], data_points[solverName][1])

      init_x, init_y = data_points[solverName][0][0], data_points[solverName][1][0]
      min_x, min_y = data_points[solverName][0][-1], data_points[solverName][1][-1]

      for x,y in [(init_x, init_y), (min_x, min_y)]:
        plt.plot(x, y, 'o')
        
        plt.text(x-(0.05*x), y+(0.05*y),point_label.format(x, y), color='blue', va='center')

      if init_y > ylim:
        ylim = init_y
      
      if min_x > xlim:
        xlim = min_x
    
    plt.xlim(-0.005, xlim+(0.25*xlim))
    plt.ylim(0, ylim+(0.5*ylim))

    plt.title("Time (s) vs Cost - All Solvers for "+problemName)
    plt.xlabel("Time Taken (s)")
    plt.ylabel("Path Cost (units)")

    plt.legend(legend, loc='upper right')

    plt.show()


  def plot_n_vs_time(self, plt, solverName, epoch=-1):

    data_points = self.__get_n_vs_time_data(solverName, epoch=epoch)
    
    plt.plot(data_points[0], data_points[1], 'ro-')
    plt.title("Problem Size (n) vs Time - "+solverName)
    plt.xlabel("No of cities n")
    plt.ylabel("Time Taken (s)")
    plt.legend([solverName], loc='upper left')

    plt.show()
  

  def plot_n_vs_time_all(self, plt, epoch=-1):

    data_points = {}

    for solverName in self.__run_details['solver_names']:

      data_points[solverName] = self.__get_n_vs_time_data(solverName, epoch=epoch)
    
    for solverName in self.__run_details['solver_names']:
      plt.plot(data_points[solverName][0], data_points[solverName][1])

    plt.title("Problem Size (n) vs Time - All Solvers")
    plt.xlabel("No of cities n")
    plt.ylabel("Time Taken (s)")
    plt.legend(self.__run_details['solver_names'], loc='upper left')

    plt.show()

    