from enum import Enum


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class Parrot:

    def __init__(self,
                 type_of_parrot: ParrotType.EUROPEAN,
                 number_of_coconuts: float,
                 voltage: float,
                 nailed: bool):
        self._type = type_of_parrot
        self._number_of_coconuts = number_of_coconuts
        self._voltage = voltage
        self._nailed = nailed

    def cry(self) -> str:
        match self._type:
            case ParrotType.EUROPEAN:
                return "Sqoork!"
            case ParrotType.AFRICAN:
                return "Sqaark!"
            case ParrotType.NORWEGIAN_BLUE:
                return "Bzzzzzz" if self._voltage > 0 else "..."

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])

    @staticmethod
    def _base_speed():
        return 12.0
