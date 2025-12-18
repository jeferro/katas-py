from typing import List

from src.dni.validation_error import ValidationError


class DNI(object):
    _NIE_CHARACTERS = [
        "X",
        "Y",
        "Z",
    ]

    _CONTROL_DIGITS = [
        "T",
        "R",
        "W",
        "A",
        "G",
        "M",
        "Y",
        "F",
        "P",
        "D",
        "X",
        "B",
        "N",
        "J",
        "Z",
        "S",
        "Q",
        "V",
        "H",
        "L",
        "C",
        "K",
        "E"]

    def __init__(self,
                 letter: str,
                 numbers: List[int],
                 control_digit: str):
        self._letter = letter
        self._numbers = numbers
        self._control_digit = control_digit

    @staticmethod
    def create(value: str):
        if len(value) != 9:
            raise ValidationError(f"DNI length must be 9: {value}")

        letter = None
        numbers = []
        control_digit = None

        for index, character in enumerate(value):
            if index == 0:
                if character.isnumeric():
                    number = int(character)

                    numbers.append(number)
                else:
                    letter = character

            elif index < 8:
                if not character.isnumeric():
                    raise ValidationError(f"DNI character in index {index} must be a numeric: {value}")

                number = int(character)

                numbers.append(number)
            else:
                last_character = character.upper()

                if not last_character:
                    raise ValidationError(f"DNI last character must be a letter: {value}")

                control_digit = DNI._calculate_control_digit(letter, numbers)

                if last_character != control_digit:
                    raise ValidationError(f"DNI control digit invalid: {value}. Expected digit control: {control_digit}")


        return DNI(letter, numbers, control_digit)

    def value(self) -> str:
        output = ""

        if self._letter is not None:
            output += self._letter

        for number in self._numbers:
            output += str(number)

        output += str(self._control_digit)

        return output

    @staticmethod
    def _calculate_control_digit(letter, numbers: List[int]) -> str:
        sum = 0
        total_letters = len(DNI._CONTROL_DIGITS)

        if letter is not None:
            sum += DNI._NIE_CHARACTERS.index(letter)

        for number in numbers:
            sum += number

        index = (sum % total_letters) - 1

        if index >= total_letters:
            raise ValidationError(f"Out of index: {index}")

        return DNI._CONTROL_DIGITS[index]
