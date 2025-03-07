from src.parrot import Parrot, ParrotType


class AfricanParrot(Parrot):

    def __init__(self, number_of_coconuts: float, voltage: float, nailed: bool):
        super().__init__(ParrotType.AFRICAN, number_of_coconuts, voltage, nailed)

    def speed(self) -> float:
        return max(0.0, self._base_speed() - self._load_factor() * self._number_of_coconuts)

    @staticmethod
    def _load_factor():
        return 9.0