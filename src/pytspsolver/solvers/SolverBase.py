from abc import ABC, abstractmethod

class SolverBase(ABC):
    
    def __init__(self, name):
        self._name = name
        super().__init__()
    
    @abstractmethod
    def run(self, tsp_problem):
        pass
    

    

