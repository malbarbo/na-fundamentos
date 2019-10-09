---
# vim: set spell spelllang=pt_br sw=4:
title: Projeto de funções e instruções condicionais
---

Receita de projeto de funções
=============================

## Receita de projeto de funções

Podemos definir novas funções combinando as funções já existentes. Vamos seguir
uma receita para definir novas funções

1. Cabeçalho: nome da função e dos parâmetros e `return`{.python}
2. Contrato: tipos dos dados de entrada e saída
3. Propósito: descrição do que a função faz
4. Exemplos: saída produzida para algumas entradas
5. Corpo: o código da função
6. Teste: verifica se a função se comporta como nos exemplos


## Receita de projeto de funções

- Cada etapa depende da anterior, mas as vezes pode ser necessário mudar a ordem

- Por exemplo, talvez você faça primeiro os exemplos para entender melhor
  o problema e poder escrever o contrato e o propósito

- As vezes você está escrevendo o corpo e encontra uma nova condição e deve
  voltar e alterar o propósito e os exemplos

- Mas você nunca deve escrever o código diretamente


## Exemplo 1

Defina uma função que produza o dobro de um dado valor.


## Exemplo 1

- Passo 1: cabeçalho - nome da função e dos parâmetros e `return`{.python}

    ```python
    def dobro(x):
        return
    ```


## Exemplo 1

- Passo 2: contrato - o que a função consome e produz - tipo dos dados de
  entrada e saída

    ```python
    def dobro(x):
        '''
        Número -> Número
        '''
        return
    ```


## Exemplo 1

- Passo 3: propósito - o que a função faz

    ```python
    def dobro(x):
        '''
        Número -> Número
        Produz o dobro de x.
        '''
        return
    ```


## Exemplo 1

- Passo 4: exemplos - resultado esperado para algumas entradas

    ```python
    def dobro(x):
        '''
        Número -> Número
        Produz o dobro de x.
        Exemplos
        >>> dobro(3)     # 2 * 3
        6
        >>> dobro(-2.1)  # 2 * -2.1
        -4.2
        '''
        return
    ```

- Para cada exemplo podemos escrever após o sinal `#`{.python} como o resultado
  foi obtido. Esta informação pode ajudar na escrita do corpo da função


## Exemplo 1

- Passo 5: corpo - o código da função

    ```python
    def dobro(x):
        '''
        Número -> Número
        Produz o dobro de x.
        Exemplos
        >>> dobro(3)     # 2 * 3
        6
        >>> dobro(-2.1)  # 2 * -2.1
        -4.2
        '''
        return 2 * x
    ```


## Exemplo 1

- Passo 6: teste - a função se comporta como nos exemplos? Testamos na janela de
  iterações

    ```python
    >>> dobro(3)
    6
    >>> dobro(-2.1)
    -4.2
    ```



# Testes automatizados

## Testes automatizados

- O Python pode verificar automaticamente se todos os exemplos estão corretos

- Chamamos esta verificação de **teste automatizado**

- A linha a seguir deve ser incluída no início do arquivo

    ```python
    from doctest import testmod
    ```

- Para executar o teste automatizado, clique em "Executar" e chame a função
  `testemod` na janela de interações

    ```python
    >>> testmod()
    ```


## Testes automatizados

A checagem de um exemplo pode falhar por um de três motivos

- O exemplo está errado. Refaça o exemplo para ter certeza que ele está certo

- O programa está errado. Neste caso o programador cometeu um erro lógico e o
  corpo da função deve ser corrigido

- O exemplo e o programa estão errados.


## Exemplo 2

Defina uma função que verifique se um número é par.


## Exemplo 2

- Passo 1: cabeçalho - nome da função e dos parâmetros e `return`{.python}

    ```python
    def par(x):
        return
    ```


## Exemplo 2

- Passo 2: contrato - o que a função consome e produz - tipo dos dados de
  entrada e saída

    ```python
    def par(x):
        '''
        Inteiro positivo -> Boolean
        '''
        return
    ```


