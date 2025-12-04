from src.yearly_vacation.contract import Contract
from datetime import date


class NormalContract(Contract):

    def __init__(self,
                 start_date: date):
        super().__init__(start_date)

    def num_vacation_days(self,
                          a_date: date):
        if self._start_at_same_year(a_date):
            return a_date.month

        additional_vacation_days = self._calculate_additional_vacation_days(a_date)

        return 24 + additional_vacation_days

    def _start_at_same_year(self,
                            a_date: date) -> bool:
        return a_date.year == self.start_date.year

    def _calculate_additional_vacation_days(self,
                                            a_date: date):
        diff = a_date - self.start_date

        diff_years = diff.days // 365

        if diff_years < 6:
            return 0

        if diff_years > 6:
            return 6

        return diff_years
