from src.cupcake.dessert import Dessert


class Cookie(Dessert):

    def __init__(self):
        pass

    def price(self) -> float:
        return 2.0

    def name(self) -> str:
        return "Cookie"
