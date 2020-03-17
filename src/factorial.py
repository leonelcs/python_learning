from functools import wraps

def factorial(x: int) -> int:
    """

    Test Methodmake

    >>> factorial(5)
    120
    >>> factorial(4)
    24
    >>> factorial(7)
    5040

    """
    aux: int = 1
    for i in range(1, x+1):
        aux = aux*i
    return aux


def imprimir(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Printing: ')
        return f(*args, **kwds)
    return wrapper

def print_function(arg):
    print("returned value is: ", arg)

def outer(a):
    def inner(b):
        return a + b
    return inner

@imprimir
def print_factorial():
    """Docstring"""
    print('o valor da funcao')
