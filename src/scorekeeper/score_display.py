from src.scorekeeper.observer import Observer


class ScoreDisplay(Observer):

    def __init__(self):
        self.score = "000:000"

    def get_score(self) -> str:
        return self.score

    def update(self, score_a, score_b):
        score_a = self._format_score(score_a)
        score_b = self._format_score(score_b)
        self.score = f"{score_a}:{score_b}"

    @staticmethod
    def _format_score(score) -> str:
        return str(score).zfill(3)
