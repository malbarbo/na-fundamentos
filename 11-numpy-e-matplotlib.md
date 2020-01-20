---
# vim: set spell spelllang=pt_br sw=4:
title: Numpy e matplotlib
---

Introdução
==========

## Introdução

Até o momento, a maioria das funções que usamos nós mesmos que escrevemos.

\pause

Em programa reais, é comum o uso de muitas funções escritas por outras pessoas.
Além de funções, também podemos utilizar variáveis e tipos definidos por outras
pessoas. Estas definições são agrupadas em bibliotecas (módulos) propósitos
específicos.

\pause

Veremos como usar bibliotecas existentes e como criar as nossas bibliotecas.


## Introdução

Para usar as funções de uma biblioteca precisamos importá-la com a instrução
`import`{.python}. Já usamos a instrução `import`{.python} em duas situação

1. Para importar a função `testmod`{.python} da biblioteca `doctest`{.python}

    ```
    from doctest import testmod
    ```

2. Para importar a variável `sys.argv`{.python}

    ```
    import sys
    ```


## Introdução

As funções pré-definidas do Python, como `int`{.python}, `print`{.python},
`len`{.python}, etc, podem ser usadas diretamente pois fazem parte de uma
biblioteca chamada `builtins`{.python} que é importada implicitamente.

Veja a lista de funções em \url{https://docs.python.org/3/library/functions.html}.


## Introdução

A biblioteca padrão do Python é bastante extensa

- Um _slogan_ do Python é _baterias incluídas_

Além disso, muitas bibliotecas externas estão disponíveis. Duas destas
bibliotecas (incluídas com a instalação do editor mu) são

- Numpy (computação científica)

- matplotlib (geração de gráficos)



NumPy
=====

## NumPy

- Biblioteca para computação científica

    - Arranjos N-dimensionais
    - Álgebra linear
    - Números aleatórios
    - etc


## NumPy

- Exemplo multiplicação de matrizes

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

- Biblioteca para geração de gráficos

    - Plotagem
    - Histogramas
    - Gráfico de barras
    - etc


## matplotlib

- Exemplo

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

- [NumPy](https://numpy.or)
- [matplotlib](https://numpy.or)
