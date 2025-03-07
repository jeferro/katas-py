from enum import Enum


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class Parrot:

    def __init__(self,
                 voltage: float,
                 nailed: bool):
        self._voltage = voltage
        self._nailed = nailed

    @staticmethod
    def _base_speed():
        return 12.0
