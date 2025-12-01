from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, score_a, score_b):
        pass
