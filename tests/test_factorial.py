from .context import factorial
import pytest

def test_factorial():
    actual = factorial.factorial(5)
    expected = 120
    assert expected == actual