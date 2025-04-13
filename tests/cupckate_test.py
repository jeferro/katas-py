from src.Cupcake import Cupcake
from src.decorations.Chocolate import Chocolate


def test_cupcake_price():
    dessert = Cupcake()
    assert dessert.price() == 1.0

def test_cupcake_name():
    dessert = Cupcake()
    assert dessert.name() == "Cupcake"

def test_cupcake_with_chocolate_price():
    dessert = Chocolate(Cupcake())
    assert dessert.price() == 1.1

def test_cupcake_with_chocolate_name():
    dessert = Chocolate(Cupcake())
    assert dessert.name() == "Cupcake with chocolate"
