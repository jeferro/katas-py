
from src.Cookie import Cookie


def test_cookie_price():
    cookie = Cookie()
    assert cookie.price() == 2.0


def test_cookie_name():
    cookie = Cookie()
    assert cookie.name() == "Cookie"
