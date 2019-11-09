from .context import factorial
import pytest

def test_factorial_5():
    actual = factorial.factorial(5)
    expected = 120
    assert expected == actual

def test_factorial_10():
    actual = factorial.factorial(10)
    expected = 3628800
    assert expected == actual

@pytest.mark.xfail(raises=TypeError)
def test_wrong_type_factorial():
    actual = factorial.factorial("4")
    assert actual == 24