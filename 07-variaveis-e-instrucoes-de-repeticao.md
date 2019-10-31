---
# vim: set spell spelllang=pt_br sw=4:
title: Variáveis e instruções de repetição
---

Introdução
==========

## Introdução

O valor $e ^ x$, onde $e$ é o número de Euler e $x$ um valor real qualquer,
pode ser calculado pela seguinte série de Taylor

$$e^x = \sum_{n = 0}^{\infty} \frac{x^n}{n!} = \frac{x^0}{0!} + \frac{x^1}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \dots $$

\pause

### Exercício

Calcule o valor de $e^2$ usando a série anterior.


## Introdução

\small

|   $n$    | dividendo ($x^n$) | divisor ($n!$) | termo ($\frac{x^n}{n!}$)        | soma ($e^x$) |
|:--------:|:-----------------:|:--------------:|:-------------------------------:|:------------:|
| 0        |        1          |       1        | $\frac{1}{1} = 1.0$             |     1.0      |
| \pause 1 |        2          |       1        | $\frac{2}{1} = 2.0$             |     3.0      |
| \pause 2 |        4          |       2        | $\frac{4}{2} = 2.0$             |     5.0      |
| \pause 3 |        8          |       6        | $\frac{8}{6} = 1.333333$        |   6.333333   |
| \pause 4 |       16          |       24       | $\frac{16}{24} = 0.666666$      |     7.0      |
| \pause 5 |       32          |      120       | $\frac{32}{120} = 0.266666$     |   7.266666   |
| \pause 6 |       64          |      720       | $\frac{64}{720} = 0.088888$     |   7.355555   |
| \pause 7 |      128          |     5040       | $\frac{128}{5040} = 0.0253968$  |   7.380952   |
| \pause 8 |      256          |    40320       | $\frac{256}{50320} = 0.0063492$ |   7.387301   |


## Introdução

Para todas as linhas, exceto a primeira

- O valor de $x^n$ foi obtido multiplicando o valor de $x^{n - 1}$ (isto é,
  $x^n$  da linha anterior) pelo valor de $x$ (Ex: $16 = 8 \times 2$)

- O valor de $n!$ foi obtido multiplicando o valor de $(n - 1)!$ (isto é, $n!$
  da linha anterior) pelo valor de $n$ (Ex: $120 = 24 \times 5$)

- O valor de $e^x$ foi obtido pelo valor de $e^x$ da linha anterior mais
  o valor de $\frac{x^n}{n!}$ (Ex: $7.26666 = 7.0 + 0.26666$)


## Introdução

- Veremos como expressar este tipo de processo com funções em Python

- Para isso precisamos

    - De instruções de repetição

    - Aprimorar nosso entendimento de variáveis



Variáveis
=========

## Variáveis

- Uma variável na matemática é um símbolo que representa um objeto matemático
  (número, vetor, função, etc)

    - Tem este nome porque os argumentos (variáveis) das funções podem variar

- Até agora pensamos em variáveis em Python como as variáveis na matemática

- Agora veremos que variáveis na computação podem não corresponder diretamente
  as variáveis em matemática


## Variáveis

- Uma variável na computação é um nome associado com uma célula de memória
  (local de armazenamento)

    - Na célula de memória associada com a variável é armazenado um valor
      (número, string, etc)


## Variáveis

- O fato de uma variável corresponder a uma célula de memória tem duas
  implicações

    - A célula de memória associada com a variável pode ser alterada

    - O valor armazenado na célula de memória associada com a variável pode ser
      alterado


## Variáveis

Considere o seguinte exemplo

\small

<div class="columns">
<div class="column" width="50%">
```python
>>> x = 10
>>> y = x
>>> x
10
>>> y
10
```

\pause

```python
>>> x = 20
>>> x
20
>>> y
```

\pause

```python
10
```
</div>

\pause

<div class="column" width="50%">
```python
>>> x = x + 3
>>> x
```

\pause

```python
23
```
</div>
</div>


## Variáveis

- Quando a instrução `x = 10`{.python} é executado o Python reserva uma célula
  de memória para o valor `10`{.python} e associa esta célula ao nome `x`

- Quando a instrução `y = x`{.python} é executada a célula de memória associada
  com `x` passa também a ser associada com `y`, ou seja, tanto `x` quando `y`
  estão associados com a mesma célula de memória


## Variáveis

- Quando a instrução `x = 20`{.python} é executado o Python reserva uma nova
  célula de memória para o valor `20`{.python} e associa esta célula com o nome
  `x`. Note que a memória associada com `y` não é alterada

