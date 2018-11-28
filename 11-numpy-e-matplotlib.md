---
# vim: set spell spelllang=pt_br sw=4:
title: Numpy e matplotlib
---

Introdução
==========

## Introdução

- A biblioteca padrão do Python é bastante extensa

    - Um _slogan_ do Python é _baterias incluídas_

- Além disso, muitas bibliotecas externas estão disponíveis

- Duas destas bibliotecas (incluídas no editor mu) são

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
