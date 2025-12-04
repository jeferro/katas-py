from abc import ABC, abstractmethod

class Contract(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def calculate_num_vacation(self):
        pass
