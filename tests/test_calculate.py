"""Tests for calculate() in app.py: parsing and evaluating expressions."""

import pytest

from app import calculate


@pytest.mark.parametrize("expr, expected", [
    ("3+4", 7),
    ("10-4", 6),
    ("3*4", 12),
    ("7/2", 3.5),
])
def test_calculate_each_operator(expr, expected):
    """Each of the 4 operators gives the right result through calculate."""
    assert calculate(expr) == expected


def test_calculate_ignores_spaces():
    """Spaces around numbers and operators are ignored."""
    assert calculate(" 3 + 4 ") == 7


def test_calculate_decimals():
    """Decimal operands are accepted."""
    assert calculate("1.5+2.25") == 3.75


@pytest.mark.parametrize("expr", [
    "",
    "1+2+3",
    "+5",
    "5+",
    "42",
    "a+3",
])
def test_calculate_invalid_expressions(expr):
    """Malformed expressions raise ValueError instead of returning a value."""
    with pytest.raises(ValueError):
        calculate(expr)
