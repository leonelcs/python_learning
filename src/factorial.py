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