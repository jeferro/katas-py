import re
from typing import List

from src.int_utils import IntUtils

DEFAULT_DELIMITER = ","
DELIMITER_PATTERN = '^//(.{1})'

class StringCalculator:

    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        int_numbers = self._map_numbers_to_int(numbers)

        return IntUtils.sum(int_numbers)

    def _map_numbers_to_int(self, numbers) -> List[int]:
        if not self._is_delimiter_declared(numbers):
            return self._map_values_using_delimiter(numbers, DEFAULT_DELIMITER)

        delimiter = self._map_delimiter(numbers)
        numbers_without_delimiter = numbers.replace(f'//{delimiter}\n', '')

        return self._map_values_using_delimiter(numbers_without_delimiter, delimiter)

    @staticmethod
    def _is_delimiter_declared(numbers):
        return numbers.startswith("//")

    @staticmethod
    def _map_delimiter(numbers):
        first_line = numbers.split("\n")[0]

        matches = re.search(DELIMITER_PATTERN, first_line)
        return matches.group(1)

    @staticmethod
    def _map_values_using_delimiter(numbers: str,
                                    delimiter: str) -> List[int]:
        split = numbers.replace(f'\n', delimiter) \
            .split(delimiter)

        result = []

        for item in split:
            result.append(int(item))

        return result