- Quando a instrução `x = x + 3`{.python} é executada o Python lê o valor
  armazenado na célula de memória associado com `x` (`20`{.python}), soma com
  `3`{.python}, reserva uma nova célula de memória para o valor `23`{.python}
  e associa esta célula ao nome `x`. A célula de memória previamente associada
  com `x` fica a disposição para armazenar outro valor


## Variáveis

- A expressão `x = x + 3`{.python} parece estranha

    - Como `x` pode ser **igual** a `x + 3`{.python}!? \pause

    - **Pare!** \pause

    - O símbolo `=` representa igualdade na matemática, mas em Python ele tem
      outro significado


## Variáveis

- O símbolo `=` é chamado de atribuição em Python

    - A expressão `a = 10`{.python} (lê-se `a` recebe `10`{.python}) significa

        - Associe com o nome `a` uma célula de memória com o valor `10`{.python}

    - A expressão `a = 2 * a + 1`{.python} (lê-se `a` recebe duas vezes `a` mais 1) significa

        - Associe com o nome `a` uma célula de memória com o valor
          `2 * a + 1`{.python} (isto é, o valor da célula de memória atualmente
          associado com `a` multiplicado por `2`{.python} mais `1`{.python})


## Variáveis

- O valor do lado direto de `=` é uma expressão

    - Se a expressão for o nome de uma variável, nenhuma nova célula de memória
      é reservada

    - Se a expressão for uma constante ou uma expressão composta, ela
      é avaliada é o resultado é armazenado em uma nova célula de memória

- O valor do lado esquerdo de `=` deve ser um nome (que será associado com
  a célula de memória que contém o resultado da expressão do lado direito)

    - A expressão `10 = x`{.python} não é válida porque `10`{.python} não é um
      nome


## Variáveis

- Porque usar o mesmo nome para armazenar valores distintos? Não podemos usar
  um novo nome para armazenar cada valor? \pause

    - Sim podemos! É isso que temos feito até agora \pause

- Mas as vezes precisamos armazenar valores que estão sendo calculados, como
  a soma de uma série, e não sabemos quantos valores intermediários serão
  calculados. Como dar um nome diferente para cada valor se não sabemos de
  antemão quantos valores teremos?

    - Em geral, usamos a mesma variável para armazenar valores distintos em
      processos que envolvem repetição de instruções



Instruções de repetição
=======================

## Instruções de repetição

- Até agora vimos uma instrução de controle, a seleção (`if`{.python})

- Agora veremos outra instrução de controle, o enquanto (`while`{.python}), uma
  instrução de repetição


## Instruções de repetição

- A instrução `while`{.python} repete um conjunto de instruções até que uma
  determinada condição seja alcançada

- A forma preliminar do `while`{.python} é

    \small

    ```python
    while condicao:
        instrucoes
    ```

\normalsize
\pause

- Como o Python avalia uma instrução `while`{.python}? \pause

    - Ele primeiro avalia a expressão `condicao`, se o resultado for
      `True`{.python}, então ele executa o bloco `instrucoes` e volta para a
      linha do `while condicao`{.python} para repetir o processo. A repetição
      para quando o resultado de `condicao` for `False`{.python}.


## Instruções de repetição

Qual o valor de `i` após o término do `while`{.python}?

\small

```python
>>> i = 0
>>> while i != 5:
...    i = i + 1
...
>>> i
```

\vspace{-0.5cm}

\only<1>{?}
\only<2>{5}


## Instruções de repetição

Quais os valores de `i` e `n` após o término do `while`{.python}?

\small

```python
>>> i = 1
>>> n = 1
>>> while i <= 4:
...    n = n * i
...    i = i + 1
...
>>> (i, n)
```

\vspace{-0.5cm}

\only<1>{(?, ?)}
\only<2>{(5, 24)}


## Instruções de repetição

Quais os valores de `i`, `a` e `b` após o término do `while`{.python}?

\small

```python
>>> i = 0
>>> a = 0
>>> b = 1
>>> while i < 6:
...     t = b
...     b = a + b
...     a = t
...     i = i + 1
...
>>> (i, a, b)
```

\vspace{-0.5cm}

\only<1>{(?, ?, ?)}
\only<2>{(6, 8, 13)}


## Instruções de repetição

Quais os valores de `cont`, `n` e `i` após o término do `while`{.python}?

\small

```python
>>> cont = 0
>>> n = 10
>>> i = n
>>> while i > 0:
...     if n % i == 0:
...         cont = cont + 1
...     i = i - 1
...
>>> (cont, n, i)
```

\vspace{-0.5cm}

\only<1>{(?, ?, ?)}
\only<2>{(4, 10, 0)}


## Instruções de repetição

Dado a seguinte função

\small

