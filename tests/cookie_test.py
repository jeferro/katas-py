from src.Cookie import Cookie
from src.decorations.Chocolate import Chocolate
from src.decorations.Peanut import Peanut


def test_cookie_price():
    dessert = Cookie()
    assert dessert.price() == 2.0

def test_cookie_name():
    dessert = Cookie()
    assert dessert.name() == "Cookie"

def test_cookie_with_chocolate_price():
    dessert = Chocolate(Cookie())
    assert dessert.price() == 2.1

def test_cookie_with_chocolate_name():
    dessert = Chocolate(Cookie())
    assert dessert.name() == "Cookie with chocolate"

def test_cookie_with_peanut_price():
    dessert = Peanut(Cookie())
    assert dessert.price() == 2.2

def test_cookie_with_peanut_name():
    dessert = Peanut(Cookie())
    assert dessert.name() == "Cookie with peanut"

def test_cookie_with_chocolate_and_peanut_price():
    dessert = Peanut(Chocolate(Cookie()))
    assert dessert.price() == 2.3

def test_cookie_with_chocolate_and_peanut_name():
    dessert = Peanut(Chocolate(Cookie()))
    assert dessert.name() == "Cookie with chocolate and peanut"

def test_cookie_with_peanut_chocolate_price():
    dessert = Chocolate(Peanut(Cookie()))
    assert dessert.price() == 2.3

def test_cookie_with_peanut_and_chocolate_name():
    dessert = Chocolate(Peanut(Cookie()))
    assert dessert.name() == "Cookie with peanut and chocolate"

