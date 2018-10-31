# Este programa exibe uma bola que se movimenta na horizontal e muda de direção
# quando chega na lateral da janela. Quando a tecla + é pressionada a bola
# aumenta de velocidade e quando a tecla - é pressionada a bola diminui de
# velocidade.
#
# Para executar o programa, digite main(BOLA_INICIAL) na janela de interações

# Permite que o arquivo creation.py seja importado no Windows
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from typing import NamedTuple
from creation import *
from doctest import testmod


# Bola representa o estado do mundo
class Bola(NamedTuple):
    # posição no eixo x da bola
    x: float
    # modulo da velocidade no eixo x
    vx: float
    # direção da bola, pode ser 'esquerda' ou 'direita'
    direcao: str


RAIO = 20
LARGURA = 600
ALTURA = 400
POS_Y = ALTURA / 2
AUMENTO_VELOCIDADE = 1
VELOCIDADE_MAXIMA = LARGURA - 2 * RAIO
BOLA_INICIAL = Bola(LARGURA / 2, 1, 'direita')

# Imagens
FUNDO = rectangle(LARGURA, ALTURA, fill('white'))
BOLA = circle(RAIO, fill('red'))


def desenho(bola):
    '''
    Bola -> Imagem
    Cria uma imagem do mundo.
    Esta função foi testada fazendo uma inspeção visual dos seguintes exemplos:
    image_view(desenho(Bola(50, 1, 'direita')))
    image_view(desenho(Bola(250, 1, 'direita')))
    image_view(desenho(Bola(500, 1, 'direita')))
    '''
    return place(
        BOLA,
        'center', bola.x,
        'center', POS_Y,
        FUNDO
    )


def on_tick(bola):
    '''
    Bola -> Bola
    Manipula evento de relógio.
    Avança a bola na direção atual. Quando a bola passa do limite da janela,
    ela muda de direção.
    Exemplos
    >>> on_tick(Bola(20, 5, 'direita'))
    Bola(x=25, vx=5, direcao='direita')
    >>> on_tick(Bola(50, 5, 'esquerda'))
    Bola(x=45, vx=5, direcao='esquerda')

    Os exemplos a seguir ilustram a bola mudando de direção. A bola tem que
    avançar 40 pixels, mas ela só pode avançar 10 na direção atual, portanto
    ela avança estes 10, muda de direção e avança os outros 30 na nova direção.
    >>> on_tick(Bola(LARGURA - RAIO - 10 , 40, 'direita')) == Bola(LARGURA - RAIO - 30, 40, 'esquerda')
    True
    >>> on_tick(Bola(RAIO + 10, 40, 'esquerda')) == Bola(RAIO + 30, 40, 'direita')
    True
    '''
    if bola.direcao == 'direita':
        nx = bola.x + bola.vx
        if nx <= LARGURA - RAIO:
            b = Bola(nx, bola.vx, bola.direcao)
        else:
            b = Bola(2 * (LARGURA - RAIO) - nx, bola.vx, 'esquerda')
    else:  # bola.direcao == 'esquerda'
        nx = bola.x - bola.vx
        if nx >= RAIO:
            b = Bola(nx, bola.vx, bola.direcao)
        else:
            b = Bola(2 * RAIO - nx, bola.vx, 'direita')
    return b


def on_key(bola, tecla):
    '''
    Bola, Tecla -> Bola
    Aumenta a velocidade da bola quando a tecla '+' é pressionada ou diminui a
    velocidade da bola quando a tecla '-' é pressionada. A velocidade mínima é
    1 e a velocidade máxima é VELOCIDADE_MAXIMA.
    Exemplos
    >>> on_key(Bola(10, 2, 'direita'), '+')
    Bola(x=10, vx=3, direcao='direita')
    >>> on_key(Bola(10, 2, 'direita'), '-')
    Bola(x=10, vx=1, direcao='direita')
    >>> on_key(Bola(10, 1, 'direita'), '-')
    Bola(x=10, vx=1, direcao='direita')
    >>> on_key(Bola(10, LARGURA - 2 * RAIO, 'direita'), '+') == Bola(10, LARGURA - 2 * RAIO, 'direita')
    True
    '''
    if tecla == '+' and bola.vx < VELOCIDADE_MAXIMA:
        b = Bola(bola.x, bola.vx + 1, bola.direcao)
    elif tecla == '-' and bola.vx > 1:
        b = Bola(bola.x, bola.vx - 1, bola.direcao)
    else:
        b = bola
    return b


def main(bola):
    return create(bola, desenho, on_tick=on_tick, on_key=on_key)