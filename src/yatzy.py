from src.yatzy_category import YatzyCategory



class Yatzy:

    DICE_VALUES = [6, 5, 4, 3, 2, 1]

    def score(self, dice, category: YatzyCategory) -> int:

        # calculate the score
        result = 0
        match category:
            case YatzyCategory.CHANCE:
                # chance sums the dice
                result = sum(dice)

            case YatzyCategory.YATZY:
                dice_frequencies = self.calculate_dice_frequencies(dice)

                # score for yatzy if all dice are the same
                yatzy_result = 0
                if 5 in dice_frequencies.values():
                    yatzy_result = 50

                result = yatzy_result

            case YatzyCategory.ONES:
                # sum all the ones
                dice_frequencies = self.calculate_dice_frequencies(dice)

                result = dice_frequencies[1]

            case YatzyCategory.TWOS:
                # sum all the twos
                dice_frequencies = self.calculate_dice_frequencies(dice)

                result = dice_frequencies[2] * 2

            case YatzyCategory.THREES:
                # sum all the threes
                dice_frequencies = self.calculate_dice_frequencies(dice)

                result = dice_frequencies[3] * 3

            case YatzyCategory.FOURS:
                # sum all the fours
                dice_frequencies = self.calculate_dice_frequencies(dice)

                result = dice_frequencies[4] * 4

            case YatzyCategory.FIVES:
                # sum all the fives
                dice_frequencies = self.calculate_dice_frequencies(dice)

                result = dice_frequencies[5] * 5

            case YatzyCategory.SIXES:
                # sum all the sixes
                dice_frequencies = self.calculate_dice_frequencies(dice)

                result = dice_frequencies[6] * 6

            case YatzyCategory.PAIR:
                dice_frequencies = self.calculate_dice_frequencies(dice)

                # score pair if two dice are the same
                pair_result = 0
                # score highest pair if there is more than one
                for i in self.DICE_VALUES:
                    if dice_frequencies[i] >= 2:
                        pair_result = i * 2
                        break

                result = pair_result

            case YatzyCategory.THREE_OF_A_KIND:
                dice_frequencies = self.calculate_dice_frequencies(dice)

                # score if three dice are the same
                three_kind_result = 0
                for i in self.DICE_VALUES:
                    if dice_frequencies[i] >= 3:
                        three_kind_result = i * 3

                result = three_kind_result

            case YatzyCategory.FOUR_OF_A_KIND:
                dice_frequencies = self.calculate_dice_frequencies(dice)

                # score if four dice are the same
                four_kind_result = 0
                for i in self.DICE_VALUES:
                    if dice_frequencies[i] >= 4:
                        four_kind_result = i * 4

                result = four_kind_result

            case YatzyCategory.SMALL_STRAIGHT:
                dice_frequencies = self.calculate_dice_frequencies(dice)

                # score if dice contains 1,2,3,4,5
                small_straight_result = 0

                count = 0
                for frequency in dice_frequencies.values():
                    if frequency == 1:
                        count += 1

                if count == 5 and dice_frequencies[6] == 0:
                    for die in dice:
                        small_straight_result += die

                result = small_straight_result

            case YatzyCategory.LARGE_STRAIGHT:
                dice_frequencies = self.calculate_dice_frequencies(dice)

                # score if dice contains 2,3,4,5,6
                large_straight_result = 0
                straight_count = 0
                for frequency in dice_frequencies.values():
                    if frequency == 1:
                        straight_count += 1

                if straight_count == 5 and dice_frequencies[1] == 0:
                    for die in dice:
                        large_straight_result += die

                result = large_straight_result

            case YatzyCategory.TWO_PAIRS:
                dice_frequencies = self.calculate_dice_frequencies(dice)

                # score if there are two pairs
                two_pair_result = 0
                pair_count = 0
                for frequency in dice_frequencies.values():
                    if frequency >= 2:
                        pair_count += 1

                if pair_count == 2:
                    for i in self.DICE_VALUES:
                        if dice_frequencies[i] >= 2:
                            two_pair_result += i * 2

                result = two_pair_result

            case YatzyCategory.FULL_HOUSE:
                dice_frequencies = self.calculate_dice_frequencies(dice)

                # score if there is a pair as well as three of a kind
                full_house_result = 0
                if 2 in dice_frequencies.values() and 3 in dice_frequencies.values():
                    for die in dice:
                        full_house_result += die

                result = full_house_result

        return result

    def calculate_dice_frequencies(self, dice):
        dice_frequencies = {i: 0 for i in self.DICE_VALUES}
        for die in dice:
            dice_frequencies[die] += 1
        return dice_frequencies

    @staticmethod
    def score_change(dice):
        yatzy = Yatzy()
        return yatzy.score(dice, YatzyCategory.CHANCE)

    @staticmethod
    def score_yatzy(dice):
        yatzy = Yatzy()
        return yatzy.score(dice, YatzyCategory.YATZY)

    @staticmethod
    def score_ones(dice):
        yatzy = Yatzy()
        return yatzy.score(dice, YatzyCategory.ONES)

    @staticmethod
    def score_twos(dice):
        yatzy = Yatzy()
        return yatzy.score(dice, YatzyCategory.TWOS)

    @staticmethod
    def score_threes(dice):
        yatzy = Yatzy()
        return yatzy.score(dice, YatzyCategory.THREES)

    @staticmethod
    def score_fours(dice):
        yatzy = Yatzy()
        return yatzy.score(dice, YatzyCategory.FOURS)

    @staticmethod
    def score_fives(dice):
        yatzy = Yatzy()
        return yatzy.score(dice, YatzyCategory.FIVES)

    @staticmethod
    def score_sixes(dice):
        yatzy = Yatzy()
        return yatzy.score(dice, YatzyCategory.SIXES)

    @staticmethod
    def score_pair(dice):
        yatzy = Yatzy()
        return yatzy.score(dice, YatzyCategory.PAIR)

    @staticmethod
    def score_two_pair(dice):
        yatzy = Yatzy()
        return yatzy.score(dice, YatzyCategory.TWO_PAIRS)

    @staticmethod
    def score_three_of_a_kind(dice):
        yatzy = Yatzy()
        return yatzy.score(dice, YatzyCategory.THREE_OF_A_KIND)

    @staticmethod
    def score_four_a_kind(dice):
        yatzy = Yatzy()
        return yatzy.score(dice, YatzyCategory.FOUR_OF_A_KIND)

    @staticmethod
    def score_small_straight(dice):
        yatzy = Yatzy()
        return yatzy.score(dice, YatzyCategory.SMALL_STRAIGHT)

    @staticmethod
    def score_straight(dice):
        yatzy = Yatzy()
        return yatzy.score(dice, YatzyCategory.LARGE_STRAIGHT)

    @staticmethod
    def score_full_house(dice):
        yatzy = Yatzy()
        return yatzy.score(dice, YatzyCategory.FULL_HOUSE)
