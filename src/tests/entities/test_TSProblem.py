import pytest
from pytspsolver.entities import TSProblem

class Test_TSProblem(object):
  
  def test_TSProblem_Init_ShouldSucceedWithDefaultValues(self):
        
        name = 'Problem1'

        prob = TSProblem(name)

        assert prob.name == 'Problem1'
        assert type(prob._cities) == list
