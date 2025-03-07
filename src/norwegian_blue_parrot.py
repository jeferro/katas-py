from src.parrot import Parrot, ParrotType


class NorwegianBlueParrot(Parrot):

    def __init__(self, voltage: float, nailed: bool):
        super().__init__(voltage, nailed)

    def speed(self) -> float:
        return 0 if self._nailed else self._compute_base_speed_for_voltage(self._voltage)

    def _compute_base_speed_for_voltage(self, voltage):
        return min([24.0, voltage * self._base_speed()])

    def cry(self) -> str:
        return "Bzzzzzz" if self._voltage > 0 else "..."