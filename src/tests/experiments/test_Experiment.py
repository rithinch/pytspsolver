import pytest
from pytspsolver.experiments import Experiment

class Test_Experiment(object):
  
  def test_Experiment_Init_ShouldSucceedWithDefaultValues(self):
        
    exp = Experiment()

    assert exp._problems == []
    assert exp._solvers == []
  
  def test_Experiment_Init_ShouldSucceedWithPassedValues(self):

    exp = Experiment([1], [2])

    assert exp._problems == [1]
    assert exp._solvers == [2]
  
  def test_Experiment_add_problem_ShouldSucceed(self):

    exp = Experiment()
    count = len(exp._problems)

    exp.add_problem(1)

    assert len(exp._problems) == count+1
  
  def test_Experiment_add_problems_ShouldSucceed(self):

    exp = Experiment([])
    count = len(exp._problems)

    exp.add_problems([1,2,3])

    assert len(exp._problems) == count+3

  def test_Experiment_add_solver_ShouldSucceed(self):

    exp = Experiment()
    count = len(exp._solvers)

    exp.add_solver(1)

    assert len(exp._solvers) == count+1
  
  
  def test_Experiment_run_ShouldSucceed(self):

    epoch = 3

    exp = Experiment([], [])

    exp.run(epoch=epoch)
    
    assert len(exp._results['epochs']) == epoch

  
 



      

