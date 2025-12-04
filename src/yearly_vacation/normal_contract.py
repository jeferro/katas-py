from src.yearly_vacation.contract import Contract


class NormalContract(Contract):

    def __init__(self):
        super().__init__()

    def num_vacation_days(self):
        return 24
