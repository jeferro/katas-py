
from src.yearly_vacation.contract import Contract


def test_24_days_on_normal_contract():
    contract = Contract()
    num_vacations = contract.calculate_num_vacation()
    assert num_vacations == 24

