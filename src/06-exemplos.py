def fatorial(n):
    '''
    Natural -> Natural
    Devolve o valor n * (n - 1) * ... * 1.
    Exemplos
    >>> fatorial(0)
    1
    >>> fatorial(1)
    1
    >>> fatorial(3)
    6
    >>> fatorial(5)
    120
    '''
    if n == 0:
        fat = 1
    else:
        fat = n * fatorial(n - 1)
    return f


def par(n):
    '''
    Natural -> Booleano
    Devolve True se n é par, isto é, divisível por 2, False caso contrário.
    Exemplos
    >>> par(8)
    True
    >>> par(5)
    False
    '''
    if n == 0:
        e_par = True
    else:
        e_par = not par(n - 1)
    return e_par


def divisao(a, b):
    '''
    Natural, Natural -> Natural
    Devolve o resultado da divisão inteira de a por b.
    Exemplos
    >>> divisao(4, 5)
    0
    >>> divisao(3, 3)
    1
    >>> divisao(7, 3)
    2
    >>> divisao(13, 2)
    6
    '''
    if a < b:
        d = 0
    else:
        d = 1 + divisao(a - b, b)
    return d
