from src.alarm import Alarm
from tests.stub_sensonr import StubSensor


def test_alarm_is_off_by_default():
    stub_sensor = StubSensor(10.0)
    alarm = Alarm(stub_sensor)

    assert not alarm.is_alarm_on

def test_should_alarm_when_pressure_is_equals_to_or_less_than_17():
    stub_sensor = StubSensor(16.0)
    alarm = Alarm(stub_sensor)

    alarm.check()

    assert alarm.is_alarm_on

def test_should_alarm_when_pressure_is_equals_to_or_greater_than_21():
    stub_sensor = StubSensor(22.0)
    alarm = Alarm(stub_sensor)

    alarm.check()

    assert alarm.is_alarm_on

def test_should_not_alarm_when_pressure_is_18():
    stub_sensor = StubSensor(18.0)
    alarm = Alarm(stub_sensor)

    alarm.check()

    assert not alarm.is_alarm_on
