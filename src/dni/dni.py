from src.dni.validation_error import ValidationError


class DNI(object):

    _UNALLOWED_LETTERS = ["U", "I", "O", "Ñ"]

    def __init__(self,
                 value: str):
        self._value = value

    @staticmethod
    def create_of_value(value: str):
        if len(value) != 9:
            raise ValidationError("DNI length must be 9")

        numbers = value[:8]

        if not numbers.isnumeric():
            raise ValidationError("DNI first 8 characters must be numeric")

        letter = value[8]

        if not letter.isalpha():
            raise ValidationError("DNI last character must be numeric")

        if letter.upper() in DNI._UNALLOWED_LETTERS:
            raise ValidationError("DNI letter not allowed")

        return DNI(value)

    def value(self) -> str:
        return self._value