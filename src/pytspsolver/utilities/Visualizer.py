import numpy as np
from tabulate import tabulate
import pandas as pd

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
          size = len(result['best_path'])-1
          time = result['time']
          x.append(size)
          y.append(time)
        
      d = {}
      new_x, new_y = [], []

      for i in range(len(x)):
        if x[i] in d:
          d[x[i]][0]+=1
          d[x[i]][1].append(i)
        else:
          d[x[i]]=[1,[i]]
      added = set()

      for i in range(len(x)):
        size = x[i]
        if size in added:
          continue
        avg1 = 0
        if d[size][0] > 1:
          for j in d[size][1]:
            avg1+= y[j]
          avg1 = avg1/d[size][0]
        else:
          avg1 = y[i]
        
        new_x.append(size)
        new_y.append(avg1)
        added.add(size)

      filtered_results[epoch] = [new_x,new_y]
    
    if epoch>-1:
      data_points = filtered_results[epoch]
    else:
      avg_y_values = sum([np.array(filtered_results[i][1]) for i in filtered_results])/len(filtered_results)
      data_points = [filtered_results[0][0], list(avg_y_values)]
    
    return data_points

  def __get_time_vs_cost_data(self, problemName, solverName, epoch=-1):

    temp = []

    for e in self._results:
      if epoch>-1 and e!=epoch:
        continue
      temp.append(np.array(self._results[e][problemName][solverName]['time_vs_cost']))

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

  def __get_problem_vs_cost_data(self, epoch=-1):

    data = []

    for problem in self.__run_details['problem_names']:
      data.append(self.__get_solver_vs_cost_data(problem))
    
    d = np.array(data)

    solver_results = np.transpose(d[:,1])

    solver_names = d[0,0]

    return [self.__run_details['problem_names'], solver_names, solver_results.astype(np.float)]


  def plot_problem_vs_cost_all(self, plt, epoch=-1):
    
    datapoints = self.__get_problem_vs_cost_data(epoch=epoch)
    problem_names = datapoints[0]
    solver_names = datapoints[1]
    solver_results = datapoints[2]

    n_groups = len(problem_names)
    index = np.arange(n_groups)

    bar_width = 0.35
    opacity = 0.8

    fig, ax = plt.subplots()

    for i in range(len(solver_names)):
      rects = ax.bar(index+(i*bar_width), solver_results[i], bar_width,alpha=opacity,label=solver_names[i])
      for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()*0.5, 1.02*height,
                '{}'.format(height), color='blue', ha='center', va='center', fontweight='bold')
    
    ax.set_ylabel('Cost')
    ax.set_xlabel('Problems')
    ax.set_title('Cost Comparision - All Solvers and Problems')
    ax.set_xticks(index + bar_width/len(solver_names))
    ax.set_xticklabels(problem_names)
    ax.legend()

    plt.show()


  def plot_solver_vs_cost(self, plt, problemName, epoch=-1):

    datapoints = self.__get_solver_vs_cost_data(problemName, epoch=epoch)
    
    index = np.arange(len(datapoints[0]))
    
    rects = plt.bar(index, datapoints[1], width=0.7, edgecolor='blue')

    for rect in rects:
      height = rect.get_height()
      plt.text(rect.get_x() + rect.get_width()*0.5, 1.05*height,
              '{}'.format(height), color='blue', ha='center', va='center', fontweight='bold')

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

    plt.title("Time (s) vs Cost - {0} - {1}".format(solverName, problemName))
    plt.xlabel("Time Taken (s)")
    plt.ylabel("Path Cost (units)")
    plt.legend([solverName, "Initial Cost", "Final Cost"], loc='best')

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
        
        #plt.text(x-(0.05*x), y+(0.05*y),point_label.format(x, y), color='blue', va='center')

      if init_y > ylim:
        ylim = init_y
      
      if min_x > xlim:
        xlim = min_x
    
    #plt.xlim(-0.005, xlim+(0.25*xlim))
    #plt.ylim(0, ylim+(0.5*ylim))

    plt.title("Time (s) vs Cost - All Solvers for "+problemName)
    plt.xlabel("Time Taken (s)")
    plt.ylabel("Path Cost (units)")

    plt.legend(legend, loc='best')

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

  def n_vs_time_all_table(self, epoch=-1):
    
    data_points = {}

    for solverName in self.__run_details['solver_names']:

      data_points[solverName] = self.__get_n_vs_time_data(solverName, epoch=epoch)
    
    n = None
    d = {}

    for solverName in self.__run_details['solver_names']:
      if n==None:
        n = data_points[solverName][0]
        d["Problem Size"] = n
        
      d[solverName] = data_points[solverName][1]
    
    df = pd.DataFrame(d)

    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))

  
  def n_vs_accuracy_all_table(self, epoch=-1):
    
    data_points = {}

    datapoints = self.__get_problem_vs_cost_data(epoch=epoch)
    problem_names = datapoints[0]
    solver_names = datapoints[1]
    solver_results = datapoints[2]
    
    n = None
    d = {}

    
    for i in range(len(solver_names)):
        if n==None:
          x = self.__get_n_vs_time_data(solver_names[i], epoch=epoch)
          d["Problem Size"] = x[0]

        d[solver_names[i]] = solver_results[i]
    

    d["Optimal Cost"] = [2085, 2707, 1272, 5046, 6942, 21407, 48450, 92650]
    df = pd.DataFrame(d)

    print(tabulate(df, headers='keys', tablefmt='psql', showindex=False))
    
  def plot_problem_vs_cost_line_all(self, plt, epoch=-1):
    
      datapoints = self.__get_problem_vs_cost_data(epoch=epoch)
      problem_names = datapoints[0]
      solver_names = datapoints[1]
      solver_results = datapoints[2]
      
      a = list(map(int, problem_names))
      
      fig, ax = plt.subplots()

      ax.set_ylabel('Cost')
      ax.set_xlabel('Problems')
      ax.set_title('Cost Comparision - All Solvers and Problems')
      #ax.set_xticklabels(a)

      legend = []
      for solver in solver_names:
        legend.append(solver)

      for i in range(len(solver_names)):
        
        plt.plot(a, solver_results[i], 'o-')

      plt.legend(legend)
      #plt.xlim(0, 30)
      #plt.ylim(0,1000)
      plt.show()
