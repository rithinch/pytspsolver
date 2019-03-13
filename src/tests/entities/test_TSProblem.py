import pytest
from pytspsolver.entities import TSProblem

class Test_TSProblem(object):
  
  def test_init_shouldSucceedWithDefaultValues(self):
        
        name = 'Problem1'

        prob = TSProblem(name)

        assert prob.name == 'Problem1'
        assert type(prob._cities) == list
