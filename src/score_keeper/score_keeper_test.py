from src.score_keeper.score_display import ScoreDisplay
from src.score_keeper.score_keeper import ScoreKeeper


def test_it_reports_score():
    score_keeper = ScoreKeeper()

    score_display = ScoreDisplay()
    score_keeper.register(score_display)

    assert score_display.get_score() == "000:000"

def test_it_add_score_1_to_team_a():
    score_keeper = ScoreKeeper()

    score_display = ScoreDisplay()
    score_keeper.register(score_display)

    score_keeper.score_team_a1()

    assert score_display.get_score() == "001:000"

def test_it_add_score_2_to_team_a():
    score_keeper = ScoreKeeper()

    score_display = ScoreDisplay()
    score_keeper.register(score_display)

    score_keeper.score_team_a2()

    assert score_display.get_score() == "002:000"

def test_it_add_score_3_to_team_a():
    score_keeper = ScoreKeeper()

    score_display = ScoreDisplay()
    score_keeper.register(score_display)

    score_keeper.score_team_a3()

    assert score_display.get_score() == "003:000"

def test_it_add_score_1_to_team_b():
    score_keeper = ScoreKeeper()

    score_display = ScoreDisplay()
    score_keeper.register(score_display)

    score_keeper.score_team_b1()

    assert score_display.get_score() == "000:001"

def test_it_add_score_2_to_team_b():
    score_keeper = ScoreKeeper()

    score_display = ScoreDisplay()
    score_keeper.register(score_display)

    score_keeper.score_team_b2()

    assert score_display.get_score() == "000:002"

def test_it_add_score_3_to_team_b():
    score_keeper = ScoreKeeper()

    score_display = ScoreDisplay()
    score_keeper.register(score_display)

    score_keeper.score_team_b3()

    assert score_display.get_score() == "000:003"

def test_it_notifies_score_changes():
    score_keeper = ScoreKeeper()

    score_display = ScoreDisplay()
    score_keeper.register(score_display)

    score_keeper.score_team_a1()

    assert score_display.get_score() == "001:000"


def test_it_notifies_team_b_score_changes():
    score_keeper = ScoreKeeper()

    score_display = ScoreDisplay()
    score_keeper.register(score_display)

    score_keeper.score_team_b1()

    assert score_display.get_score() == "000:001"