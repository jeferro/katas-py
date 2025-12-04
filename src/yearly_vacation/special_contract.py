from src.yearly_vacation.contract import Contract


class SpecialContract(Contract):

    def __init__(self,
                 vacation_days: int):
        super().__init__()

        self.vacation_days = vacation_days

    def num_vacation_days(self):
        return self.vacation_days
