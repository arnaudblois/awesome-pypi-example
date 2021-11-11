"""An example module."""

import math

PHI = (1 + math.sqrt(5)) / 2


def fibonacci(num: int) -> int:
    """Return the num-th number in the Fibonacci sequence.

    Here we're using the closed-form of the equation.
    """
    return round(PHI ** num / math.sqrt(5))
