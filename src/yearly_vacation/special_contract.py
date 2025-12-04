from src.yearly_vacation.contract import Contract
from datetime import date


class SpecialContract(Contract):

    def __init__(self,
                 name: str,
                 start_date: date,
                 vacation_days: int):
        super().__init__(name,
                         start_date)

        self.vacation_days = vacation_days

    def num_vacation_days(self,
                          a_date: date):
        return self.vacation_days
