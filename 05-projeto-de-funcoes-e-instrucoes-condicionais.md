---
# vim: set spell spelllang=pt_br sw=4:
title: Projeto de funções e instruções condicionais
---

Receita de projeto de funções
=============================

## Receita de projeto de funções

Podemos definir novas funções combinando as funções já existentes. Vamos seguir
uma receita para definir novas funções

1. Cabeçalho, contrato e propósito
    - nome da função e dos parâmetros e `return`
    - tipos dos dados de entrada e saída
    - descrição do que a função faz
2. Exemplos
3. Corpo
4. Teste


## Receita de projeto de funções

- Cada etapa depende da anterior, mas as vezes pode ser necessário mudar a ordem
- Por exemplo, talvez você faça primeiro os exemplos para entender melhor
  o problema e poder escrever a assinatura e o propósito
- As vezes você está escrevendo o corpo e encontra uma nova condição e deve
  voltar e alterar o propósito e os exemplos
- Mas você nunca deve escrever o código diretamente


## Exemplo 1

Defina uma função que produza o dobro de um dado valor.

## Exemplo 1

- Passo 1: cabeçalho - nome da função e dos parâmetros e `return`

    ```python
    def dobro(x):
        return
    ```


## Exemplo 1

- Passo 1: contrato - o que a função consome e produz - tipo dos dados de
  entrada e saída

    ```python
    def dobro(x):
        '''
        Número -> Número
        '''
        return
    ```


## Exemplo 1

- Passo 1: propósito - o que a função faz

    ```python
    def dobro(x):
        '''
        Número -> Número
        Produz o dobro de x.
        '''
        return
    ```


## Exemplo 1

- Passo 2: exemplos - resultado esperado para algumas entradas

    ```python
    def dobro(x):
        '''
        Número -> Número
        Produz o dobro de x.
        >>> dobro(3)
        6
        >>> dobro(-2)
        -4
        >>> dobro(4.3)
        8.6
        '''
        return
    ```


## Exemplo 1

- Passo 3: corpo - baseado nos passos anteriores, definir o corpo da função

    ```python
    def dobro(x):
        '''
        Número -> Número
        Produz o dobro de x.
        >>> dobro(3)
        6
        >>> dobro(4.3)
        8.6
        '''
        return 2 * x
    ```

## Exemplo 1

- Passo 4: testar - testar os exemplos na janela de interações

    ```python
    >>> dobro(3)
    6
    >>> dobro(4.3)
    8.6
    ```

## Exemplo 1

- Após definir uma função, podemos usá-la como qualquer outra função
  pré-definida

    ```python
    >>> dobro(4) + 2
    10
    >>> dobro(1 + dobro(abs(-7)))
    30
    ```


# Testes automatizados

## Testes automatizados

- O Python pode verificar automaticamente se todos os exemplos estão corretos

- Chamamos esta verificação de **teste automatizado**

- A linha a seguir deve ser incluída no início do arquivo

    ```python
    from doctest import testmod
    ```

- Para executar o teste automatizado, clique em "Correr" e execute a função
  `testemod` na janela de interações

    ```python
    >>> testmod()
    ```


## Testes automatizados

A checagem de um exemplo pode falhar por um de três motivos

- O exemplo está errado. Refaça o exemplo para ter certeza que ele está certo

- O programa está errado. Neste caso o programador cometeu um erro lógico e o
  corpo da função deve ser corrigido

- O exemplo e o programa estão errados. Este caso é difícil de acontecer, mas
  se depois de corrigir o exemplo e ter certeza que ele está certo, então o
  corpo da função também precisa ser corrigido


## Exemplo 2

Defina uma função que verifique se um número é par.



# Instruções condicionais

## Instruções condicionais

Forma preliminar do `if`

```python
if condição:
    consequente
else:
    alternativa
```


## Exemplo 3

Defina uma função que encontre o máximo entre dois valores dados.


## Exemplo 4

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


## Exemplo 5

Defina uma função que some o quadrado dos dois maiores valores entre três
valores dados.

## Exemplo 6

Defina uma função que receba como parâmetros os lados de um triângulo
e o classifique em escaleno, isósceles ou equilátero.

## Exemplo 7

Defina uma função que receba como parâmetros os coeficientes de uma equação de
segundo e determine as suas raízes. Considere as três possibilidades: uma raiz,
duas raízes ou nenhum raiz.



# Atividades

## Atividades

@. Use a função `par` definida em sala de aula para definir uma função `impar`
que verifique se um dado número é ímpar.

@. A empresa Feras da Engenharia paga R$ 50,00 por hora para um engenheiro.
Cada engenheiro trabalha em média de 20 a 50 horas por semana. Defina uma
função que calcule o salário de um engenheiro a partir do número de horas
trabalhada.


## Atividades

@. Defina uma função chamada `converte3` que receba como entrada três dígitos
de um número, começando pelo menos significativo, seguido pelo próximo mais
significativo, e assim por diante,  e produza o número correspondente. Por
exemplo: `converte3(6, 7, 2) = 276`.

@. Defina uma função que converta uma quantidade de segundos para horas,
minutos e segundos.


## Atividades

@. Defina uma função que verifique se três medidas podem formar um triângulo.
Para formar um triângulo a soma de qualquer duas medidas deve ser maior ou igual
do que a terceira medida.

@. Defina uma função que classifique o grau de obesidade de uma pessoa a partir
do IMC. Os dados de entrada devem ser o peso e a altura da pessoa. Veja
informações sobre IMC na
\href{https://pt.wikipedia.org/wiki/\%C3\%8Dndice_de_massa_corporal}{Wikipédia}.


## Atividades

@. O governo do estado deu uma aumento de salário para os funcionários
públicos. O percentual de aumento depende do valor do salário atual. Para
funcionários que ganham até R$ 1200 o aumento é de 10%, para funcionários que
ganham entre R$ 1200 e R$ 3000 o aumento é de 7%, para funcionários que ganham
entre R$ 3000 e R$ 8000, o aumento é de 3%, e finalmente, para os funcionários
que ganham mais que R$ 8000 não haverá aumento. Defina uma função que calcule
o novo salário a partir do salário atual.


## Atividades

@. Um número é palíndromo se quando lido da direita para a esquerda ou da
esquerda para a direita é idêntico. Ex: 9119, 1221, 5665, 7337. Defina uma
função que verifique se um dado número inteiro de 4 dígitos é palíndromo.
Considere que o valor de entrada é o próprio número e não os quatro dígitos que
compõem o número.
