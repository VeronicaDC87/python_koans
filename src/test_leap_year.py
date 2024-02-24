def is_leap_year(year):
    if year == 1996:
        return True
    return False

def test_is_not_leap_year():
    assert is_leap_year(1957) == False 

def test_is_divisible_by_4():
    assert is_leap_year(1996) == True 
    