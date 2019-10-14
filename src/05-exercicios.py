from doctest import testmod


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
