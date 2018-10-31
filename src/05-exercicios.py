from doctest import testmod


def par(x):
    '''
    Número -> Booleano
    Devolve True se x é um número par, isto é, se x é múltiplo de 2.
    Exemplos
    >>> par(7)
    False
    >>> par(4)
    True
    '''
    return x % 2 == 0


def impar(x):
    '''
    Número -> Booleano
    Devolve True se x é um número impar, False caso contrário.
    Exemplos
    >>> impar(7)
    True
    >>> impar(4)
    False
    '''
    return not par(x)


def impar_alternativa(x):
    '''
    Número -> Booleano
    Devolve True se x é um número impar, False caso contrário.
    Exemplos
    >>> impar_alternativa(7)
    True
    >>> impar_alternativa(4)
    False
    '''
    if par(x):
        r = False
    else:
        r = True
    return r


def salario(horas):
    '''
    Número -> Número
    Calcula o salário de um engenheiro a partir do número de horas trabalhadas.
    Exemplos
    >>> salario(10)
    500
    >>> salario(20)
    1000
    '''
    return 50 * horas


def converte3(unidade, dezena, centena):
    '''
    Número, Número, Número -> Número
    Converte os valores da unidade, da dezena e da centena para um número
    composto por estes dígitos.
    Exemplos
    >>> converte3(6, 7, 2)
    276
    >>> converte3(1, 2, 3)
    321
    '''
    return centena * 100 + dezena * 10 + unidade * 1


def converte_hms(segundos):
    '''
    Número -> Número, Número, Número
    Converte um tempo dado em segundos para horas, minutos, segundos.
    Exemplos
    >>> converte_hms(304)
    (0, 5, 4)
    >>> converte_hms(4212)
    (1, 10, 12)
    >>> converte_hms(7456)
    (2, 4, 16)
    '''
    h = segundos // 3600
    m = (segundos % 3600) // 60
    s = (segundos % 3600) % 60
    return (h, m, s)


def eh_triangulo(a, b, c):
    '''
    Número, Número, Número -> Booleano
    Devolve True se três medidas podem formar um triângulo, False caso
    contrário. Para forma um triângulo a soma de duas medidas quaisquer deve
    ser maior ou igual do que a outro medida.
    Exemplos
    >>> eh_triangulo(3, 4, 5)
    True
    >>> eh_triangulo(6, 4, 3)
    True
    >>> eh_triangulo(4, 7, 3)
    True
    >>> eh_triangulo(3, 1, 5)
    False
    >>> eh_triangulo(4, 8, 2)
    False
    >>> eh_triangulo(6, 1, 3)
    False
    '''
    return a + b >= c and a + c >= b and b + c >= a


def novo_salario(salario):
    '''
    Número -> Número
    Calcula o novo salário a partir do salário atual. Salários até 1200 tem
    aumento de 10%, salários de 1200 a 3000 tem aumento de 7%, salários de 3000
    a 8000 tem aumento de 3% e salários maiores do que 8000 não tem aumento.
    Exemplos
    >>> novo_salario(1000)
    1100.0
    >>> novo_salario(2000)
    2140.0
    >>> novo_salario(5000)
    5150.0
    >>> novo_salario(9000)
    9000.0
    '''
    if salario <= 1200:
        f = 1.1
    elif salario <= 3000:
        f = 1.07
    elif salario <= 8000:
        f = 1.03
    else:
        f = 1.0
    return salario * f


def eh_palindromo(x):
    '''
    Número -> Booleano
    Devolve True se um número de quatro dígitos é palíndromo e False caso
    contrário. Um número é palíndromo se quando lido da direita para a esquerda
    ou da esquerda para a direita é idêntico.
    Exemplos
    >>> eh_palindromo(9119)
    True
    >>> eh_palindromo(1221)
    True
    >>> eh_palindromo(1222)
    False
    >>> eh_palindromo(3112)
    False
    '''
    milhar = (x % 10000) // 1000
    centena = (x % 1000) // 100
    dezena = (x % 100) // 10
    unidade = (x % 10) // 1
    return milhar == unidade and centena == dezena