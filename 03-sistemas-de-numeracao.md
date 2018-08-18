---
# vim: set spell spelllang=pt_br:
title: Sistemas de numeração
---

Introdução
==========

## Enigma

Em um universo virtual existe um planeta semelhante ao nosso. Os seres
inteligentes desse planeta são os _humenos_. Os seres _humenos_ são humanoides
que utilizam os mesmos algarismos que nós e o sistema de numeração deles foi
criado baseado nos mesmos princípios que o nosso sistema decimal. Uma caixa
fechada no mundo dos _humenos_ indica a quantidade de bombons dentro dela com
a inscrição 25. Na contagem decimal dos humanos existem 19 bombons na caixa.
\pause Quantos dedos nas mãos têm os _humenos_?



## Sistema de numeração

- Notação para representar números de um dado conjunto de forma consistente

- Exemplos
   - Sistema de numeração Romano
   - Sistema de numeração unário (cada número natural é representado pelo
     número de símbolos correspondente)
   - Sistema de numeração Hindu-Arábico (nosso sistema decimal)



Sistemas de numeração posicional
================================

## Notação posicional

- O nosso sistema decimal utiliza notação posicional
   - O valor de cada dígito (algarismo) é determinado pela sua posição
   - O valor do número representado é a soma do valor atribuído a cada dígito
     do número

## Notação posicional

- Por exemplo, cada dígito do número 6737 tem um valor que depende da sua
  posição

$$
\begin{array}{ccccccccc}
 6737  &\rightarrow&      6     &   &      7     &   &      3     &   &      7     \\
       &   &   \times   &   &   \times   &   &   \times   &   &   \times   \\
       &   &    10^3    &   &    10^2    &   &    10^1    &   &    10^0    \\
       &   & \downarrow &   & \downarrow &   & \downarrow &   & \downarrow \\
 6737  & = &    6000    & + &    700     & + &     30     & + &      7
\end{array}
$$



## Base de um sistema de numeração

- No sistema decimal são utilizados 10 dígitos distintos para representar os
  números

- Podemos utilizar outra quantidade qualquer (diferente de zero) para definir
  outros sistemas

- A quantidade de dígitos distintos utilizados em um sistema de numeração
  posicional é chamada de _base_

- O valor de um número representado na base $b$ pela sequência de dígitos $d_m
  d_{m-1} \dots d_1 d_0$ é
$$ d_m \times b^m + d_{m-1} \times b^{m - 1} + \cdots + d_1 \times b^1 + d_0 \times b^0$$



## Sistemas de numeração em computação

- Na computação é comum o uso de outras bases:
   - Binária (base 2)
      - $0, 1$
   - Octal (base 8)
      - $0, 1, 2, 3, 4, 5, 6, 7$
      - Usado para "abreviar" número binários (três dígitos binários
        correspondem a um dígito octal)
   - Hexadecimal (base 16)
      - $0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, D$
      - Usado para "abreviar" número binários (quadro dígitos binários
        correspondem a um dígito hexadecimal)



## Sistemas de numeração em computação

- No nível mais básico, os computadores modernos lidam apenas com o sistema
  binário
   - Todos dados armazenados e processados são descritos por uma sequência de
     dígitos binários



Conversão de base
=================

## Conversão de base

- Decimal para outra base
    - Método das divisões sucessivas
    - Exemplo da conversão de 23 na base decimal para binário

    | Número | Divisor | Resultado | Resto|
    |:------:|:-------:|:---------:|:----:|
    |   23   |    2    |    11     |   1  |
    |   11   |    2    |     5     |   1  |
    |    5   |    2    |     2     |   1  |
    |    2   |    2    |     1     |   0  |
    |    1   |    2    |     0     |   1  |

    - Ajuntando os restos de "baixo para cima" obtemos $10111$
    - Portanto $23_{10} = 10111_2$



## Conversão de base

- Outra base para decimal
    - Soma dos valores correspondente a cada dígito
    - Exemplo da conversão de 10111 em binário para decimal
    $$
    \begin{array}{ccccccccccc}
            1     & &      0     & &      1     & &      1     & &      1     & &\\
         \times   & &   \times   & &   \times   & &   \times   & &   \times   & &\\
           2^4    & &     2^3    & &     2^2    & &     2^1    & &     2^0    & &\\
       \downarrow & & \downarrow & & \downarrow & & \downarrow & & \downarrow & &\\
           16     &+&      0     &+&      4     &+&      2     &+&      1     &=& 23
    \end{array}
    $$
    - Portanto $10111_2 = 23_{10}$



Unidades de medidas de informação
===================================

## Unidades de medidas de informação

- Um _bit_ (dígito binário) é a unidade básica de informação usada na
  computação
   - Pode armazenar um de dois valores distintos (0 ou 1)

- Um _byte_ é uma sequência de 8 bits
   - Pode armazenar um de $2^8 = 256$ valores distintos


## Múltiplos (sistema internacional)

Nome     | Símbolo | Múltiplo | Quantidade
---------|---------|----------|----------
bit      |   b     |   10^0   | 1
kilobit  |   kb    |   10^3   | 1.000
megabit  |   Mb    |   10^6   | 1.000.000
gigabit  |   Gb    |   10^9   | 1.000.000.000

Nome     | Símbolo | Múltiplo | Quantidade
---------|---------|----------|----------
byte     |   B     |   10^0   | 1
kilobyte |   kB    |   10^3   | 1.000
megabyte |   MB    |   10^6   | 1.000.000
gigabyte |   GB    |   10^9   | 1.000.000.000


## Múltiplos (JEDEC / IEC)

Nome              | Símbolo | Múltiplo | Quantidade
------------------|---------|----------|----------
bit               |   b     |   2^0    | 1
kilobit/kibibit   |   kib   |   2^10   | 1.024
megabit/mebibit   |   Mib   |   2^20   | 1.048.576
gigabit/gibibit   |   Gib   |   2^30   | 1.073.741.824

Nome              | Símbolo | Múltiplo | Quantidade
------------------|---------|----------|----------
byte              |   B     |   2^0    | 1
kilobyte/kibibyte |   kiB   |   2^10   | 1.024
megabyte/mebibyte |   MiB   |   2^20   | 1.048.576
gigabyte/gibibyte |   GiB   |   2^30   | 1.073.741.824



Atividades
==========

## Atividades

@. Por que os computadores usam o sistema de numeração binário?

@. Explique como o computador podem armazenar informações que não são
   "naturalmente" numéricas (como áudio, vídeo, texto, etc).

## Atividades

@. Converta os seguintes números para decimal:
    - $1011001_2$
    - $161721_8$
    - FFA0$_{16}$

@. Converta os seguintes números para binário, octal e hexadecimal:
    - 1234
    - 4321
    - 1001

## Atividades

@. Quantos números distintos é possível representar no sistema decimal
   com 1, 5 e 10 dígitos?

@. Quantos números distintos é possível representar no sistema binário com 1,
   8, 16, 32 e 64 bits?
