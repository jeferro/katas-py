from src.yearly_vacation.contract import Contract


class NormalContract(Contract):

    def __init__(self):
        super().__init__()

    def calculate_num_vacation(self):
        return 24
