from src.scorekeeper.observer import Observer
from typing import Set

class ScoreKeeper:

    def __init__(self):
        self.observers: Set[Observer] = set()
        self.score_b = 0
        self.score_a = 0

    def get_score(self) -> str:
        score_a = self._format_score(self.score_a)
        score_b = self._format_score(self.score_b)

        return f"{score_a}:{score_b}"

    @staticmethod
    def _format_score(score) -> str:
        return str(score).zfill(3)

    def score_team_a1(self) -> None:
        self._increase_team_a(1)

    def score_team_a2(self) -> None:
        self._increase_team_a(2)

    def score_team_a3(self) -> None:
        self._increase_team_a(3)

    def score_team_b1(self) -> None:
        self._increase_team_b(1)

    def score_team_b2(self) -> None:
        self._increase_team_b(2)

    def score_team_b3(self) -> None:
        self._increase_team_b(3)

    def _increase_team_a(self, increment) -> None:
        self.score_a += increment

        self._notify()

    def _increase_team_b(self, increment) -> None:
        self.score_b += increment

        self._notify()

    def _notify(self) -> None:
        for observer in self.observers:
            observer.update(self.score_a, self.score_b)

    def register(self, observer: Observer) -> None:
        self.observers.add(observer)
