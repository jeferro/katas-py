from enum import Enum


class ParrotType(Enum):
    EUROPEAN = 1
    AFRICAN = 2
    NORWEGIAN_BLUE = 3


class Parrot:

    def __init__(self,
                 voltage: float):
        self._voltage = voltage

    @staticmethod
    def _base_speed():
        return 12.0
