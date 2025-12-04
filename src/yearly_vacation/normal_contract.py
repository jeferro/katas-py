from src.yearly_vacation.contract import Contract
from datetime import date

MAX_ADDITIONAL_AGE_VACATION_DAYS = 2

MAX_ADDITIONAL_SENIORITY_VACATION_DAYS = 6

MINIMAL_SENIORITY = 6

DEFAULT_VACATION_DAYS = 24


class NormalContract(Contract):

    def __init__(self,
                 name: str,
                 birthday: date,
                 start_date: date):
        super().__init__(name,
                         birthday,
                         start_date)

    def num_vacation_days(self,
                          a_date: date):
        if self._start_at_same_year(a_date):
            return a_date.month

        seniority_years = self._calculate_seniority_years(a_date)

        if seniority_years < MINIMAL_SENIORITY:
            return DEFAULT_VACATION_DAYS

        is_older_than_40_years = self._is_older_than_40_years(a_date)

        additional_seniority_vacation_days = seniority_years

        if additional_seniority_vacation_days > MAX_ADDITIONAL_SENIORITY_VACATION_DAYS:
            additional_seniority_vacation_days = MAX_ADDITIONAL_SENIORITY_VACATION_DAYS

        additional_age_vacation_days = 0

        if is_older_than_40_years:
            additional_age_vacation_days = seniority_years // 5

            if additional_age_vacation_days > MAX_ADDITIONAL_AGE_VACATION_DAYS:
                additional_age_vacation_days = MAX_ADDITIONAL_AGE_VACATION_DAYS

        return DEFAULT_VACATION_DAYS + additional_seniority_vacation_days + additional_age_vacation_days

    def _start_at_same_year(self,
                            a_date: date) -> bool:
        return a_date.year == self.start_date.year

    def _calculate_seniority_years(self,
                                   a_date: date) -> int:
        diff = a_date - self.start_date

        return diff.days // 365

    def _is_older_than_40_years(self,
                             a_date: date) -> bool:
        diff = a_date - self.birthday

        age = diff.days // 365

        return age >= 40
