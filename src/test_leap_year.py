from src.is_leap_year import is_leap_year


def test_is_not_leap_year():
    assert is_leap_year(1957) == False 

def test_is_divisible_by_4():
    assert is_leap_year(1996) == True 
    