from src.parrot import Parrot


class EuropeanParrot(Parrot):

    def __init__(self):
        super().__init__()

    @staticmethod
    def create_of(voltage: float):
        return EuropeanParrot()

    def speed(self) -> float:
        return self._base_speed()

    def cry(self) -> str:
        return "Sqoork!"
