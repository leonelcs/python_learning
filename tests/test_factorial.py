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

def test_imprimir():
    factorial.imprimir(factorial, 5)

@pytest.mark.xfail(raises=TypeError)
def test_wrong_type_factorial():
    with pytest.raises(TypeError):
        factorial.factorial("5")