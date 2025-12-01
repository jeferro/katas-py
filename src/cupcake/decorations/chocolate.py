from src.cupcake.dessert import Dessert
from src.cupcake.decorations.decorator import Decorator


class Chocolate(Decorator):

    def __init__(self,
                 dessert: Dessert):
        super().__init__(dessert)

    def _decorator_price(self) -> float:
        return 0.1

    def _decorator_name(self) -> str:
        return "chocolate"
