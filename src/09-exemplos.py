# Dado uma lista de números, defina uma função que some 1 a cada elemento da
# lista.
#   1. Defina uma função que devolva uma nova lista.
#   2. Defina uma função que altere a lista passada como parâmetro.

def soma_1(xs):
    '''
    Lista de números -> Lista de números
    Cria uma lista de númerois somando 1 a cada elemento de xs.
    >>> soma_1([1, 3, 4])
    [2, 4, 5]
    >>> soma_1([5])
    [6]
    >>> soma_1([])
    []
    '''
    ys = []
    for x in xs:
        ys.append(x + 1)
    return ys


def soma_1_mod(xs):
    '''
    Lista de números -> None
    Modifica xs somando 1 a cada elemento.
    Exemplos
    >>> xs = [1, 3, 4]
    >>> soma_1_mod(xs)
    >>> xs
    [2, 4, 5]
    >>> xs = [5]
    >>> soma_1_mod(xs)
    >>> xs
    [6]
    >>> xs = []
    >>> soma_1_mod(xs)
    >>> xs
    []
    '''
    i = 0
    while i < len(xs):
        xs[i] = xs[i] + 1
        i = i + 1
