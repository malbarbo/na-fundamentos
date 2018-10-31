# Um retângulo sobreposto a uma elipse
overlay(
    'center', # alinhamento no eixo x
    'center', # alinhamento no eixo y
    rectangle(30, 60, fill('orange', 0.5)),
    ellipse(60, 30, fill('purple'))
)
# Um retângulo sobreposto a uma elipse
overlay(
    'right',  # alinha as figuras pela direita
    'center',
    rectangle(30, 60, fill('orange', 0.5)),
    ellipse(60, 30, fill('purple'))
)
# Um retângulo sobreposto a uma elipse
overlay(
    'left',   # alinha as figuras pela esquerda
    'center',
    rectangle(30, 60, fill('orange', 0.5)),
    ellipse(60, 30, fill('purple'))
)
# Um retângulo sobreposto a uma elipse
overlay(
    'center',
    'top',    # alinha as figuras pelo topo
    rectangle(30, 60, fill('orange', 0.5)),
    ellipse(60, 30, fill('purple'))
)
# Um retângulo sobreposto a uma elipse
overlay(
    'center',
    'bottom', # alinha as figuras pela base
    rectangle(30, 60, fill('orange', 0.5)),
    ellipse(60, 30, fill('purple'))
)
# Um retângulo sobreposto a uma elipse
overlay(
    'left',   # alinha as figuras pela esquerda
    'bottom', # alinha as figuras pela base
    rectangle(30, 60, fill('orange', 0.5)),
    ellipse(60, 30, fill('purple'))
)
# Mais que duas imagens
overlay(
    'center',
    'center',
    circle(5, fill('red')),
    circle(10, fill('black')),
    circle(15, fill('red')),
    circle(20, fill('black')),
    circle(25, fill('red')),
)
