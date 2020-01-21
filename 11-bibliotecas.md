---
# vim: set spell spelllang=pt_br sw=4:
title: Bibliotecas
---

Introdução
==========

## Introdução

Até o momento, a maioria das funções que usamos nós mesmos que escrevemos.

\pause

Em programa reais, é comum o uso de muitas funções escritas por outras pessoas.
Além de funções, também podemos utilizar variáveis e tipos definidos por outras
pessoas. Estas definições são agrupadas em bibliotecas (módulos) de propósitos
específicos.

\pause

Veremos como usar bibliotecas existentes e como criar as nossas bibliotecas.


## Introdução

Para usar as funções de uma biblioteca precisamos importá-la com a instrução
`import`{.python}. Já usamos a instrução `import`{.python} em duas situação

1. Para importar a função `testmod`{.python} da biblioteca `doctest`{.python}

    ```python
    from doctest import testmod
    ```

2. Para importar a variável `sys.argv`{.python}

    ```python
    import sys
    ```



Biblioteca padrão
=================


## Biblioteca padrão

As funções pré-definidas do Python, como `int`{.python}, `print`{.python},
`len`{.python}, etc, podem ser usadas diretamente pois fazem parte de uma
biblioteca chamada `builtins`{.python} que é importada implicitamente.

Veja a lista de funções no módulo `builtins`{.python} em
\url{https://docs.python.org/3/library/functions.html}.


## Biblioteca padrão

A biblioteca padrão do Python é bastante extensa

- Um _slogan_ do Python é _baterias incluídas_

Vamos ver o exemplo de dois módulos: `math` e `random`

- Veja a lista completa das bibliotecas em \url{https://docs.python.org/3/library/index.html}


## Biblioteca `math`

O módulo `math` (\url{https://docs.python.org/3/library/math.html} provê
diversas funções e constantes matemáticas.

\pause

Exemplo importando o módulo

```python
>>> import math
>>> math.sin(math.pi / 4)
0.7071067811865475
```

\pause

Exemplo importando nomes específicos do módulo

```python
>>> from math import cos, pi, sqrt
>>> cos(pi / 4)
0.7071067811865476
>>> sqrt(2)
1.4142135623730951
```


## Biblioteca `random`

O módulo `random` (\url{https://docs.python.org/3/library/random.html} provê
diversas funções relacionadas com geração de números (pseudo) aleatórios.

\pause

Gerando número aleatórios em um intervalos

```python
from random import randint
>>> randint(5, 13)
7
```

\pause

Embaralhando os elementos de uma lista

```python
import random
>>> x = [1, 2, 3, 4, 5]
>>> random.shuffle(x)
>>> x
[3, 1, 5, 4, 2]
```


Definindo bibliotecas
=====================

## Definindo bibliotecas

Também podemos criar novas bibliotecas. Este assunto é extenso (veja um
tutorial em \url{https://docs.python.org/3/tutorial/modules.html}), mas de
forma básica podemos criar bibliotecas colocando funções em arquivos
diferentes.


## Definindo bibliotecas

Por exemplo, se criarmos um arquivo chamado `pontos.py` com o conteúdo

\scriptsize

```python
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
```

\normalsize

Podemos usar a função `distancia` em outro arquivo (no mesmo diretório de
`pontos.py`) fazendo um `import`

\scriptsize

```python
import pontos

print(pontos.distancia((1.0, 2.0), (3.0, 4.0)))
```


Bibliotecas externas
====================

## Bibliotecas externas

Por último, muitas bibliotecas externas estão disponíveis. Duas destas
bibliotecas (incluídas com a instalação do editor mu mas que não estão
incluídas na instalação padrão do Python) são

- Numpy (computação científica)

- matplotlib (geração de gráficos)



NumPy
=====

## NumPy

Biblioteca para computação científica

- Arranjos N-dimensionais
- Álgebra linear
- Números aleatórios
- etc


## NumPy

\small

```python
>>> import numpy as np
>>> a = np.array([1, 2, 3])
>>> a
array([1, 2, 3])
>>> a[1]
2
>>> b = np.array([[4, 5], [6, 7], [8, 9]])
>>> b
array([[4, 5],
       [6, 7],
       [8, 9]])
>>> b[2, 1]
9
>>> a @ b
array([40, 46])
```


matplotlib
==========

## matplotlib

Biblioteca para geração de gráficos

- Plotagem
- Histogramas
- Gráfico de barras
- etc


## matplotlib

```python
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0, 2, 100)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()
```

## matplotlib

![](imagens/matplotlib.pdf)


Referências
===========

## Referências

- [NumPy](https://numpy.org)
- [matplotlib](https://matplotlib.org/)
