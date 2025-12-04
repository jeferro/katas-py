
from datetime import date

from src.yearly_vacation.normal_contract import NormalContract
from src.yearly_vacation.special_contract import SpecialContract


test_date = date.fromisoformat('2025-06-01')


def test_24_days_on_normal_contract():
    birthday = date.fromisoformat('2001-01-26')
    start_date = date.fromisoformat('2024-01-01')

    normal_contract = NormalContract('Marco Gil',
                                     birthday,
                                     start_date)

    assert normal_contract.num_vacation_days(test_date) == 24

def test_special_contract_can_override_vacation_days():
    birthday = date.fromisoformat('1999-07-12')
    start_date = date.fromisoformat('2024-01-01')

    special_contract = SpecialContract('Marco Sanchez',
                                       birthday,
                                       start_date,
                                       26)

    assert special_contract.num_vacation_days(test_date) == 26

def test_in_contract_which_starts_at_current_year_have_vacation_days_similar_to_number_of_months():
    birthday = date.fromisoformat('1997-12-30')
    start_date = date.fromisoformat('2025-01-01')

    normal_contract = NormalContract('Juan Perez',
                                     birthday,
                                     start_date)

    assert normal_contract.num_vacation_days(test_date) == 6

def test_additional_vacation_days_on_normal_contract():
    birthday = date.fromisoformat('1986-06-09')
    start_date = date.fromisoformat('2018-01-01')

    normal_contract = NormalContract('Laura Martinez',
                                     birthday,
                                     start_date)

    assert normal_contract.num_vacation_days(test_date) == 30