```python
def fun(a, b):
    s = 0
    while a <= b:
        s = s + a
        a = a + 1
    return s
```

\normalsize

Quais os valores de `x` e `y` após a execução de `fun`?

\small

```python
>>> x = 3
>>> y = fun(x, x + 2)
>>> (x, y)
```

\vspace{-0.5cm}

\only<1>{(?, ?)}
\only<2>{(3, 12)}



# Exemplos


## Exemplo

Dado dois inteiros positivos $a$ e $b$, defina uma função que calcule o resto
da divisão de $a$ por $b$ usando uma sequência de subtrações.


## Exemplos

Seguindo a receita de projeto de funções obtemos

\small

```python
def resto(a, b):
    '''
    Inteiro Positivo, Inteiro Positivo -> Inteiro Positivo
    Calcula o resto da divisao de a por b usando uma
    sequência de subtrações.
    Exemplos
    >>> resto(18, 5)
    3
    >>> resto(16, 3)
    1
    >>> resto(8, 2)
    0
    '''
    return
```


## Exemplos

- O próximo passo é escrever o corpo!

- Os passos feitos até agora devem guiar a escrita do corpo da função

- Apesar de termos colocado o resultado dos exemplos diretamente (fizemos
  o cálculo "de cabeça"), neste momento é importante pensarmos em uma forma
  sistemática para obter os resultados dos exemplos

- A criação de uma tabela pode ajudar


## Exemplos

- Vamos considerar o exemplo `resto(18, 5)`{.python}. Como podemos obter
  o resultado `3`{.python} usando uma sequência de subtrações? \pause

- A ideia é ir subtraindo `5`{.python} de `18`{.python} enquanto isso for
  possível
    - `18 - 5`{.python} dá `13`{.python}
    - `13 - 5`{.python} dá `8`{.python}
    - `8 - 5`{.python} dá `3`{.python}
    - Não dá para subtrair `5`{.python} de `3`{.python}, portanto o resto da
      divisão de `18`{.python} por `5`{.python} é `3`{.python}


## Exemplos

Vamos escrever o resultado deste processo em uma tabela. Lembrando que estamos
calculando `resto(18, 5)`{.python}, portanto, temos `a = 18`{.python} e `b
= 5`{.python}. Precisamos apenas de uma coluna `resto`, que representa o valor
atual que vamos "tentar" subtrair `5`{.python} \pause

| `resto`  |
|:--------:|
|  18      |
| \pause 13|
| \pause 8 |
| \pause 3 |


## Exemplos

- A partir da tabela podemos responder as seguintes questões
    - Qual o valor inicial de `resto`?
      \pause `resto = a`{.python}
    - Como o valor de `resto` é atualizado a cada linha?
      \pause `resto = resto - b`{.python}
    - Qual a condição necessária para continuar o processo (as subtrações)?
      \pause `resto >= b`{.python}
    - Qual a expressão que define o resultado?
      \pause `resto`


## Exemplos

A partir da observações anteriores podemos escrever o corpo da função

\scriptsize

```python
def resto(a, b):
    # valor inicial de resto
    resto = a
    # condição necessária para continuar o processo
    while resto >= b:
        # como resto é atualizado
        resto = resto - b
    # expressão que define o resultado
    return resto
```


## Exemplo

Defina uma função que calcule o produto de dois números inteiros usando uma
sequência de somas.


## Exemplo

Seguindo a receita de projeto de funções obtemos

\small

```python
def multiplica(a, b):
    '''
    Inteiro Positivo, Inteiro Positivo -> Inteiro Positivo
    Calcula o produto entre a e b usando uma sequência de somas.
    Exemplos
    >>> multiplica(3, 4)
    12
    >>> multiplica(2, 5)
    10
    >>> multiplica(5, 0)
    0
    '''
    return
```


## Exemplo

- O próximo passo é escrever o corpo!

- Os passos feitos até agora devem guiar a escrita do corpo da função

- Como obter os resultados dos exemplos anteriores usando somas? \pause
$$ a \times b = \underbrace{a + a + \cdots + a}_{b\ \text{vezes}} = \sum_{n = 1}^{b} a$$


## Exemplo

Vamos calcular `multiplica(3, 4)`{.python} usando uma sequência de somas. Temos
que `a = 3`{.python} e `b = 4`{.python}, `n` representa quantas vezes o valor
de $a$ foi somado e `prod` é o valor parcial da soma

|   `n`    | `prod` (valor parcial de $a \times b$) |
|:--------:|:--------------------------------------:|
|  0       |                 0                      |
| \pause 1 |                 3                      |
| \pause 2 |                 6                      |
| \pause 3 |                 9                      |
| \pause 4 |                12                      |


