from src.african_parrot import AfricanParrot
from src.european_parrot import EuropeanParrot
from src.norwegian_blue_parrot import NorwegianBlueParrot
from src.parrot import ParrotType


def create_parrot(type_of_parrot: ParrotType.EUROPEAN,
                  number_of_coconuts: float,
                  voltage: float,
                  nailed: bool):
    match type_of_parrot:
        case ParrotType.EUROPEAN:
            return EuropeanParrot(voltage, nailed)
        case ParrotType.AFRICAN:
            return AfricanParrot(number_of_coconuts, voltage, nailed)
        case ParrotType.NORWEGIAN_BLUE:
            return NorwegianBlueParrot(voltage, nailed)
        case ParrotType.EUROPEAN:
            raise ValueError(f'Unknown parrot: {type_of_parrot}')