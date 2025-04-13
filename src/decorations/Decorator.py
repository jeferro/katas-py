from abc import ABC, abstractmethod
from src.Dessert import Dessert


class Decorator(Dessert, ABC):

    def __init__(self,
                 dessert: Dessert):
        self.dessert = dessert

    def price(self) -> float:
        return self.dessert.price() + self._decorator_price()

    def name(self) -> str:
        return f"{self.dessert.name()} with {self._decorator_name()}"

    @abstractmethod
    def _decorator_price(self) -> float:
        pass

    @abstractmethod
    def _decorator_name(self) -> str:
        pass
