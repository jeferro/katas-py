import pytest

from src.dni.dni import DNI
from src.dni.validation_error import ValidationError


def test_valid_dni():
    DNI.create_of_value(value="31970165G")


def test_error_dni_length_less_than_9():
    with pytest.raises(ValidationError):
        DNI.create_of_value(value="3197016G")


def test_error_dni_length_greater_than_9():
    with pytest.raises(ValidationError):
        DNI.create_of_value(value="319701655G")


def test_first_8_characters_should_be_numbers():
    with pytest.raises(ValidationError):
        DNI.create_of_value(value="3A970165G")


def test_last_characters_should_be_a_letter():
    with pytest.raises(ValidationError):
        DNI.create_of_value(value="319701657")
