from src.cupcake.cookie import Cookie
from src.cupcake.cupcake import Cupcake
from src.cupcake.package import Package


def test_package_with_cupcake_price():
    cupcake = Cupcake()

    package = Package()
    package.append(cupcake)

    assert package.price() == 0.9


def test_package_with_cupcake_and_cookie_price():
    cupcake = Cupcake()
    cookie = Cookie()

    package = Package()
    package.append(cupcake)
    package.append(cookie)

    assert package.price() == 2.7


def test_multiple_package_inside_price():
    cupcake1 = Cupcake()
    cookie = Cookie()

    package_in = Package()
    package_in.append(cupcake1)
    package_in.append(cookie)

    cupcake2 = Cupcake()

    package = Package()
    package.append(cupcake2)
    package.append(package_in)

    assert package.price() == 3.6
