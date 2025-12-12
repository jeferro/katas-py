
from src.bowling.bowling import Bowling


def test_score_of_frame():
    bowling = Bowling()
    bowling.roll(1)
    bowling.roll(2)

    assert bowling.score() == 3


def test_score_several_frames():
    bowling = Bowling()
    bowling.roll(1)
    bowling.roll(2)

    bowling.roll(7)
    bowling.roll(1)

    assert bowling.score() == 11


def test_square():
    bowling = Bowling()
    bowling.roll(7)
    bowling.roll(3)

    bowling.roll(4)
    bowling.roll(5)

    assert bowling.score() == 23


def test_strike():
    bowling = Bowling()
    bowling.roll(10)

    bowling.roll(4)
    bowling.roll(5)

    assert bowling.score() == 28
