def exp(a, b):
    '''
    Inteiro Positivo, Inteiro Positivo -> Inteiro
    Calcula o valor a**b usando uma sequencia de multiplicacoes
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


def conta_divisores_7_13(a, b):
    '''
    Inteiro Positivo, Inteiro Positivo -> Inteiro
    Calcula a quantidade de valores no intervalo [a, b] que sao multiplos
    de 7 e 13.
    Exemplos
    >>> conta_divisores_7_13(10, 20)
    0
    >>> conta_divisores_7_13(90, 182)
    2
    '''
    n = a
    cont = 0
    while n <= b:
        if n % 7 == 0 and n % 13 == 0:
            cont = cont + 1
        n = n + 1
    return cont


def sen(x):
    '''
    Numero -> Numero
    Calcula o valor de seno(x), onde x é dado em radianos, usando uma serie de
    Taylor.
    Exemplo
    >>> round(sen(1.0), 5)
    0.84147
    >>> round(sen(2.0), 5)
    0.9093
    >>> round(sen(3.0), 5)
    0.14112
    >>> round(sen(4.0), 5)
    -0.7568
    '''
    n = 0
    dividendo = x
    divisor = 1
    termo = dividendo / divisor
    seno = termo
    while abs(termo) > 0.000001:
        n = n + 1
        dividendo = -1 * dividendo * x * x
        divisor = divisor * (2 * n) * (2 * n + 1)
        termo = dividendo / divisor
        seno = seno + termo
    return seno


def cos(x):
    '''
    Numero -> Numero
    Calcula o valor de cosseno(x), onde x é dado em radianos, usando uma serie de
    Taylor.
    Exemplo
    >>> round(cos(1.0), 5)
    0.5403
    >>> round(cos(2.0), 5)
    -0.41615
    >>> round(cos(3.0), 5)
    -0.98999
    >>> round(cos(4.0), 5)
    -0.65364
    '''
    n = 0
    dividendo = 1
    divisor = 1
    termo = dividendo / divisor
    coss = termo
    while abs(termo) > 0.000001:
        n = n + 1
        dividendo = -1 * dividendo * x * x
        divisor = divisor * (2 * n) * (2 * n - 1)
        termo = dividendo / divisor
        coss = coss + termo
    return coss


def perfeito(n):
    '''
    Inteiro Positivo -> Boolean
    Devolve True se n é um número perfeito, False caso contrario.
    >>> perfeito(1)
    False
    >>> perfeito(5)
    False
    >>> perfeito(6)
    True
    >>> perfeito(7)
    False
    >>> perfeito(8)
    False
    >>> perfeito(27)
    False
    >>> perfeito(28)
    True
    '''
    soma_divisores = 0
    d = 1
    while d < n:
        if n % d == 0:
            soma_divisores = soma_divisores + d
        d = d + 1
    return n == soma_divisores


def primo(n):
    '''
    Inteiro Positivo -> Boolean
    Devolve True e n é número primo, False caso contrario.
    Exemplos
    >>> primo(1)
    False
    >>> primo(2)
    True
    >>> primo(3)
    True
    >>> primo(4)
    False
    >>> primo(5)
    True
    >>> primo(6)
    False
    '''
    tem_divisor = False
    d = 2
    while d < n and not tem_divisor:
        if n % d == 0:
            tem_divisor = True
        d = d + 1
    return not tem_divisor and n != 1


def decompoe_soma_2_primos(n):
    '''
    Inteiro Positivo -> (Inteiro Positivo, Inteiro Positivo)
    Encontra numeros primos a e b tal que n = a + b.
    Exemplos
    >>> decompoe_soma_2_primos(4)
    (2, 2)
    >>> decompoe_soma_2_primos(5)
    (2, 3)
    >>> decompoe_soma_2_primos(6)
    (3, 3)
    >>> decompoe_soma_2_primos(7)
    (2, 5)
    >>> decompoe_soma_2_primos(8)
    (3, 5)
    >>> decompoe_soma_2_primos(9)
    (2, 7)
    '''
    encontrou = False
    a = 2
    while a <= n / 2 and not encontrou:
        b = n - a
        if primo(a) and primo(b):
            encontrou = True
            nums = (a, b)
        a = a + 1
    if not encontrou:
        nums = 'Não encontrou'
    return nums
