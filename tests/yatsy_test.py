from src.yatzy import Yatzy
from src.yatzy_category import YatzyCategory


def test_chance_scores_sum_of_all_dice():
    assert (15 == score_change([2, 3, 4, 5, 1]))
    assert (16 == score_change([3, 3, 4, 5, 1]))


def score_change(dice):
    return Yatzy().score(dice, YatzyCategory.CHANCE)


def test_yatzy_scores_50():
    assert (50 == score_yatzy([4, 4, 4, 4, 4]))
    assert (50 == score_yatzy([6, 6, 6, 6, 6]))
    assert (0 == score_yatzy([6, 6, 6, 6, 3]))


def score_yatzy(dice):
    return Yatzy().score(dice, YatzyCategory.YATZY)


def test_test_1s():
    assert (1 == score_ones([1, 2, 3, 4, 5]))
    assert (2 == score_ones([1, 2, 1, 4, 5]))
    assert (0 == score_ones([6, 2, 2, 4, 5]))
    assert (4 == score_ones([1, 2, 1, 1, 1]))


def score_ones(dice):
    return Yatzy().score(dice, YatzyCategory.ONES)


def test_twos():
    assert (4 == score_twos([1, 2, 3, 2, 6]))
    assert (10 == score_twos([2, 2, 2, 2, 2]))


def score_twos(dice):
    return Yatzy().score(dice, YatzyCategory.TWOS)


def test_threes():
    assert (6 == score_threes([1, 2, 3, 2, 3]))
    assert (12 == score_threes([2, 3, 3, 3, 3]))


def score_threes(dice):
    return Yatzy().score(dice, YatzyCategory.THREES)


def test_fours():
    assert (12 == score_fours([4, 4, 4, 5, 5]))
    assert (8 == score_fours([4, 4, 5, 5, 5]))
    assert (4 == score_fours([4, 5, 5, 5, 5]))


def score_fours(dice):
    return Yatzy().score(dice, YatzyCategory.FOURS)


def test_fives():
    assert (10 == score_fives([4, 4, 4, 5, 5]))
    assert (15 == score_fives([4, 4, 5, 5, 5]))
    assert (20 == score_fives([4, 5, 5, 5, 5]))


def score_fives(dice):
    return Yatzy().score(dice, YatzyCategory.FIVES)


def test_sixes():
    assert (0 == score_sixes([4, 4, 4, 5, 5]))
    assert (6 == score_sixes([4, 4, 6, 5, 5]))
    assert (18 == score_sixes([6, 5, 6, 6, 5]))


def score_sixes(dice):
    return Yatzy().score(dice, YatzyCategory.SIXES)


def test_pair():
    assert (6 == score_pair([3, 4, 3, 5, 6]))
    assert (10 == score_pair([5, 3, 3, 3, 5]))
    assert (12 == score_pair([5, 3, 6, 6, 5]))


def score_pair(dice):
    return Yatzy().score(dice, YatzyCategory.PAIR)


def test_two_pair():
    assert (16 == score_two_pair([3, 3, 5, 4, 5]))
    assert (16 == score_two_pair([3, 3, 5, 5, 5]))


def score_two_pair(dice):
    return Yatzy().score(dice, YatzyCategory.TWO_PAIRS)


def test_three_of_a_kind():
    assert (9 == score_three_of_a_kind([3, 3, 3, 4, 5]))
    assert (15 == score_three_of_a_kind([5, 3, 5, 4, 5]))
    assert (9 == score_three_of_a_kind([3, 3, 3, 3, 5]))


def score_three_of_a_kind(dice):
    return Yatzy().score(dice, YatzyCategory.THREE_OF_A_KIND)


def test_four_of_a_knd():
    assert (12 == score_four_a_kind([3, 3, 3, 3, 5]))
    assert (20 == score_four_a_kind([5, 5, 5, 4, 5]))
    assert (12 == score_four_a_kind([3, 3, 3, 3, 3]))


def score_four_a_kind(dice):
    return Yatzy().score(dice, YatzyCategory.FOUR_OF_A_KIND)


def test_small_straight():
    assert (15 == score_small_straight([1, 2, 3, 4, 5]))
    assert (15 == score_small_straight([2, 3, 4, 5, 1]))
    assert (0 == score_small_straight([1, 2, 2, 4, 5]))


def score_small_straight(dice):
    return Yatzy().score(dice, YatzyCategory.SMALL_STRAIGHT)


def test_large_straight():
    assert (20 == score_straight([6, 2, 3, 4, 5]))
    assert (20 == score_straight([2, 3, 4, 5, 6]))
    assert (0 == score_straight([1, 2, 2, 4, 5]))


def score_straight(dice):
    return Yatzy().score(dice, YatzyCategory.LARGE_STRAIGHT)


def test_full_house():
    assert (18 == score_full_house([6, 2, 2, 2, 6]))
    assert (0 == score_full_house([2, 3, 4, 5, 6]))


def score_full_house(dice):
    return Yatzy().score(dice, YatzyCategory.FULL_HOUSE)
