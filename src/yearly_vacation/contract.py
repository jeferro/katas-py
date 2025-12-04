from abc import ABC, abstractmethod
from datetime import date

class Contract(ABC):

    def __init__(self,
                 name: str,
                 start_date: date):
        self.name = name
        self.start_date = start_date

    @abstractmethod
    def num_vacation_days(self,
                          a_date: date):
        pass
