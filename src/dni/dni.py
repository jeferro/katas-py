from src.dni.validation_error import ValidationError


class DNI(object):

    _UNALLOWED_LETTERS = ["U", "I", "O", "Ñ"]

    def __init__(self,
                 value: str):
        self._value = value

    @staticmethod
    def create_of_value(value: str):
        if len(value) != 9:
            raise ValidationError("DNI length must be 9: " + value)

        numbers = []
        letter = None

        for index, character in enumerate(value):
            if index < 8:
                if not character.isnumeric():
                    raise ValidationError(f"DNI character in index {index} must be a numeric: " + value)

                number = int(character)

                numbers.append(number)
            else:
                if not character.isalpha():
                    raise ValidationError(f"DNI last character must be a letter: " + value)

                letter = character.upper()

                if letter in DNI._UNALLOWED_LETTERS:
                    raise ValidationError("DNI letter not allowed: " + value)

        return DNI(value)

    def value(self) -> str:
        return self._value