from abc import ABC, abstractmethod

class Contract(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def num_vacation_days(self):
        pass