## Exemplo 2

- Passo 3: propósito - o que a função faz

    ```python
    def par(x):
        '''
        Inteiro positivo -> Boolean
        Produz True se x é um número par, False caso contrário
        '''
        return
    ```


## Exemplo 2

- Passo 4: exemplos - resultado esperado para algumas entradas

    ```python
    def par(x):
        '''
        Inteiro positivo -> Boolean
        Produz True se x é um número par, False caso contrário
        Exemplos
        >>> par(4) # 4 % 2 == 0
        True
        >>> par(7) # 7 % 2 == 0
        False
        '''
        return
    ```


## Exemplo 2

- Passo 5: corpo - o código da função

    ```python
    def par(x):
        '''
        Inteiro positivo -> Boolean
        Produz True se x é um número par, False caso contrário
        Exemplos
        >>> par(4) # 4 % 2 == 0
        True
        >>> par(7) # 7 % 2 == 0
        False
        '''
        return x % 2 == 0
    ```


## Exemplo 2

- Passo 6: teste - a função se comporta como nos exemplos? Testamos na janela
  de iterações

    ```python
    >>> par(4)
    True
    >>> par(7)
    False
    ```


## Exemplo 3

Defina uma função que encontre o máximo entre dois valores dados.


## Exemplo 3

- Passo 1: cabeçalho - nome da função e dos parâmetros e `return`{.python}

    ```python
    def maximo(a, b):
        return
    ```


## Exemplo 3

- Passo 2: contrato - o que a função consome e produz - tipo dos dados de
  entrada e saída

    ```python
    def maximo(a, b):
        '''
        Número, Número -> Número
        '''
        return
    ```


## Exemplo 3

- Passo 3: propósito - o que a função faz

    ```python
    def maximo(a, b):
        '''
        Número, Número -> Número
        Devolve o valor máximo entre a e b.
        '''
        return
    ```


## Exemplo 3

- Passo 4: exemplos - resultado esperado para algumas entradas

    ```python
    def maximo(a, b):
        '''
        Número, Número -> Número
        Devolve o valor máximo entre a e b.
        Exemplos
        >>> maximo(2, 4) # ????
        4
        >>> maximo(7, 4) # ????
        7
        '''
        return
    ```

\pause

- Ops! Até sabemos os resultados esperados dos exemplos, mas como computar
  estes valores?


# Instruções condicionais

## Instruções condicionais

- As instruções condicionais permitem que um programa execute instruções
  diferentes dependendo do valor de uma determinada condição

- A instrução condicional mais comum nas linguagens de programação é o `if`{.python}
  (_se_ em português)

- No caso da função `maximo`, temos que usar a instrução `if`{.python}


## Instruções condicionais

A forma preliminar do `if`{.python} é

```python
if condição:
    consequente
else:
    alternativa
```


## Instruções condicionais

Podemos pensar nos exemplos da função máximo da seguinte forma

```python
>>> maximo(7, 4) # 7 > 4 = True, produz 7
7
>>> maximo(2, 4) # 2 > 4 = False, produz 4
4
```

\pause

Escrevendo a instrução condicional temos

```python
def maximo(a, b):
    if a > b:
        m = a
    else:
        m = b
    return m
```


## Exemplo 4

Escreva uma função que receba como entrada a cor atual de um semáforo de
trânsito e devolva a próxima cor que será ativada (considere um semáforo com
três cores: verde, amarelo e vermelho).


## Exemplo 5

Defina uma função que encontre o máximo entre três valores dados.


## Instruções condicionais

Forma geral do `if`

```python
if condição_1:
    consequente_1
elif condição_2:
    consequente_2
...
elif condição_n:
    consequente_n
else:
    alternativa
```


## Entendendo como um programa é executado

<div class="columns">
<div class="column" width="50%">
Dado a função:

\footnotesize

