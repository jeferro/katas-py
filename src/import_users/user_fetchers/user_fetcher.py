
from abc import ABC, abstractmethod

class UserFetcher(ABC):

    @abstractmethod
    def fetch(self) -> list[list[str]]:
        pass
