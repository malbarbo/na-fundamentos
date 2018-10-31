# Este programa exibe um triangulo no centro da tela que aumenta de tamanho com
# o passar do tempo. Quando a tecla espaço é pressionada o triângulo volta ao
# tamanho inicial e continua a aumentar de tamanho;
#
# Para executar o programa, digite main(LADO_INICIAL) na janela de interações

# Permite que o arquivo creation.py seja importado no Windows
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from creation import *
from doctest import testmod

# Mundo
#   Número: tamanho do lado do triângulo

LADO_INICIAL = 40
AUMENTO = 10
LARGURA = 600
ALTURA = 400
FUNDO = rectangle(LARGURA, ALTURA, fill('white'))


def desenho(lado):
    '''
    Mundo -> Imagem
    Cria uma imagem do mundo.
    Esta função foi testada fazendo uma inspeção visual dos seguintes exemplos:
    image_view(desenho(100))
    image_view(desenho(200))
    image_view(desenho(300))
    '''
    return place(
        triangle(lado, fill('red')),
        'center', LARGURA / 2,
        'center', ALTURA / 2,
        FUNDO,
    )


def on_tick(lado):
    '''
    Mundo -> Mundo
    Aumenta o lado do triângulo.
    Exemplos
    >>> on_tick(100) == 100 + AUMENTO
    True
    '''
    return lado + AUMENTO


def on_key(lado, tecla):
    '''
    Mundo, Tecla -> Mundo
    Retorna o lado do triângulo para o tamanho inicial se tecla for ' '.
    Exemplos
    >>> on_key(100, 'a')
    100
    >>> on_key(100, ' ') == TAMANHO_INICIAL
    True
    '''
    if tecla == ' ':
        nlado = LADO_INICIAL
    else:
        nlado = lado
    return nlado


def main(lado):
    return create(lado, desenho, on_tick=on_tick, on_key=on_key)
