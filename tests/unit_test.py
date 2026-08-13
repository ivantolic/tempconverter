from converter import celsius_to_fahrenheit

def test_zero_celsius():
    assert celsius_to_fahrenheit(0) == 32


def test_boiling_point():
    assert celsius_to_fahrenheit(100) == 212
    
def test_decimal_value():
    assert celsius_to_fahrenheit(2) == 35.6
    
def test_minus_forty():
    assert celsius_to_fahrenheit(-40) == -40