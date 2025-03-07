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
