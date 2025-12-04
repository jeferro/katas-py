
from src.yearly_vacation.normal_contract import NormalContract


def test_24_days_on_normal_contract():
    contract = NormalContract()
    num_vacations = contract.calculate_num_vacation()
    assert num_vacations == 24

