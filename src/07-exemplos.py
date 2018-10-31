def multiplica(a, b):
    '''
    Inteiro Positivo, Inteiro Positivo -> Inteiro Positivo
    Calcula o produto entre a e b usando sequencia de adições.
    Exemplos
    >>> multiplica(3, 4)
    12
    >>> multiplica(2, 5)
    10
    >>> multiplica(5, 0)
    0
    '''
    n = 0
    prod = 0
    while n != b:
        n = n + 1
        prod = prod + a
    return prod


def resto(a, b):
    '''
    Inteiro Positivo, Inteiro Positivo -> Inteiro Positivo
    Calcula o resto da divisão de a por b usando sequencia de subtrações.
    Exemplos
    >>> resto(10, 2)
    0
    >>> resto(10, 3)
    1
    >>> resto(10, 4)
    2
    '''
    resto = a
    while resto >= b:
        resto = resto - b
    return resto


def proximo_multiplo(m, n):
    '''
    Inteiro Positivo, Inteiro Positivo -> Inteiro Positivo
    Encontra o menor número maior que m que seja múltiplo de n.
    >>> proximo_multiplo(10, 8)
    16
    >>> proximo_multiplo(6, 2)
    8
    >>> proximo_multiplo(5, 5)
    10
    '''
    p = m + 1
    while p % n != 0:
        p = p + 1
    return p


def proximo_multiplo_2(m, n):
    '''
    Inteiro Positivo, Inteiro Positivo -> Inteiro Positivo
    Encontra o menor número maior que m que seja múltiplo de n.
    >>> proximo_multiplo_2(10, 8)
    16
    >>> proximo_multiplo_2(6, 2)
    8
    >>> proximo_multiplo_2(5, 5)
    10
    '''
    return n * ((m // n) + 1)


def e(x):
    '''
    Número -> Número
    Calcula o valor de e**x (onde e é o número de Euler) usando uma série de
    Taylor.
    Exemplos
    >>> round(e(1.0), 5)
    2.71828
    >>> round(e(2.0), 5)
    7.38906
    >>> round(e(3.0), 5)
    20.08554
    '''
    n = 0
    dividendo = 1
    divisor = 1
    termo = 1
    soma = 1
    while termo > 0.000001:
        n = n + 1
        dividendo = dividendo * x
        divisor = divisor * n
        termo = dividendo / divisor
        soma = soma + termo
    return soma