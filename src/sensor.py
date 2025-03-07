from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod
    def pop_next_pressure_psi_value(self) -> int:
        pass