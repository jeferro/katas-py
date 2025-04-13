
class Frame:

    def __init__(self):
        self.first_attempt = None
        self.second_attempt = None

        self.bonus = 0

    def roll(self,
             knocked_pins: int):
        if self.first_attempt is None:
            self.first_attempt = knocked_pins
            return

        if self.second_attempt is None:
            self.second_attempt = knocked_pins

    def add_bonus(self,
                  bonus: int):
        self.bonus = bonus

    def score(self):
        if self.is_completed():
            return self.first_attempt + self.second_attempt + self.bonus

        if self.first_attempt:
            return self.first_attempt

        return 0

    def is_completed(self) -> bool:
        return True if self.first_attempt and self.second_attempt else False

    def is_first_attempt(self) -> bool:
        return True if self.first_attempt and not self.second_attempt else False

    def is_square(self) -> bool:
        return True if self.score() == 10 and self.second_attempt else False
