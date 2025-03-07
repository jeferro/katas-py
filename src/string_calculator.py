import re
from typing import List

from src.int_utils import IntUtils

DEFAULT_DELIMITER = ","


class StringCalculator:

    def add(self, numbers_str: str) -> int:
        if not numbers_str:
            return 0

        numbers = self._map_numbers_str_to_int(numbers_str)

        self._ensure_not_negative_numbers(numbers)

        filtered_numbers = self._filter_huge_numbers(numbers)

        return IntUtils.sum(filtered_numbers)

    def _map_numbers_str_to_int(self, numbers_str) -> List[int]:
        if self._is_not_delimiter_declared(numbers_str):
            return self._map_values_using_delimiter(numbers_str, [DEFAULT_DELIMITER])

        delimiters = self._map_delimiters(numbers_str)
        numbers_without_delimiter_line = self._remove_delimiter_line(numbers_str)

        return self._map_values_using_delimiter(numbers_without_delimiter_line, delimiters)

    @staticmethod
    def _is_not_delimiter_declared(numbers_str: str) -> bool:
        return not numbers_str.startswith("//")

    @staticmethod
    def _map_delimiters(numbers_str) -> List[str]:
        first_line: str = numbers_str.split("\n")[0]

        if first_line.startswith("//["):
            matches = re.search('^//\[(.+)]', first_line)
        else:
            matches = re.search('^//(.{1})', first_line)

        return matches.group(1).replace("[", "").split("]")

    @staticmethod
    def _remove_delimiter_line(numbers_str: str) -> str:
        index = numbers_str.index("\n") + 1

        return numbers_str[index:]

    @staticmethod
    def _map_values_using_delimiter(numbers_str: str,
                                    delimiters: List[str]) -> List[int]:
        first_delimiter = delimiters[0]
        other_delimiters = delimiters[1:]

        numbers_str = numbers_str.replace(f'\n', first_delimiter)

        for other_delimiter in other_delimiters:
            numbers_str = numbers_str.replace(other_delimiter, first_delimiter)

        split = numbers_str.split(first_delimiter)

        numbers = []

        for item in split:
            numbers.append(int(item))

        return numbers

    @staticmethod
    def _ensure_not_negative_numbers(numbers):
        negative_numbers = []

        for number in numbers:
            if number < 0:
                negative_numbers.append(number)

        if negative_numbers:
            raise RuntimeError(f'Invalid negative numbers: {negative_numbers}')

    def _filter_huge_numbers(self, numbers):
        filtered_numbers = []

        for number in numbers:
            if number < 1000:
                filtered_numbers.append(number)

        return filtered_numbers
