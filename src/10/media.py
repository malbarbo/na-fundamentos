def main():
    print('Este programa calcula a média de 3 notas')
    a = float(input('Nota 1: '))
    b = float(input('Nota 2: '))
    c = float(input('Nota 3: '))
    m = media(a, b, c)
    print('A média é {0:.2f}'.format(m))


def media(a, b, c):
    '''
    Número, Número, Número -> Número
    Calcula a média dos valores a, b, c.
    Exemplos
    >>> media(1.0, 2.0, 3.0)
    2.0
    >>> media(3.0, 5.0, 10.0)
    6.0
    '''
    return (a + b + c) / 3


if __name__ == "__main__":
    main()
