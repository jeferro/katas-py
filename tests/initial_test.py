import pytest

from src.string_calculator import StringCalculator


def test_when_empty_string_then_return_zero():
    string_calculator = StringCalculator()

    assert string_calculator.add(f"") == 0


def test_when_string_with_unique_value_then_return_value():
    string_calculator = StringCalculator()

    value = 1
    assert string_calculator.add(f"{value}") == value


def test_when_string_with_two_values_then_return_sum():
    string_calculator = StringCalculator()

    assert string_calculator.add(f"1,2") == 3


def test_when_string_with_three_values_then_return_sum():
    string_calculator = StringCalculator()

    assert string_calculator.add(f"1,2,3") == 6


def test_when_string_with_four_values_then_return_sum():
    string_calculator = StringCalculator()

    assert string_calculator.add(f"1,2,3,4") == 10


def test_allow_using_new_line_between_numbers():
    string_calculator = StringCalculator()

    assert string_calculator.add(f"1\n2,3,4") == 10


def test_allow_different_delimiters():
    string_calculator = StringCalculator()

    assert string_calculator.add(f"//;\n1;2") == 3


def test_not_allowed_negative_numbers():
    with pytest.raises(RuntimeError) as cause:
        string_calculator = StringCalculator()
        string_calculator.add(f"//;\n-1;-2;3")

    assert "Invalid negative numbers: [-1, -2]" in str(cause.value)


def test_ignore_numbers_bigger_than_1000():
    string_calculator = StringCalculator()

    assert string_calculator.add(f"2,1001") == 2


def test_delimiter_can_be_of_any_length():
    string_calculator = StringCalculator()

    assert string_calculator.add(f"//[***]\n1***2***3") == 6
