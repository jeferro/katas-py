from src.parrot import Parrot, ParrotType


class AfricanParrot(Parrot):

    def __init__(self, number_of_coconuts: float, voltage: float, nailed: bool):
        super().__init__(ParrotType.AFRICAN, number_of_coconuts, voltage, nailed)