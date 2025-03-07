from src.african_parrot import AfricanParrot
from src.european_parrot import EuropeanParrot
from src.norwegian_blue_parrot import NorwegianBlueParrot


def test_speed_of_european_parrot():
    parrot = EuropeanParrot.create_of(voltage=0)

    assert parrot.speed() == 12.0


def test_cry_of_european_parrot():
    parrot = EuropeanParrot.create_of(voltage=0)

    assert parrot.cry() == "Sqoork!"


def test_speed_of_african_parrot_with_one_coconut():
    parrot = AfricanParrot.create_of(voltage=0, number_of_coconuts=1)

    assert parrot.speed() == 3.0


def test_cry_of_african_parrot():
    parrot = AfricanParrot.create_of(voltage=1, number_of_coconuts=0)

    assert parrot.cry() == "Sqaark!"


def test_speed_of_african_parrot_with_two_coconuts():
    parrot = AfricanParrot.create_of(voltage=1, number_of_coconuts=2)

    assert parrot.speed() == 0.0


def test_speed_of_african_parrot_with_no_coconuts():
    parrot = AfricanParrot.create_of(voltage=0, number_of_coconuts=0)

    assert parrot.speed() == 12.0


def test_speed_norwegian_blue_parrot_nailed():
    parrot = NorwegianBlueParrot.create_of(voltage=1.5, nailed=True)

    assert parrot.speed() == 0.0


def test_speed_norwegian_blue_parrot_not_nailed():
    parrot = NorwegianBlueParrot.create_of(voltage=1.5, nailed=False)

    assert parrot.speed() == 18.0


def test_speed_norwegian_blue_parrot_not_nailed_high_voltage():
    parrot = NorwegianBlueParrot.create_of(voltage=4, nailed=False)

    assert parrot.speed() == 24.0


def test_cry_norwegian_blue_parrot_high_voltage():
    parrot = NorwegianBlueParrot.create_of(voltage=4, nailed=False)

    assert parrot.cry() == "Bzzzzzz"


def test_cry_norwegian_blue_parrot_no_voltage():
    parrot = NorwegianBlueParrot.create_of(voltage=0, nailed=False)

    assert parrot.cry() == "..."
