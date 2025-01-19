from src.sensor import Sensor


class StubSensor(Sensor):

    def __init__(self,
                 value: float):
        super().__init__()
        self.value = value


    def pop_next_pressure_psi_value(self) -> float:
        return self.value

