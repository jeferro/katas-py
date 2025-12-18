from typing import List

from src.dni.validation_error import ValidationError


class DNI(object):
    _LETTERS = ["T",
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
                 value: str):
        self._value = value

    @staticmethod
    def create_of_value(value: str):
        if len(value) != 9:
            raise ValidationError(f"DNI length must be 9: {value}")

        numbers = []
        letter = None

        for index, character in enumerate(value):
            if index < 8:
                if not character.isnumeric():
                    raise ValidationError(f"DNI character in index {index} must be a numeric: {value}")

                number = int(character)

                numbers.append(number)
            else:
                last_character = character.upper()

                if not last_character:
                    raise ValidationError(f"DNI last character must be a letter: {value}")

                letter = DNI._calculate_letter(numbers)

                if last_character != letter:
                    raise ValidationError(f"DNI letter invalid: {value}. Expected letter: {letter}")


        return DNI(value)

    def value(self) -> str:
        return self._value

    @staticmethod
    def _calculate_letter(numbers: List[int]) -> str:
        sum = 0
        total_letters = len(DNI._LETTERS)

        for number in numbers:
            sum += number

        index = (sum % total_letters) - 1

        if index >= total_letters:
            raise ValidationError(f"Out of index: {index}")

        return DNI._LETTERS[index]
