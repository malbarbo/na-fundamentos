from doctest import testmod


def dobro(x):
    '''
    Número -> Número
    Calcula o dobro de x.

    Exemplos
    >>> dobro(3)
    6
    >>> dobro(2.4)
    4.8
    >>> dobro(-4.1)
    -8.2
    '''
    return 2 * x


def par(x):
    '''
    Inteiro positivo -> Boleano
    Devolve True se x é um número par, isto é, se x é múltiplo de 2.

    Exemplos
    >>> par(7)
    False
    >>> par(4)
    True
    '''
    return x % 2 == 0


def maximo(x, y):
    '''
    Número, Número -> Número
    Devolve o valor máximo entre x e y.

    Exemplos
    >>> maximo(2, 3)
    3
    >>> maximo(2, 2)
    2
    >>> maximo(4, 3)
    4
    >>> maximo(-4, -7)
    -4
    '''
    if x > y:
        maxi = x
    else:
        maxi = y
    return maxi


def maximo3v1(x, y, z):
    '''
    Número, Número, Número -> Número
    Devolve o valor máximo entre x, y e z.

    Exemplos
    >>> maximo3v1(4, 2, 3)
    4
    >>> maximo3v1(4, 7, 3)
    7
    >>> maximo3v1(1, 2, 3)
    3
    >>> maximo3v1(2, 2, 1)
    2
    >>> maximo3v1(2, 1, 2)
    2
    >>> maximo3v1(1, 2, 2)
    2
    >>> maximo3v1(4, 4, 4)
    4
    '''
    if x >= y:
        if x >= z:
            m = x
        else:
            m = z
    else:
        if y >= z:
            m = y
        else:
            m = z
    return m


def maximo3v2(x, y, z):
    '''
    Número, Número, Número -> Número
    Devolve o valor máximo entre x, y e z.

    Exemplos
    >>> maximo3v2(4, 2, 3)
    4
    >>> maximo3v2(4, 7, 3)
    7
    >>> maximo3v2(1, 2, 3)
    3
    >>> maximo3v2(2, 2, 1)
    2
    >>> maximo3v2(2, 1, 2)
    2
    >>> maximo3v2(1, 2, 2)
    2
    >>> maximo3v2(4, 4, 4)
    4
    >>> maximo3v2(2, 1, 3)
    3
    '''
    if x >= y and x >= z:
        m = x
    else:
        if y >= x and y >= z:
            m = y
        else:
            m = z
    return m


def maximo3v3(x, y, z):
    '''
    Número, Número, Número -> Número
    Devolve o valor máximo entre x, y e z.

    Exemplos
    >>> maximo3v3(4, 2, 3)
    4
    >>> maximo3v3(4, 7, 3)
    7
    >>> maximo3v3(1, 2, 3)
    3
    >>> maximo3v3(2, 2, 1)
    2
    >>> maximo3v3(2, 1, 2)
    2
    >>> maximo3v3(1, 2, 2)
    2
    >>> maximo3v3(4, 4, 4)
    4
    '''
    if x >= y and x >= x:
        m = x
    elif y >= x and y >= z:
        m = y
    else:
        m = z
    return m


def maximo3(x, y, z):
    '''
    Número, Número, Número -> Número
    Devolve o valor máximo entre x, y e z.

    Exemplos
    >>> maximo3(4, 2, 3)
    4
    >>> maximo3(4, 7, 3)
    7
    >>> maximo3(1, 2, 3)
    3
    >>> maximo3(2, 2, 1)
    2
    >>> maximo3(2, 1, 2)
    2
    >>> maximo3(1, 2, 2)
    2
    >>> maximo3(4, 4, 4)
    4
    '''
    return maximo(x, maximo(y, z))


def soma_quadrado_maiores(x, y, z):
    '''
    Número, Número, Número -> Número
    Calcula a soma dos quadrados nos dois maiores valores entre x, y, z.

    Exemplos
    >>> soma_quadrado_maiores(3, 2, 1)
    13
    >>> soma_quadrado_maiores(3, 2, 4)
    25
    >>> soma_quadrado_maiores(2, 3, 5)
    34
    '''
    if x >= z and y >= z:
        m1 = x
        m2 = y
    elif x >= y and z >= y:
        m1 = x
        m2 = z
    else:
        m1 = y
        m2 = z
    return m1 ** 2 + m2 ** 2


def classifica_triangulo(a, b, c):
    '''
    Número, Número, Número -> String
    Classifica um triângulo de acordo com as medidas a, b e c do seus lados.
    Um triângulo com os três lados iguais é equilátero. Um triângulo com dois
    lados iguais é escaleno e um triângulo com os três lados diferentes é
    escaleno.

    Exemplos
    >>> classifica_triangulo(3, 3, 3)
    'equilátero'
    >>> classifica_triangulo(2, 2, 3)
    'isósceles'
    >>> classifica_triangulo(2, 3, 2)
    'isósceles'
    >>> classifica_triangulo(2, 2, 3)
    'isósceles'
    >>> classifica_triangulo(2, 3, 4)
    'escaleno'
    '''
    if a == b and b == c:
        tipo = 'equilátero'
    elif a != b and b != c and a != c:
        tipo = 'escaleno'
    else:
        tipo = 'isósceles'
    return tipo


def baskara(a, b, c):
    '''
    Número, Número, Número -> Número ou (Número, Número) ou String
    Calcula as raízes da equação a (x ** 2) + b x + c. Devolve um valor se a
    equação só tem uma raiz, devolve dois valores se a equação tem duas raízes
    ou devolve 'sem raízes' se a equação não tem raiz.

    Exemplos
    >>> baskara(1, 2, -3)
    (1.0, -3.0)
    >>> baskara(1, 4, 4)
    -2.0
    >>> baskara(4, 2, 3)
    'sem raízes'
    '''
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        r = (x1, x2)
    elif delta == 0:
        r = -b / (2 * a)
    else:
        r = 'sem raízes'
    return r
