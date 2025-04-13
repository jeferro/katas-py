from src.Dessert import Dessert
from src.decorations.Decorator import Decorator


class Chocolate(Decorator):

    def __init__(self,
                 dessert: Dessert):
        super().__init__(dessert)

    def _decorator_price(self) -> float:
        return 0.1

    def _decorator_name(self) -> str:
        return "chocolate"
