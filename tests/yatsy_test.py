from src.yatzy import Yatzy


def test_chance_scores_sum_of_all_dice():
    assert (15 == Yatzy.score_change([2, 3, 4, 5, 1]))
    assert (16 == Yatzy.score_change([3, 3, 4, 5, 1]))


def test_yatzy_scores_50():
    assert (50 == Yatzy.score_yatzy([4, 4, 4, 4, 4]))
    assert (50 == Yatzy.score_yatzy([6, 6, 6, 6, 6]))
    assert (0 == Yatzy.score_yatzy([6, 6, 6, 6, 3]))


def test_test_1s():
    assert (1 == Yatzy.score_ones([1, 2, 3, 4, 5]))
    assert (2 == Yatzy.score_ones([1, 2, 1, 4, 5]))
    assert (0 == Yatzy.score_ones([6, 2, 2, 4, 5]))
    assert (4 == Yatzy.score_ones([1, 2, 1, 1, 1]))


def test_twos():
    assert (4 == Yatzy.score_twos([1, 2, 3, 2, 6]))
    assert (10 == Yatzy.score_twos([2, 2, 2, 2, 2]))


def test_threes():
    assert (6 == Yatzy.score_threes([1, 2, 3, 2, 3]))
    assert (12 == Yatzy.score_threes([2, 3, 3, 3, 3]))


def test_fours():
    assert (12 == Yatzy.score_fours([4, 4, 4, 5, 5]))
    assert (8 == Yatzy.score_fours([4, 4, 5, 5, 5]))
    assert (4 == Yatzy.score_fours([4, 5, 5, 5, 5]))


def test_fives():
    assert (10 == Yatzy.score_fives([4, 4, 4, 5, 5]))
    assert (15 == Yatzy.score_fives([4, 4, 5, 5, 5]))
    assert (20 == Yatzy.score_fives([4, 5, 5, 5, 5]))


def test_sixes():
    assert (0 == Yatzy.score_sixes([4, 4, 4, 5, 5]))
    assert (6 == Yatzy.score_sixes([4, 4, 6, 5, 5]))
    assert (18 == Yatzy.score_sixes([6, 5, 6, 6, 5]))


def test_pair():
    assert (6 == Yatzy.score_pair([3, 4, 3, 5, 6]))
    assert (10 == Yatzy.score_pair([5, 3, 3, 3, 5]))
    assert (12 == Yatzy.score_pair([5, 3, 6, 6, 5]))


def test_two_pair():
    assert (16 == Yatzy.score_two_pair([3, 3, 5, 4, 5]))
    assert (16 == Yatzy.score_two_pair([3, 3, 5, 5, 5]))


def test_three_of_a_kind():
    assert (9 == Yatzy.score_three_of_a_kind([3, 3, 3, 4, 5]))
    assert (15 == Yatzy.score_three_of_a_kind([5, 3, 5, 4, 5]))
    assert (9 == Yatzy.score_three_of_a_kind([3, 3, 3, 3, 5]))


def test_four_of_a_knd():
    assert (12 == Yatzy.score_four_a_kind([3, 3, 3, 3, 5]))
    assert (20 == Yatzy.score_four_a_kind([5, 5, 5, 4, 5]))
    assert (12 == Yatzy.score_four_a_kind([3, 3, 3, 3, 3]))


def test_small_straight():
    assert (15 == Yatzy.score_small_straight([1, 2, 3, 4, 5]))
    assert (15 == Yatzy.score_small_straight([2, 3, 4, 5, 1]))
    assert (0 == Yatzy.score_small_straight([1, 2, 2, 4, 5]))


def test_large_straight():
    assert (20 == Yatzy.score_large_straight([6, 2, 3, 4, 5]))
    assert (20 == Yatzy.score_large_straight([2, 3, 4, 5, 6]))
    assert (0 == Yatzy.score_large_straight([1, 2, 2, 4, 5]))


def test_full_house():
    assert (18 == Yatzy.score_full_house([6, 2, 2, 2, 6]))
    assert (0 == Yatzy.score_full_house([2, 3, 4, 5, 6]))


