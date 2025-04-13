from src.frame import Frame
from typing import List


class Bowling(object):

    def __init__(self):
        self.frames: List[Frame] = []

        self.active_frame = 0

    def roll(self,
             knocked_pins: int):
        if len(self.frames) > self.active_frame:
            current_frame = self.frames[self.active_frame]
        else:
            current_frame = Frame()

            self.frames.append(current_frame)

        current_frame.roll(knocked_pins)

    def score(self) -> int:
        total = 0

        for frame in self.frames:
            total += frame.score()

        return total
