
from datetime import date

from src.yearly_vacation.normal_contract import NormalContract
from src.yearly_vacation.special_contract import SpecialContract


def test_24_days_on_normal_contract():
    start_date = date.fromisoformat('2021-01-01')

    normal_contract = NormalContract(start_date)

    test_date = date.fromisoformat('2021-01-06')
    assert normal_contract.num_vacation_days(test_date) == 24

def test_special_contract_can_override_vacation_days():
    start_date = date.fromisoformat('2021-01-01')
    custom_vacation_days = 36

    special_contract = SpecialContract(start_date,
                                       custom_vacation_days)

    test_date = date.fromisoformat('2021-01-06')
    assert special_contract.num_vacation_days(test_date) == custom_vacation_days


def test_in_contract_which_starts_at_current_year_have_vacation_days_similar_to_number_of_months():
    today = date.today()
    begin_of_year = date.fromisoformat(f'{today.year}-01-01')

    normal_contract = NormalContract(begin_of_year)

    month = 6
    test_date = date.fromisoformat(f'{today.year}-0{month}-15')
    assert normal_contract.num_vacation_days(test_date) == month
