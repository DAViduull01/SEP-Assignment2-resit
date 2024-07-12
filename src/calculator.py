# src/calculator.py

"""
This module provides a mathematical operation and that is division.
"""

def divide(numerator, denominator):
    """
    Divide the numerator by the denominator.

    Args:
        numerator (int or float): The number to be divided (numerator).
        denominator (int or float): The number by which to divide (denominator).

    Returns:
        float: The result of the division.

    Raises:
        ValueError: If the denominator is zero.

    Example:
        >>> divide(10, 2)
        5.0
        >>> divide(5, 0)
        Traceback (most recent call last):
            ...
        ValueError: Cannot divide by zero
    """
    if denominator == 0:
        raise ValueError("Cannot divide by zero")
    return numerator / denominator
