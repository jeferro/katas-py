class Yatzy:

    DICE_VALUES = [6, 5, 4, 3, 2, 1]

    @staticmethod
    def _calculate_dice_frequencies(dice):
        dice_frequencies = {i: 0 for i in Yatzy.DICE_VALUES}

        for die in dice:
            dice_frequencies[die] += 1

        return dice_frequencies

    @staticmethod
    def score_change(dice) -> int:
        # chance sums the dice
        return sum(dice)

    @staticmethod
    def score_yatzy(dice) -> int:
        dice_frequencies = Yatzy._calculate_dice_frequencies(dice)

        # score for yatzy if all dice are the same
        yatzy_result = 0
        if 5 in dice_frequencies.values():
            yatzy_result = 50

        return yatzy_result

    @staticmethod
    def score_ones(dice) -> int:
        # sum all the ones
        dice_frequencies = Yatzy._calculate_dice_frequencies(dice)

        return dice_frequencies[1]

    @staticmethod
    def score_twos(dice) -> int:
        # sum all the twos
        dice_frequencies = Yatzy._calculate_dice_frequencies(dice)

        return dice_frequencies[2] * 2

    @staticmethod
    def score_threes(dice) -> int:
        # sum all the threes
        dice_frequencies = Yatzy._calculate_dice_frequencies(dice)

        return dice_frequencies[3] * 3

    @staticmethod
    def score_fours(dice) -> int:
        # sum all the fours
        dice_frequencies = Yatzy._calculate_dice_frequencies(dice)

        return dice_frequencies[4] * 4

    @staticmethod
    def score_fives(dice) -> int:
        # sum all the fives
        dice_frequencies = Yatzy._calculate_dice_frequencies(dice)

        return dice_frequencies[5] * 5


    @staticmethod
    def score_sixes(dice) -> int:
        # sum all the sixes
        dice_frequencies = Yatzy._calculate_dice_frequencies(dice)

        return dice_frequencies[6] * 6

    @staticmethod
    def score_pair(dice) -> int:
        dice_frequencies = Yatzy._calculate_dice_frequencies(dice)

        # score pair if two dice are the same
        pair_result = 0
        # score highest pair if there is more than one
        for i in Yatzy.DICE_VALUES:
            if dice_frequencies[i] >= 2:
                pair_result = i * 2
                break

        return pair_result

    @staticmethod
    def score_two_pair(dice) -> int:
        dice_frequencies = Yatzy._calculate_dice_frequencies(dice)

        # score if there are two pairs
        two_pair_result = 0
        pair_count = 0
        for frequency in dice_frequencies.values():
            if frequency >= 2:
                pair_count += 1

        if pair_count == 2:
            for i in Yatzy.DICE_VALUES:
                if dice_frequencies[i] >= 2:
                    two_pair_result += i * 2

        return two_pair_result

    @staticmethod
    def score_three_of_a_kind(dice) -> int:
        dice_frequencies = Yatzy._calculate_dice_frequencies(dice)

        # score if three dice are the same
        three_kind_result = 0
        for i in Yatzy.DICE_VALUES:
            if dice_frequencies[i] >= 3:
                three_kind_result = i * 3

        return three_kind_result

    @staticmethod
    def score_four_a_kind(dice) -> int:
        dice_frequencies = Yatzy._calculate_dice_frequencies(dice)

        # score if four dice are the same
        four_kind_result = 0
        for i in Yatzy.DICE_VALUES:
            if dice_frequencies[i] >= 4:
                four_kind_result = i * 4

        return four_kind_result

    @staticmethod
    def score_small_straight(dice) -> int:
        dice_frequencies = Yatzy._calculate_dice_frequencies(dice)

        # score if dice contains 1,2,3,4,5
        small_straight_result = 0

        count = 0
        for frequency in dice_frequencies.values():
            if frequency == 1:
                count += 1

        if count == 5 and dice_frequencies[6] == 0:
            for die in dice:
                small_straight_result += die

        return small_straight_result

    @staticmethod
    def score_large_straight(dice) -> int:
        dice_frequencies = Yatzy._calculate_dice_frequencies(dice)

        # score if dice contains 2,3,4,5,6
        large_straight_result = 0
        straight_count = 0
        for frequency in dice_frequencies.values():
            if frequency == 1:
                straight_count += 1

        if straight_count == 5 and dice_frequencies[1] == 0:
            for die in dice:
                large_straight_result += die

        return large_straight_result

    @staticmethod
    def score_full_house(dice) -> int:
        dice_frequencies = Yatzy._calculate_dice_frequencies(dice)

        # score if there is a pair as well as three of a kind
        full_house_result = 0
        if 2 in dice_frequencies.values() and 3 in dice_frequencies.values():
            for die in dice:
                full_house_result += die

        return full_house_result
