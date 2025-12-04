from src.yearly_vacation.contract import Contract
from datetime import date


class NormalContract(Contract):

    def __init__(self,
                 start_date: date):
        super().__init__(start_date)

    def num_vacation_days(self,
                          a_date: date):
        today = date.today()

        if a_date.year == today.year:
            return a_date.month

        return 24
