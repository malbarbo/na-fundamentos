def resto(a, b):
    '''
    Inteiro Positivo, Inteiro Positivo -> Inteiro Positivo
    Calcula o resto da divisão de a por b usando uma sequência de subtrações.
    Exemplos
    >>> resto(18, 5)
    3
    >>> resto(16, 3)
    1
    >>> resto(8, 2)
    0
    '''
    resto = a
    while resto >= b:
        resto = resto - b
    return resto


def multiplica(a, b):
    '''
    Inteiro Positivo, Inteiro Positivo -> Inteiro Positivo
    Calcula o produto entre a e b usando uma sequência de adições.
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


def exp(a, b):
    '''
    Inteiro Positivo, Inteiro Positivo -> Inteiro
    Calcula o valor a**b usando uma sequência de multiplicações
    Exemplos
    >>> exp(3, 1)
    3
    >>> exp(3, 2)
    9
    >>> exp(3, 3)
    27
    '''
    n = 0
    expo = 1
    while n != b:
        expo = expo * a
        n = n + 1
    return expo


def conta_multiplos_3_5(a, b):
    '''
    Inteiro Positivo, Inteiro Positivo -> Inteiro
    Calcula a quantidade de valores no intervalo [a, b] que sao múltiplos
    de 3 e 5.
    Exemplos
    >>> conta_multiplos_3_5(1, 14)
    0
    >>> conta_multiplos_3_5(10, 31)
    2
    '''
    n = a
    cont = 0
    while n <= b:
        if n % 3 == 0 and n % 5 == 0:
            cont = cont + 1
        n = n + 1
    return cont


def hiperfatorial(n):
    '''
    Inteiro Positivo -> Inteiro Positivo
    Calcula o hiperfatorial de n, que é definido como
    1**1 * 2**2 * 3 ** 3 ... n ** n
    Exemplos
    >>> hiperfatorial(1)
    1
    >>> hiperfatorial(2)
    4
    >>> hiperfatorial(3)
    108
    '''
    hfat = 1
    k = 0
    while k != n:
        k = k + 1
        hfat = hfat * k ** k
    return hfat


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
