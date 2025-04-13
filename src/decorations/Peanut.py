from src.Dessert import Dessert
from src.decorations.Decorator import Decorator


class Peanut(Decorator):

    def __init__(self,
                 dessert: Dessert):
        super().__init__(dessert)

    def _decorator_price(self) -> float:
        return 0.2

    def _decorator_name(self) -> str:
        return "peanut"