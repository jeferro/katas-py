from src.score_display import ScoreDisplay


def test_it_reports_the_initial_score():
    display = ScoreDisplay()
    result = display.get_score()
    assert result == "000:000"

def test_it_updates_with_zero_numbers():
    display = ScoreDisplay()

    display.update(0, 0)

    result = display.get_score()
    assert result == "000:000"

def test_it_updates_score_a():
    display = ScoreDisplay()

    display.update(1, 0)

    result = display.get_score()
    assert result == "001:000"

def test_it_updates_score_b():
    display = ScoreDisplay()

    display.update(0, 1)

    result = display.get_score()
    assert result == "000:001"