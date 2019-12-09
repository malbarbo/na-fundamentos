from doctest import testmod


# Defina uma função que some todos os elementos das posições pares de uma
# lista.

def soma_posicoes_pares(xs):
    '''
    Lista de números -> Número
    Soma os elementos das posições pares de xs, isto é, xs[0] + xs[2] + xs[4] + ...
    Exemplos
    >>> soma_posicoes_pares([1, 2, 4, 7, 1, 2])
    6
    >>> soma_posicoes_pares([3, 7])
    3
    >>> soma_posicoes_pares([3, 7, 2])
    5
    '''
    soma = 0
    i = 0
    while i < len(xs):
        soma = soma + xs[i]
        i = i + 2
    return soma


# Defina uma função calcule o produto do elementos de uma lista.

def produto(xs):
    '''
    Lista de números -> Número
    Calcula o produto de todos os números de xs.
    >>> produto([4, 2, 7])
    56
    >>> produto([])
    1
    >>> produto([4])
    4
    '''
    prod = 1
    for x in xs:
        prod = prod * x
    return prod



# Defina uma função que verifique se todos os elementos de uma lista não vazia
# são iguais.

def todos_iguais(xs):
    '''
    Devolve True se todos os elementos de xs são iguais, False caso contrário.
    Lista -> Boolean
    >>> todos_iguais([2, 2, 2])
    True
    >>> todos_iguais([2, 2, 1])
    False
    >>> todos_iguais([1])
    True
    >>> todos_iguais([1, 2])
    False
    '''
    iguais = True
    a = xs[0]
    for x in xs:
        if x != a:
            iguais = False
    return iguais


# Defina uma função que receba como parâmetros dois números naturais n e k, e
# produza uma lista com os k primeiros múltiplos de n.

def multiplos(n, k):
    '''
    Cria um lista com os primeiros k múltiplos de n.
    >>> multiplos(3, 5)
    [0, 3, 6, 9, 12]
    >>> multiplos(4, 0)
    []
    >>> multiplos(2, 1)
    [0]
    >>> multiplos(5, 2)
    [0, 5]
    '''
    mul = []
    i = 0
    while i < k:
        mul.append(i * n)
        i = i + 1
    return mul


# Defina uma função que receba como parâmetro um lista e um valor n e verifique
# se a soma dos n primeiros elementos da lista é igual a soma dos últimos n
# elementos da lista.

def soma_inicio_fim_igual(xs, n):
    '''
    Verifica se a soma dos n primeiros elementos de xs é igual a soma dos
    últimos n elementos de xs.
    >>> soma_inicio_fim_igual([3, 2, 1, 7, 2, 9, 8, 1, 1, 4], 3)
    True
    >>> soma_inicio_fim_igual([3, 2, 1, 7, 2, 9, 8, 1, 1, 4], 1)
    False
    >>> soma_inicio_fim_igual([3, 4], 0)
    True
    >>> soma_inicio_fim_igual([3, 4], 1)
    False
    >>> soma_inicio_fim_igual([3, 4], 2)
    True
    '''
    s = 0
    i = 0
    while i < len(xs) and i < n:
        s = s + xs[i]
        i = i + 1
    j = len(xs) - 1
    while j >= 0 and j >= len(xs) - n:
        s = s - xs[j]
        j = j - 1
    return s == 0


# Defina uma função que calcule a média dos valores de uma lista não vazia.

def media(xs):
    '''
    Lista de números -> Número
    Calcula a média dos valores da lista não vazia xs.
    Exemplos
    >>> media([3.0])
    3.0
    >>> media([3.0, 4.0, 5.0])
    4.0
    '''
    soma = 0
    for x in xs:
        soma = soma + x
    return soma / len(xs)


# Defina uma função que encontre o valor máximo de uma lista não vazia.

def maximo(xs):
    '''
    Lista de números -> Número
    Encontra o valor máximo da lista não vazia xs.
    Exemplo
    >>> maximo([1])
    1
    >>> maximo([5, 7, 1, 2])
    7
    >>> maximo([-3, -2, -1, -5])
    -1
    '''
    max = xs[0]
    for x in xs:
        if x > max:
            max = x
    return max


# Defina uma função que verifique se um dado elemento está em uma lista.

def contem(valor, xs):
    '''
    Número, Lista de números -> Booleano
    Devolve True se valor está presente em xs, False caso contrário.
    Exemplos
    >>> contem(2, [])
    False
    >>> contem(8, [2, 5, 10])
    False
    >>> contem(2, [2, 5, 10])
    True
    >>> contem(5, [2, 5, 10])
    True
    >>> contem(10, [2, 5, 10])
    True
    '''
    presente = False
    for x in xs:
        if valor == x:
            presente = True
    return presente


