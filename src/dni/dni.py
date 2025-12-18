from src.dni.validation_error import ValidationError


class DNI(object):

    def __init__(self,
                 value: str):
        self.value = value

    @staticmethod
    def create_of_value(value: str):
        if len(value) != 9:
            raise ValidationError("DNI length must be 9")

        return DNI(value)