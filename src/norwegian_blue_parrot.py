from src.parrot import Parrot

MIN_SPEED = 24.0


class NorwegianBlueParrot(Parrot):

    def __init__(self, voltage: float, nailed: bool):
        super().__init__(voltage)

        self._nailed = nailed

    @staticmethod
    def create_of(voltage: float,
                  nailed: bool):
        return NorwegianBlueParrot(voltage, nailed)

    def speed(self) -> float:
        return 0 if self._nailed else self._compute_base_speed_for_voltage(self._voltage)

    def _compute_base_speed_for_voltage(self, voltage):
        return min([MIN_SPEED, voltage * self._base_speed()])

    def cry(self) -> str:
        return "Bzzzzzz" if self._voltage > 0 else "..."