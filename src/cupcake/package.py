from src.cupcake.dessert import Dessert


class Package(Dessert):

    def __init__(self):
        self.desserts = []

    def price(self) -> float:
        total_price = 0.0

        for dessert in self.desserts:
            if isinstance(dessert, Package):
                total_price += dessert.price()
            else:
                total_price += dessert.price() * 0.9

        return round(total_price, 2)

    def name(self) -> str:
        return "Package"

    def append(self,
               dessert: Dessert):
        self.desserts.append(dessert)