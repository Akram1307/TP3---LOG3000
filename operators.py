"""Arithmetic operations used by the calculator.

Each function takes two numbers and returns the result. app.py maps each
operator symbol (+, -, *, /) to one of them.
"""


def add(a,b):
    """Return the sum of two numbers.

    Args:
        a (float): Left operand.
        b (float): Right operand.

    Returns:
        float: a + b.
    """
    return a + b

def subtract(a,b):
    """Return the difference of two numbers.

    Args:
        a (float): Left operand.
        b (float): Right operand.

    Returns:
        float: a - b.
    """
    return b - a

def multiply(a,b):
    """Return the product of two numbers.

    Args:
        a (float): Left operand.
        b (float): Right operand.

    Returns:
        float: a * b.
    """
    return a * b

def divide(a,b):
    """Return the quotient of two numbers.

    Args:
        a (float): Dividend.
        b (float): Divisor.

    Returns:
        float: a / b.

    Raises:
        ZeroDivisionError: If b is 0.
    """
    return a / b
