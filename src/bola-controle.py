# Este programa exibe uma bola se move em um determinada direção com o passa do
# tempo. A bola para quando chega nos limites da janela. As teclas 'left',
# 'right', 'up' e 'down' controlam a direção da bola.

# Para executar o programa, digite main(BOLA_INICIAL) na janela de interações

# Permite que o arquivo creation.py seja importado no Windows
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from typing import NamedTuple
from creation import *

# Bola representa o estado do mundo
class Bola(NamedTuple):
    # posição x do centro da bola
    x: float
    # posição y do centro da bola
    y: float
    # direção da bola. Pode ser 'left' 'right', 'up' ou 'down'
    dir: str


VELOCIDADE = 5
RAIO = 10
LARGURA = 600
ALTURA = 400
BOLA_INICIAL = Bola(LARGURA / 2, ALTURA / 2, 'right')


def draw(bola):
    '''
    Bola -> Imagem
    Cria uma imagem do mundo.
    Esta função foi testada fazendo uma inspeção visual dos seguintes exemplos:
    image_view(desenho(Bola(50, 50, 'left')))
    image_view(desenho(Bola(50, 150, 'left')))
    image_view(desenho(Bola(150, 350, 'left')))
    '''
    return place(
        circle(RAIO, fill('red')),
        'center', bola.x,
        'center', bola.y,
        rectangle(LARGURA, ALTURA, 'white')
    )


def on_tick(bola):
    '''
    Bola -> Bola
    Manipula evento de relógio.
    Avança a bola na direção atual. A bola nunca ultrapassa o limite da janela
    Exemplos
    >>> on_tick(Bola(30, 50, 'left')) == Bola(30 - VELOCIDADE, 50, 'left')
    True
    >>> on_tick(Bola(RAIO + 2, 50, 'left')) == Bola(RAIO, 50, 'left')
    True
    >>> on_tick(Bola(30, 50, 'right')) == Bola(30 + VELOCIDADE, 50, 'right')
    True
    >>> on_tick(Bola(LARGURA - RAIO - 2, 50, 'right')) == Bola(LARGURA - RAIO, 50, 'right')
    True
    >>> on_tick(Bola(50, 30, 'up')) == Bola(50, 30 - VELOCIDADE, 'up')
    True
    >>> on_tick(Bola(50, RAIO + 2, 'up')) == Bola(50, RAIO, 'up')
    True
    >>> on_tick(Bola(50, 30, 'down')) == Bola(50, 30 + VELOCIDADE, 'down')
    True
    >>> on_tick(Bola(50, ALTURA - RAIO - 2, 'down')) == Bola(50, ALTURA - RAIO, 'down')
    True
    '''
    if bola.dir == 'left':
        x = max(RAIO, bola.x - VELOCIDADE)
    elif bola.dir == 'right':
        x = min(LARGURA - RAIO, bola.x + VELOCIDADE)
    else:
        x = bola.x

    if bola.dir == 'up':
        y = max(RAIO, bola.y - VELOCIDADE)
    elif bola.dir == 'down':
        y = min(ALTURA - RAIO, bola.y + VELOCIDADE)
    else:
        y = bola.y

    return Bola(x, y, bola.dir)


def on_key(bola, tecla):
    '''
    Bola, Tecla -> Bola
    Muda a direção da bola quando 'left', 'right', 'up' ou 'down' são pressionados.
    Exemplos
    >>> on_key(Bola(50, 50, 'right'), 'a')
    Bola(x=50, y=50, dir='right')
    >>> on_key(Bola(50, 50, 'right'), 'left')
    Bola(x=50, y=50, dir='left')
    >>> on_key(Bola(50, 50, 'left'), 'right')
    Bola(x=50, y=50, dir='right')
    >>> on_key(Bola(50, 50, 'right'), 'up')
    Bola(x=50, y=50, dir='up')
    >>> on_key(Bola(50, 50, 'left'), 'down')
    Bola(x=50, y=50, dir='down')
    '''
    if tecla == 'left' or tecla == 'right' or tecla == 'up' or tecla == 'down':
        dir = tecla
    else:
        dir = bola.dir
    return Bola(bola.x, bola.y, dir)


def main(bola):
    create(bola, draw, on_tick=on_tick, on_key=on_key)
