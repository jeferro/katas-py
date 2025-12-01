from src.cupcake.dessert import Dessert


class Cupcake(Dessert):

    def __init__(self):
        pass

    def price(self) -> float:
        return 1.0

    def name(self) -> str:
        return "Cupcake"
