# test_calculator.py

from calculator import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 5) == 4

def test_subtract():
    assert subtract(5, 3) == 2
    assert subtract(10, 7) == 3

def test_multiply():
    assert multiply(2, 3) == 6
    assert multiply(-2, 5) == -10

def test_divide():
    assert divide(6, 2) == 3
    assert divide(10, 2) == 5

def test_divide_by_zero():
    try:
        divide(5, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero"
    else:
        assert False, "Expected a ValueError but didn't get one"
