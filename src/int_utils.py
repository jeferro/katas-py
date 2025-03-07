from typing import List


class IntUtils:

    @staticmethod
    def sum(values: List[int]):
        result = 0

        for value in values:
            result = result + value

        return result