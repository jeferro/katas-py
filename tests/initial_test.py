
from src.Cupcake import Cupcake


def test_cupcake_price():
    cupcake = Cupcake()
    assert cupcake.price() == 1.0


def test_cupcake_name():
    cupcake = Cupcake()
    assert cupcake.name() == "Cupcake"
