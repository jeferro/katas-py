
from src.square import Square


def test_area_calculation():
    square = Square(12)
    assert square.calculate_area() == 144
