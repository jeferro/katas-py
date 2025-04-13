from src.Dessert import Dessert


class Chocolate(Dessert):

    def __init__(self,
                 dessert: Dessert):
        self.dessert = dessert

    def price(self) -> float:
        return self.dessert.price() + 0.1

    def name(self) -> str:
        return f"{self.dessert.name()} with chocolate"
