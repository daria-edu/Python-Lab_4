import pytest
from math_module import factorial

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)