```python
def f(x, y, z):
    if x >= y:
        if x >= z:
            m = x
        else:
            m = z
    else:
        if y >= z:
            m = y
        else:
            m = z
    return m
```
</div>
<div class="column" width="50%">
Qual o resultado produzido por:

```python
>>> f(4, 5, 2)
?
>>> f(2, 2, 3)
?
```
</div>
</div>


## Exemplo 6

Defina uma função que receba como parâmetros os lados de um triângulo
e o classifique em escaleno, isósceles ou equilátero.


## Exemplo 7

Defina uma função que receba como parâmetros os coeficientes de uma equação de
segundo grau e determine as suas raízes. Considere as três possibilidades: uma
raiz, duas raízes ou nenhum raiz.



# Atividades

## Atividades

@. A empresa Feras da Engenharia paga R$ 50,00 por hora para um engenheiro.
Cada engenheiro trabalha em média de 20 a 50 horas por semana. Defina uma
função que calcule o salário de um engenheiro a partir do número de horas
trabalhada.


## Atividades

@. Defina uma função que converta uma quantidade de segundos para horas,
minutos (até 60) e segundos (até 60).

@. Defina uma função que verifique se três medidas podem formar um triângulo.
Para formar um triângulo a soma de qualquer duas medidas deve ser maior ou
igual do que a terceira medida.


## Atividades

@. O governo do estado deu uma aumento de salário para os funcionários
públicos. O percentual de aumento depende do valor do salário atual. Para
funcionários que ganham até R$ 1200 o aumento é de 10%, para funcionários que
ganham entre R$ 1200 e R$ 3000 o aumento é de 7%, para funcionários que ganham
entre R$ 3000 e R$ 8000, o aumento é de 3%, e finalmente, para os funcionários
que ganham mais que R$ 8000 não haverá aumento. Defina uma função que calcule o
novo salário a partir do salário atual.


## Atividades

@. Um número é palíndromo se quando lido da direita para a esquerda ou da
esquerda para a direita é idêntico. Ex: 9119, 1221, 5665, 7337. Defina uma
função que verifique se um dado número inteiro de 4 dígitos é palíndromo.
Considere que o valor de entrada é o próprio número e não os quatro dígitos que
compõem o número.


## Atividades

Este exercício já fez parte de uma prova!

@. Um construtor precisa calcular a quantidade de azulejos necessários pra
azulejar uma determinada parede. Cada azulejo é quadrado e tem 20cm de lado.
Ajude o construtor e defina uma função que receba como entrada o comprimento e
a altura em metros de uma parede e calcule a quantidade de azulejos inteiros
necessários para azulejar a parede. Considere que o construtor nunca perde um
azulejo e que recortes de azulejos não são reaproveitados. (Dica: use divisão
pelo piso `//`)


## Atividades

Este exercício já fez parte de uma prova!

@. A nota final em um disciplina é calculada pela média simples de 4 avaliações
que valem de 0 a 10. A partir da nota final os alunos ficam em um de três
situações: Aprovado, alunos com nota final maior ou igual a 7. Reprovado,
alunos com nota menor que 4. Exame, alunos com nota maior igual a 4 e menores
que 7. Defina uma função que indique a situação de um aluno dado as 4 notas das
suas avaliações.


## Atividades

Este exercício já fez parte de uma prova!

@. Cada cidadão de um país, cuja moeda chama dinheiro, tem que pagar imposto
sobre a sua renda. Cidadãos que recebem até 1000 dinheiros pagam 5% de imposto.
Cidadãos que recebem entre 1000 e 5000 dinheiros pagam 5% de imposto sobre 1000
dinheiros e 10% sobre o que passar de 1000. Cidadãos que recebem mais do 5000
dinheiros pagam 5% de imposto sobre 1000 dinheiros, 10% de imposto sobre 4000
dinheiros e 20% sobre o que passar de 5000. Defina uma função que calcule o
imposto que um cidadão deve pagar dado a sua renda.
