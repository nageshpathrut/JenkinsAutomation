from cal import calculator
import pytest

def test_add():
    assert calculator(3, 2, "add") == 5

def test_subtract():
    assert calculator(5, 3, "subtract") == 2

def test_multiply():
    assert calculator(4, 3, "multiply") == 12

def test_divide():
    assert calculator(10, 2, "divide") == 5

def test_divide_by_zero():
    with pytest.raises(ValueError):
        calculator(5, 0, "divide")

def test_invalid_operation():
    with pytest.raises(ValueError):
        calculator(3, 2, "modulus")
