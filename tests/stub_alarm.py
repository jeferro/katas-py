from src.alarm import Alarm


class StubAlarm(Alarm):

    def __init__(self,
                 value: float):
        super().__init__()
        self.value = value


    def _pop_next_pressure_psi_value(self):
        return self.value

