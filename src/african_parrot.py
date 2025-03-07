from src.parrot import Parrot

LOAD_FACTOR = 9.0


class AfricanParrot(Parrot):

    def __init__(self, voltage: float, number_of_coconuts: float):
        super().__init__()

        self._voltage = voltage
        self._number_of_coconuts = number_of_coconuts

    @staticmethod
    def create_of(number_of_coconuts: float,
                  voltage: float):
        return AfricanParrot(voltage, number_of_coconuts)

    def speed(self) -> float:
        return max(0.0, self._base_speed() - LOAD_FACTOR * self._number_of_coconuts)

    def cry(self) -> str:
        return "Sqaark!"