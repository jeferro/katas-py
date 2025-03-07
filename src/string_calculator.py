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
        if not self._is_delimiter_declared(numbers_str):
            return self._map_values_using_delimiter(numbers_str, DEFAULT_DELIMITER)

        delimiter = self._map_delimiter(numbers_str)
        numbers_without_delimiter_line = self._remove_delimiter_line(delimiter, numbers_str)

        return self._map_values_using_delimiter(numbers_without_delimiter_line, delimiter)

    @staticmethod
    def _is_delimiter_declared(numbers_str: str) -> bool:
        return numbers_str.startswith("//")

    @staticmethod
    def _map_delimiter(numbers_str) -> str:
        first_line: str = numbers_str.split("\n")[0]

        if first_line.startswith("//["):
            matches = re.search('^//\[(.+)]', first_line)
        else:
            matches = re.search('^//(.{1})', first_line)

        return matches.group(1)

    def _remove_delimiter_line(self,
                               delimiter:str,
                               numbers_str: str):

        if len(delimiter) == 1:
            return numbers_str.replace(f'//{delimiter}\n', '')
        else:
            return numbers_str.replace(f'//[{delimiter}]\n', '')

    @staticmethod
    def _map_values_using_delimiter(numbers_str: str,
                                    delimiter: str) -> List[int]:
        split = numbers_str.replace(f'\n', delimiter) \
            .split(delimiter)

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
