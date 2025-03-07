class Parrot:

    def __init__(self,
                 voltage: float):
        self._voltage = voltage

    @staticmethod
    def _base_speed():
        return 12.0
