import sys


def main():
    if len(sys.argv) == 1:
        print('Este programa encontra os pontos mais distantes em um arquivo de pontos.')
        print('Especifique o arquivo com as coordenadas dos pontos como argumento para o programa.')
        sys.exit()

    if len(sys.argv) != 2:
        print('Modo de uso inválido.')
        print('Especifique exatamente um argumento.')
        sys.exit()

    # entrada
    pontos = le_pontos_arquivo(sys.argv[1])

    # processamento
    a, b = pontos_mais_distantes(pontos)

    # saida
    exibe_pontos_mais_distantes(a, b)


def pontos_mais_distantes(pontos):
    '''
    Lista (float, float) -> (float, float), (float, float)
    Encontra os pontos mais distantes na lista de pontos.
    Exemplos
    >>> pontos_mais_distantes([(3, 3)])
    ((3, 3), (3, 3))
    >>> pontos_mais_distantes([(3, 3), (0, 1)])
    ((3, 3), (0, 1))
    >>> pontos_mais_distantes([(4, 0), (2, 0), (0, 3), (0, -1)])
    ((4, 0), (0, 3))
    '''
    # a e b são os pontos mais distantes até o momento
    a = pontos[0]
    b = pontos[0]
    max_distancia = 0
    for p1 in pontos:
        for p2 in pontos:
            distancia_p1_p2 = distancia(p1, p2)
            if distancia_p1_p2 > max_distancia:
                a = p1
                b = p2
                max_distancia = distancia_p1_p2
    return a, b


def distancia(p1, p2):
    '''
    (float, float), (float, float) -> float
    Calcula a distancia cartesiana entre os pontos p1 e p2.
    Exemplos
    >>> distancia((7.0, 8.0), (4.0, 12.0))
    5.0
    '''
    x1, y1 = p1
    x2, y2 = p2
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def le_pontos_arquivo(arquivo):
    with open(arquivo) as f:
        pontos = []
        for linha in f.readlines():
            x, y = linha.split()
            pontos.append((float(x), float(y)))
        return pontos


def exibe_pontos_mais_distantes(a, b):
    print('Os pontos mais distantes são {} e {}.'.format(a, b))
    print('A distância entre eles é {}.'.format(distancia(a, b)))


if __name__ == "__main__":
    main()
