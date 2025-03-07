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

    @staticmethod
    def create_parrot(type_of_parrot: ParrotType.EUROPEAN,
                 number_of_coconuts: float,
                 voltage: float,
                 nailed: bool):
        match type_of_parrot:
            case ParrotType.EUROPEAN:
                return Parrot(ParrotType.EUROPEAN, number_of_coconuts, voltage, nailed)
            case ParrotType.AFRICAN:
                return Parrot(ParrotType.AFRICAN, number_of_coconuts, voltage, nailed)
            case ParrotType.NORWEGIAN_BLUE:
                return Parrot(ParrotType.NORWEGIAN_BLUE, number_of_coconuts, voltage, nailed)
            case ParrotType.EUROPEAN:
                raise ValueError(f'Unknown parrot: {type_of_parrot}')


    def speed(self) -> float:
        match self._type:
            case ParrotType.EUROPEAN:
                return self._base_speed()
            case ParrotType.AFRICAN:
                return max(0.0, self._base_speed() - self._load_factor() * self._number_of_coconuts)
            case ParrotType.NORWEGIAN_BLUE:
                return 0 if self._nailed else self._compute_base_speed_for_voltage(self._voltage)

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

    @staticmethod
    def _load_factor():
        return 9.0
