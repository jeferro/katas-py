from src.frame import Frame
from typing import List


class Bowling(object):

    MAX_FRAMES = 10

    def __init__(self):
        self.active_frame = 0
        self.frames: List[Frame] = []

        for i in range(0, self.MAX_FRAMES):
            frame = Frame()

            self.frames.append(frame)

    def roll(self,
             knocked_pins: int):
        current_frame = self.frames[self.active_frame]
        previous_frame = None if self.active_frame == 0 else self.frames[self.active_frame - 1]

        current_frame.roll(knocked_pins)

        if previous_frame \
            and previous_frame.is_square() \
            and current_frame.is_first_attempt():
            previous_frame.add_bonus(knocked_pins)

        if current_frame.is_completed():
            self.active_frame += 1

    def score(self) -> int:
        total = 0

        for frame in self.frames:
            total += frame.score()

        return total
