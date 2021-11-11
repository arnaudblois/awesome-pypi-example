"""Tests of the example module using Pytest."""

from awesome_pypi_example.fibonacci import fibonacci


def test_fibonacci():
    """Test the first few numbers in the Fibonacci sequence."""
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1
    assert fibonacci(3) == 2
    assert fibonacci(4) == 3
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
