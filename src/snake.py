from creation import *
from doctest import testmod
from typing import NamedTuple
from random import randint


class Pos(NamedTuple):
    col: int
    lin: int


class SnakeWorld(NamedTuple):
    alvo: Pos
    dir: str
    corpo: List[Pos]


NUM_COLUNAS = 25
NUM_LINHAS = 15
LADO = 30
LARGURA = NUM_COLUNAS * LADO
ALTURA = NUM_LINHAS * LADO

FUNDO = rectangle(LARGURA, ALTURA, fill('white'))

ITEM_CORPO = overlay(
    'center',
    'center',
    rectangle(LADO, LADO, 'black'),
    rectangle(LADO, LADO, fill('blue'))
)

ALVO = overlay(
    'center',
    'center',
    rectangle(LADO, LADO, 'black'),
    rectangle(LADO, LADO, fill('red'))
)

MUNDO_INICIAL = SnakeWorld(
    Pos(12, 13),
    'right',
    [Pos(4, 10)]
)


def desenho(mundo):
    '''
    Mundo -> Imagem
    Cria uma imagem do mundo.
    '''
    img = FUNDO
    for p in mundo.corpo:
        img = place_item(ITEM_CORPO, p, img)
    img = place_item(ALVO, mundo.alvo, img)
    img = above('center', img, tamanho_imagem(len(mundo.corpo)))
    return img


def place_item(item, p, img):
    return place(
        item,
        'left', p.col * LADO,
        'top', p.lin * LADO,
        img
    )


def tamanho_imagem(tam):
    return text('Tamanho: ' + str(tam), 20, 'black')


def on_tick(mundo):
    '''
    Mundo -> Mundo
    '''
    np = move(mundo.corpo[0], mundo.dir)
    if pos_dentro_mundo(np) and np not in mundo.corpo:
        if np == mundo.alvo:
            corpo = [np] + mundo.corpo
            alvo = novo_alvo(corpo)
            m = SnakeWorld(alvo, mundo.dir, corpo)
        else:
            corpo = [np] + mundo.corpo[:-1]
            m = SnakeWorld(mundo.alvo, mundo.dir, corpo)
    else:
        m = mundo
    return m


def novo_alvo(corpo):
    '''
    List[Pos] -> Pos
    Gera uma posição aleatória dentro dos limites do mundo e diferente de todas
    as posições do corpo.
    Exemplos
    >>> corpo = [Pos(2, 3), Pos(2, 4)]
    >>> alvo = novo_alvo(corpo)
    >>> pos_dentro_mundo(alvo)
    True
    >>> alvo not in corpo
    True
    '''
    alvo = rand_alvo()
    while alvo in corpo:
        alvo = rand_alvo()
    return alvo


def rand_alvo():
    '''
    -> Pos
    Gera uma posição aleatória dentro dos limites do mundo.
    Exemplos
    >>> pos_dentro_mundo(rand_alvo())
    True
    '''
    return Pos(randint(0, NUM_COLUNAS - 1), randint(0, NUM_LINHAS - 1))


def move(p, dir):
    '''
    Pos, String -> Pos
    Move p na direção especifica por dir.
    Exemplos
    >>> move(Pos(0, 4), 'left')
    Pos(col=-1, lin=4)
    >>> move(Pos(0, 4), 'right')
    Pos(col=1, lin=4)
    >>> move(Pos(3, 0), 'up')
    Pos(col=3, lin=-1)
    >>> move(Pos(3, 0), 'down')
    Pos(col=3, lin=1)
    '''
    if dir == 'up':
        np = Pos(p.col, p.lin - 1)
    elif dir == 'down':
        np = Pos(p.col, p.lin + 1)
    elif dir == 'left':
        np = Pos(p.col - 1, p.lin)
    else:  # dir == 'right'
        np = Pos(p.col + 1, p.lin)
    return np


def pos_dentro_mundo(p):
    return 0 <= p.col < NUM_COLUNAS and 0 <= p.lin < NUM_LINHAS


def on_key(mundo, tecla):
    '''
    Mundo, Tecla -> Mundo
    '''
    if ((tecla == 'left' or tecla == 'right' or tecla == 'up' or tecla == 'down') and
            tecla != oposto(mundo.dir)):
        m = SnakeWorld(mundo.alvo, tecla, mundo.corpo)
    else:
        m = mundo
    return m


def oposto(dir):
    '''
    String -> String
    Devolve a direção oposta a dir.
    Exemplos
    >>> oposto('left')
    'right'
    >>> oposto('right')
    'left'
    >>> oposto('up')
    'down'
    >>> oposto('down')
    'up'
    '''
    if dir == 'left':
        r = 'right'
    elif dir == 'right':
        r = 'left'
    elif dir == 'up':
        r = 'down'
    else:  # dir == 'down'
        r = 'up'
    return r


def main(mundo):
    return create(mundo, desenho, on_tick=on_tick, ticks_per_second=10, on_key=on_key)


#main(MUNDO_INICIAL)