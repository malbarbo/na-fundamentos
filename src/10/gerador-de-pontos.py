from random import random
import sys


def main():
    # verificação do modode uso
    if len(sys.argv) != 2:
        print('Modo de usar inválido')
        print('Você forneceu {} argumento(s), forneça apenas 1 argumento (a quantidade de pontos)'.format(len(sys.argv) - 1))
        sys.exit()

    # entrada
    n = int(sys.argv[1])

    # processamento
    pontos = gerar(n)

    # saida
    for (x, y) in pontos:
        print('{:.5f} {:0.5f}'.format(x, y))


def gerar(n):
    '''
    Inteiro -> Lista (float, float)
    Gera uma lista com n pontos aleatórios com as coordenadas no intervalo [0, 1].
    '''
    pontos = []
    for _ in range(n):
        pontos.append((random(), random()))
    return pontos


if __name__ == '__main__':
    main()
