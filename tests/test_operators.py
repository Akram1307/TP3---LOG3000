"""Unit tests for the arithmetic functions in operators.py."""

import pytest

from operators import add, subtract, multiply, divide


def test_add():
    """add returns the sum, including with negative and decimal numbers."""
    assert add(2, 3) == 5
    assert add(-4, 1) == -3
    assert add(1.5, 2.25) == 3.75


def test_subtract():
    """subtract returns a - b (order of operands matters)."""
    assert subtract(10, 4) == 6
    assert subtract(4, 10) == -6
    assert subtract(2.5, 0.5) == 2.0


def test_multiply():
    """multiply returns the product a * b."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(2.5, 2) == 5.0


def test_divide():
    """divide returns the exact quotient, not a rounded down one."""
    assert divide(8, 2) == 4
    assert divide(7, 2) == 3.5
    assert divide(-9, 2) == -4.5


def test_divide_by_zero():
    """Dividing by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(5, 0)
