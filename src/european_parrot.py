from src.parrot import Parrot, ParrotType


class EuropeanParrot(Parrot):

    def __init__(self, voltage: float):
        super().__init__(voltage)

    def speed(self) -> float:
        return self._base_speed()

    def cry(self) -> str:
        return "Sqoork!"
