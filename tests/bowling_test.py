
from src.bowling import Bowling


def test_score_of_frame():
    bowling = Bowling()
    bowling.roll(1)
    bowling.roll(2)

    assert bowling.score() == 3
