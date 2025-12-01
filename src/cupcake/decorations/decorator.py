from abc import ABC, abstractmethod

from src.cupcake.dessert import Dessert


class Decorator(Dessert, ABC):

    def __init__(self,
                 dessert: Dessert):
        self.dessert = dessert

    def price(self) -> float:
        result = self.dessert.price() + self._decorator_price()

        return round(result, 2)

    def name(self) -> str:
        if isinstance(self.dessert, Decorator):
            word = "and"
        else:
            word = "with"

        return f"{self.dessert.name()} {word} {self._decorator_name()}"

    @abstractmethod
    def _decorator_price(self) -> float:
        pass

    @abstractmethod
    def _decorator_name(self) -> str:
        pass
