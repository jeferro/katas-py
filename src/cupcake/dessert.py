
from abc import ABC, abstractmethod

class Dessert(ABC):

    @abstractmethod
    def price(self) -> float:
        pass

    @abstractmethod
    def name(self) -> str:
        pass