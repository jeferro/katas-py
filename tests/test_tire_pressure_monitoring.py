
from tests.stub_alarm import StubAlarm


def test_alarm_is_off_by_default():
    stub_alarm = StubAlarm(10.0)

    assert not stub_alarm.is_alarm_on

def test_should_alarm_when_pressure_is_equals_to_or_less_than_or_e_16():
    stub_alarm = StubAlarm(16.0)

    stub_alarm.check()

    assert stub_alarm.is_alarm_on

def test_should_alarm_when_pressure_is_equals_to_or_greater_than_22():
    stub_alarm = StubAlarm(22.0)

    stub_alarm.check()

    assert stub_alarm.is_alarm_on

def test_should_not_alarm_when_pressure_is_18():
    stub_alarm = StubAlarm(18.0)

    stub_alarm.check()

    assert not stub_alarm.is_alarm_on
