import pytest

from src.dni.dni import DNI
from src.dni.validation_error import ValidationError


def test_valid_dni():
    raw_dni = "31970165G"

    dni = DNI.create_of_value(value=raw_dni)

    assert dni.value() == raw_dni


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


def test_letter_u_is_not_allowed():
    with pytest.raises(ValidationError):
        DNI.create_of_value(value="31970165U")


def test_letter_i_is_not_allowed():
    with pytest.raises(ValidationError):
        DNI.create_of_value(value="31970165I")


def test_letter_o_is_not_allowed():
    with pytest.raises(ValidationError):
        DNI.create_of_value(value="31970165O")


def test_letter_eñe_is_not_allowed():
    with pytest.raises(ValidationError):
        DNI.create_of_value(value="31970165Ñ")