## Exemplo

A partir da tabela podemos responder as seguintes questões

- Qual o valor inicial de `n` e `prod`?
  \pause `n = 0`{.python} e `prod = 0`{.python}
- Como os valores de `n` e `prod` são atualizados (como os valores de uma linha
  são calculados usando os valores da linha anterior)?
  \pause `n = n + 1`{.python} (soma `1`{.python} no valor da linha anterior)
  e `prod = prod + a`{.python} (soma `a`{.python} no valor da linha anterior)
- Qual a condição necessária para continuar o processo?
  \pause `n != b`{.python}
- Qual a expressão que define o resultado?
  \pause `prod`


## Exemplo

A partir da observações anteriores podemos escrever o corpo da função

\scriptsize

```python
def multiplica(a, b):
    # valor inicial de n e prod
    n = 0
    prod = 0
    # condição necessária para repetir o processo
    while n != b:
        # como o valor de n é atualizado
        n = n + 1
        # como o valor de prod é atualizado
        prod = prod + a
    # a expressão que define o resultado
    return prod
```


## Exemplo

Dado dois número inteiros positivos $a$ e $b$, defina uma função que calcule
o valor $a^b$ usando uma sequência de multiplicações.


## Exemplo

Dado dois número inteiros positivos $a$ e $b$, onde $a < b$, defina uma função
que conte a quantidade de números no intervalo $[a, b]$ que sejam múltiplos de
3 e 5 ao mesmo tempo.


## Exemplo

O hiperfatorial de um número natural $n$ é definido como $$H(n) = \prod_{k
= 1}^{n} k^k = 1^1 \times 2^2 \times 3^3 \times \cdots \times (n - 1)^{n - 1}
\times n^n$$ Defina uma função que calcule o hiperfatorial de um dado número.


## Exemplo

Defina uma função que calcule o valor $e^x$, para um dado $x$, usando a série
$$e^x = \sum_{n = 0}^{\infty} \frac{x^n}{n!} = \frac{x^0}{0!} + \frac{x^1}{1!} + \frac{x^2}{2!} + \frac{x^3}{3!} + \frac{x^4}{4!} + \dots $$



Atividades
==========


## Atividades

@. Dado dois inteiros positivos $a$ e $b$, defina uma função que calcule
   a divisão inteira de $a$ por $b$ usando uma sequência de subtrações.

@. O superfatorial de um número natural $n$ é definido como o produto dos
   primeiros $n$ fatoriais, isto é
   $$sf(n) = \prod_{k = 1}^{n} k! = 1! \times 2! \times 3! \times \cdots \times (k - 1)! \times k!$$
   Defina uma função que calcule o superfatorial de um dado número


## Atividades

@. Defina uma função que calcule o valor $\sin x$, para um dado $x$ em radianos, usando a série
$$\sin x = \sum^{\infty}_{n=0} \frac{(-1)^n}{(2n+1)!} x^{2n+1} = x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$$

@. Defina uma função que calcule o valor $\cos x$, para um dado $x$ em radianos, usando a série
$$\cos x = \sum^{\infty}_{n=0} \frac{(-1)^n}{(2n)!} x^{2n} = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$$


## Atividades

Este exercício já fez parte de uma prova!

@. Defina uma função que receba como parâmetro um valor $n$ e calcule o valor
   aproximado de $\pi$ usando os primeiros $n$ termos da série

   $$\pi = 4 \sum_{k=0}^{\infty} \frac{(-1)^k}{2 k + 1}
       = 4 \left ( \frac{1}{1} - \frac{1}{3} + \frac{1}{5} - \frac{1}{7} + \frac{1}{9} - \cdots  \right)$$


## Atividades

@. Defina uma função que verifique se um dado número inteiro positivo
é perfeito. Um número é perfeito se a soma dos seus divisores (excluindo ele
mesmo) é igual a ele próprio. Por exemplo, 6 é um número perfeito pois $6
= 1 + 2 + 3$.

@. Defina uma função que verifique se um dado número inteiro positivo é primo.
Um número inteiro positivo é primo se ele tem apenas dois divisores distintos,
1 e ele mesmo.

## Atividades

@. Dado um número inteiro positivo $n \ge 4$, defina uma função que devolva
dois números $a$ e $b$, tal que $a$ e $b$ sejam primos e $n = a + b$.


## Leitura recomendada

- \href{https://penseallen.github.io/PensePython2e/}{Livro Pense em Python} 2ª edição. Allen B. Downey

    - \href{https://penseallen.github.io/PensePython2e/07-iteracao.html}{Capítulo
      7 - Iteração}

