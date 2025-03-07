from src.parrot import Parrot, ParrotType


class NorwegianBlueParrot(Parrot):

    def __init__(self, number_of_coconuts: float, voltage: float, nailed: bool):
        super().__init__(ParrotType.NORWEGIAN_BLUE, number_of_coconuts, voltage, nailed)