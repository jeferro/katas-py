
class Frame:

    def __init__(self):
        self.first_attempt = None
        self.second_attempt = None

        self.bonus = 0

    def roll(self,
             knocked_pins: int):
        if not self.first_attempt:
            self.first_attempt = knocked_pins
            return

        if not self.second_attempt:
            self.second_attempt = knocked_pins

    def add_bonus(self,
                  next_frame):
        if not isinstance(next_frame, Frame):
            return

        if self.is_square():
            self.bonus = next_frame.first_attempt

        if self.is_strike():
            self.bonus = next_frame.first_attempt + next_frame.second_attempt

    def score(self):
        if self.second_attempt:
            return self.first_attempt + self.second_attempt + self.bonus

        if self.first_attempt:
            return self.first_attempt + self.bonus

        return 0

    def is_completed(self) -> bool:
        if self.second_attempt:
            return True

        if self.first_attempt == 10:
            return True

        return False

    def is_square(self) -> bool:
        if not self.is_completed():
            return False

        if self.first_attempt == 10:
            return True

        if self.first_attempt + self.second_attempt == 10:
            return True

        return False

    def is_strike(self) -> bool:
        if not self.is_completed():
            return False

        if self.first_attempt == 10:
            return True

        return False

    def is_bonus_necessary(self) -> bool:
        return True if self.is_square() or self.is_strike() else False
