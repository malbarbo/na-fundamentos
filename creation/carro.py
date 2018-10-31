from creation import *

CORPO_CARRO = above(
    'center',
    rectangle(100, 30, fill('red')),
    rectangle(200, 30, fill('red')),
    rectangle(200, 30, fill('white'))
)

RODA = circle(25, fill('black'))

CARRO = place(
    RODA,
    'center', 160,
    'center', 65,
    place(
        RODA,
        'center', 40,
        'center', 65,
        CORPO_CARRO,
    )
)

image_view(CARRO)