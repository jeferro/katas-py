
from src.yearly_vacation.normal_contract import NormalContract
from src.yearly_vacation.special_contract import SpecialContract


def test_24_days_on_normal_contract():
    normal_contract = NormalContract()
    assert normal_contract.num_vacation_days() == 24

def test_special_contract_can_override_vacation_days():
    custom_vacation_days = 36
    special_contract = SpecialContract(custom_vacation_days)
    assert special_contract.num_vacation_days() == custom_vacation_days
