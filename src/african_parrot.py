from src.parrot import Parrot, ParrotType


class AfricanParrot(Parrot):

    def __init__(self, voltage: float, number_of_coconuts: float):
        super().__init__(voltage)

        self._number_of_coconuts = number_of_coconuts

    def speed(self) -> float:
        return max(0.0, self._base_speed() - self._load_factor() * self._number_of_coconuts)

    @staticmethod
    def _load_factor():
        return 9.0

    def cry(self) -> str:
        return "Sqaark!"