def contem2(valor, xs):
    '''
    Número, Lista de números -> Booleano
    Devolve True se valor está presente em xs, False caso contrário
    Exemplos
    >>> contem2(2, [])
    False
    >>> contem2(8, [2, 5, 10])
    False
    >>> contem2(2, [2, 5, 10])
    True
    >>> contem2(5, [2, 5, 10])
    True
    >>> contem2(10, [2, 5, 10])
    True
    '''
    # Usamos while ao invés de for, desta forma podemos interromper a repetição
    # se valor for encontrado em xs
    presente = False
    i = 0
    while i < len(xs) and not presente:
        if valor == xs[i]:
            presente = True
        i = i + 1
    return presente


# Defina uma função que devolva a posição do valor máximo de uma lista não
# vazia.

def indice_maximo(xs):
    '''
    Lista de números -> Número
    Devolve a posição do valor máximo de xs. Isto é, o índice i tal
    que xs[i] == maximo(xs).
    >>> indice_maximo([5])
    0
    >>> indice_maximo([4, 4, 4, 4])
    0
    >>> indice_maximo([4, 1, 5])
    2
    >>> indice_maximo([4, 1, 5, 8, 5, 8])
    3
    '''
    m = maximo(xs)
    i = 0
    while xs[i] != m:
        i = i + 1
    return i


# Defina uma função que devolva as posições do valor máximo de uma lista não
# vazia.

def indices_maximo(xs):
    '''
    Lista de números -> Número
    Devolve todos os índices das ocorrências do valor máximo de xs.
    >>> indices_maximo([5])
    [0]
    >>> indices_maximo([4, 4, 4, 4])
    [0, 1, 2, 3]
    >>> indices_maximo([4, 1, 5])
    [2]
    >>> indices_maximo([4, 1, 5, 8, 5, 8])
    [3, 5]
    '''
    m = maximo(xs)
    i = 0
    indices = []
    while i < len(xs):
        if xs[i] == m:
            indices.append(i)
        i = i + 1
    return indices


# Defina uma função que receba como parâmetro dois números inteiros não
# negativos a e b, onde a <= b, e devolva uma lista com todos os números (em
# ordem crescente) no intervalo [a, b].

def lista_intervalo(a, b):
    '''
    Inteiro positivo, Inteiro Positivo -> Lista de números inteiros
    Cria uma lista com os números inteiros no intervalo [a, b].
    Exemplos
    >>> lista_intervalo(5, 5)
    [5]
    >>> lista_intervalo(2, 5)
    [2, 3, 4, 5]
    >>> lista_intervalo(-2, 2)
    [-2, -1, 0, 1, 2]
    '''
    xs = []
    n = a
    while n <= b:
        xs.append(n)
        n = n + 1
    return xs


# Defina uma função que receba como parâmetro uma lista xs e crie uma nova
# lista com os elementos positivos de xs.

def positivos(xs):
    '''
    Lista de números - > Lista de números
    Devolve uma lista com os elementos positivos de xs.
    >>> positivos([])
    []
    >>> positivos([1, -2, 5, -3, 8, 9])
    [1, 5, 8, 9]
    >>> positivos([-1, -5])
    []
    >>> positivos([1, 5])
    [1, 5]
    '''
    pos = []
    for x in xs:
        if x > 0:
            pos.append(x)
    return pos


# Defina uma função que calcule a união de dois conjuntos (sem usar o operador |).

def uniao_conjunto(a, b):
    '''
    Conjunto de valores, Conjunto de valores -> Conjunto de valores
    Devolve um conjunto que é a união dos conjuntos a e b.
    Exemplos
    >>> uniao_conjunto({3, 4, 7}, {8, 6, 4, 3})
    {3, 4, 6, 7, 8}
    '''
    c = set()
    for x in a:
        c.add(x)
    for x in b:
        c.add(x)
    return c


# Defina uma função que receba como entrada uma lista de valores e devolva um
# dicionário que associe cada valor da lista com a posição de sua primeira
# ocorrência na lista.

def primeira_posicao(xs):
    '''
    Lista -> Dicionario
    Devolve um dicionário que associa cada elemento de xs com a primeira
    posição que ele aparece em xs.
    Exemplos
    >>> primeira_posicao([3, 3, 5, 5, 3, 4, 4, 3, 5, 4])
    {3: 0, 5: 2, 4: 5}
    '''
    pos = {}
    i = 0
    while i < len(xs):
        if xs[i] not in pos:
            pos[xs[i]] = i
        i = i + 1
    return pos
