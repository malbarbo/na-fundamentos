from typing import NamedTuple

from doctest import testmod


def segundos(horas, minutos, segundos):
    ''' Inteiro, Inteiro, Inteiro -> Inteiro
    Converte o tempo dado em horas, minutos e segundos para segundos
    Exemplos:
    >>> segundos(0, 5, 4)
    304
    >>> segundos(1, 10, 12)
    4212
    '''
    return 3600 * horas + 60 * minutos + segundos


def hipotenusa(x, y):
    ''' Float, Float -> Float
    Calcula o valor da hipotenusa dados os catetos de um triângulo retângulo
    Exemplos
    >>> hipotenusa(3.0, 4.0)
    5.0
    >>> hipotenusa(6.0, 8.0)
    10.0
    '''
    return (x ** 2 + y ** 2) ** 0.5


def justifica_direita(texto, limite):
    ''' String, Inteiro -> String
    Cria um texto justificado a direita com um limite de caracteres
    Exemplos:
    >>> justifica_direita('casa', 10)
    '      casa'
    >>> justifica_direita('abacaxi', 10)
    '   abacaxi'
    >>> justifica_direita('abacaxi', 12)
    '     abacaxi'
    '''
    return ' ' * (limite - len(texto)) + texto


class Ponto(NamedTuple):
    '''Representa um ponto no plano cartesiano
        x - é a coordenada x
        y - é a coordenada y
    '''
    x: float
    y: float


def distancia(p1, p2):
    ''' Ponto, Ponto -> float
    Calcula a distância entre dois pontos no plano cartesiano
    Exemplos
    >>> distancia(Ponto(2.0, 7.0), Ponto(6.0, 4.0))
    5.0
    '''
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
