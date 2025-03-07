from src.sensor import Sensor
from src.random_sensor import RandomSensor

class Alarm(object):

    _LOW_PRESSURE_THRESHOLD = 17.0
    _HIGH_PRESSURE_THRESHOLD = 21.0

    def __init__(self,
                 sensor: Sensor):
        self._sensor = sensor if sensor is not None else RandomSensor()

        self._is_alarm_on = False
        
    def check(self):
        psi_pressure_value = self._sensor.pop_next_pressure_psi_value()

        if psi_pressure_value < self._LOW_PRESSURE_THRESHOLD \
                or self._HIGH_PRESSURE_THRESHOLD < psi_pressure_value:
            self._is_alarm_on = True

    @property
    def is_alarm_on(self) -> bool:
        return self._is_alarm_on
