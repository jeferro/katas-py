import random

from src.sensor import Sensor


class RandomSensor(Sensor):

    # The reading of the pressure value from the sensor is simulated in this implementation.
    # Because the focus of the exercise is on the other class.

    _OFFSET = 16.0
        
    def pop_next_pressure_psi_value(self) -> float:
        pressure_telemetry_value = self._sample_pressure()
        return RandomSensor._OFFSET + pressure_telemetry_value

    @staticmethod
    def _sample_pressure():
        # placeholder implementation that simulate a real sensor in a real tire
        pressure_telemetry_value = 6 * random.random() * random.random()
        return pressure_telemetry_value
