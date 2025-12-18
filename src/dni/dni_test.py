import pytest

from src.dni.dni import DNI
from src.dni.validation_error import ValidationError


def test_valid_dni():
    raw_dni = "31970165P"

    dni = DNI.create_of_value(value=raw_dni)

    assert dni.value() == raw_dni


def test_error_dni_length_less_than_9():
    with pytest.raises(ValidationError):
        DNI.create_of_value(value="3197016P")


def test_error_dni_length_greater_than_9():
    with pytest.raises(ValidationError):
        DNI.create_of_value(value="319701655P")


def test_first_8_characters_should_be_numbers():
    with pytest.raises(ValidationError):
        DNI.create_of_value(value="3A970165P")


def test_last_characters_should_be_a_letter():
    with pytest.raises(ValidationError):
        DNI.create_of_value(value="319701657")


def test_letter_validation():
    with pytest.raises(ValidationError):
        DNI.create_of_value(value="31970165A")
