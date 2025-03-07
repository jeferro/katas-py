from src.parrot import Parrot


class EuropeanParrot(Parrot):

    def __init__(self, voltage: float):
        super().__init__(voltage)

    @staticmethod
    def create_of(voltage: float):
        return EuropeanParrot(voltage)

    def speed(self) -> float:
        return self._base_speed()

    def cry(self) -> str:
        return "Sqoork!"
