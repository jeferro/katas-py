from typing import List


class StringCalculator:

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        values = numbers.replace(f'\n', ',').split(",")

        return self._sum_values(values)

    @staticmethod
    def _sum_values(values: List[str]) -> int:
        result = 0

        for value in values:
            result = result + int(value)

        return result