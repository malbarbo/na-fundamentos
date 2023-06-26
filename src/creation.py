# Veja exemplos de uso das funções no material disponível na página.
#
# Versão 0.1 - 13/05/2018


def square(side, mode):
    '''
    Float, Mode -> Image
    Cria um quadrado com o tamanho do lado `side` e com a pintura `mode`.
    '''
    return Square(side, mode)


def rectangle(width, height, mode):
    '''
    Float, Float, Mode -> Image
    Cria um retângulo com o tamanho width x height e com a pintura `mode`.
    '''
    return Rectangle(width, height, mode)


def triangle(side, mode):
    '''
    Float -> Image
    Cria um triângulo equilátero com o tamanho do lado `side` e com a pintura
    `mode`.
    '''
    return Triangle(side, mode)


def circle(radius, mode):
    '''
    Float, Mode -> Image
    Cria um círculo com radio `radius` e com a pintura `mode`.
    '''
    return Circle(radius, mode)


def ellipse(width, height, mode):
    '''
    Float, Float, Mode -> Image
    Cria uma elipse com o tamanho width x height e com a pintura `mode`.
    '''
    return Ellipse(width, height, mode)


def text(text, size, color):
    '''
    String, Float, Mode -> Image
    Cria uma imagem do texto com altura da fonte size (em pixels) e com a
    pintura `mode`.
    '''
    return Text(text, size, color)


def pixmap(path):
    '''
    String -> Image
    Lê o arquivo especificado por path e cria uma imagem.
    '''
    return _pixmap(path)


def beside(align, *images):
    '''
    String, Imagem... -> Imagem
    Cria uma imagem colocando todas as imagens passadas como parâmetro uma ao
    lado da outra alinhadas de acordo com o parâmetro align (que pode ser
    'top', 'center' ou 'bottom')
    '''
    return Beside(align, images)


def above(align, *images):
    '''
    String, Imagem... -> Imagem
    Cria uma imagem colocando todas as imagens passadas como parâmetro uma
    embaixo da outra alinhadas de acordo com o parâmetro align (que pode ser
    'left', 'center' ou 'right')
    '''
    return Above(align, images)


def overlay(x_align, y_align, *images):
    '''
    String, String, Imagem... -> Imagem
    Cria uma imagem colocando todas as imagens passadas como parâmetro uma
    sobre a outra (a primeira imagem fica por cima) alinhadas de acordo com os
    parâmetro x_align (que pode ser 'left', 'center' ou 'right') e y_align (que
    pode ser 'left', 'center' ou 'right')
    '''
    return Overlay(x_align, y_align, images)


def place(image, x_align, x, y_align, y, scene):
    '''
    Image, String, Float, String, float, Image -> Image
    Cria uma imagem adicionando image sobre scene na coordenada (x, y) e
    recorda o resultado para ficar do tamanho de scene. A imagem é ancorada
    pelos alinhamentos x_align e y_align.
    '''
    return Place(image, x_align, x, y_align, y, scene)


def color(red, green, blue, alpha=255):
    '''
    Inteiro, Inteiro, Inteiro, Inteiro -> Color
    Cria uma cor no modelo RGBA. Cada valor deve estar no intervalo 0..255.
    '''
    return Color(red, green, blue, alpha)


def fill(color, opacity=1.0):
    '''
    Color ou String, Float -> Preenchimento
    Cria um preenchimento a partir de uma cor ou nome de cor e opacidade. O
    valor da opacidade é restrito ao intervalo 0..1.
    '''
    return _fill(color, opacity)


def image_width(image):
    '''
    Image -> Float
    Devolve a largura da imagem.
    '''
    return image.width


def image_height(image):
    '''
    Image -> Float
    Devolve a altura da imagem.
    '''
    return image.height


def image_view(image):
    '''
    Image -> Nada
    Abre uma janela e exibe a imagem.
    '''
    _image_view(image)


def image_save(image, filename):
    '''
    Image, String -> Nada
    Grava a imagem no formato svg no arquivo `filename`.
    '''
    _image_save(image, filename)


def create(world, to_draw, on_tick=None, ticks_per_second=None, on_key=None):
    return _create(world, to_draw, on_tick=on_tick, ticks_per_second=ticks_per_second, on_key=on_key)


#######################################
# Implementation section

import sys
from dataclasses import dataclass, replace
from typing import List
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen, QPolygon, QFont, QFontMetricsF, QPixmap
from PyQt5.QtCore import QPoint, QTimer, Qt, QSize, QRect
from PyQt5.QtSvg import QSvgGenerator

#######################################
# Paint modes


class Mode:
    pass


@dataclass
class Color(Mode):
    red: int
    green: int
    blue: int
    alpha: int = 255

    def with_alpha(self, alpha):
        return replace(self, alpha=alpha)

    def by_name(name):
        c = name.upper()
        if c in Color.__dict__:
            return Color.__dict__[c]
        raise Exception('Invalid color name: {}'.format(name))

    def _qcolor(self):
        return QColor(self.red, self.green, self.blue, self.alpha)


@dataclass
class Fill(Mode):
    color: Color


def _fill(color, opacity):
    if type(color) == str:
        color = Color.by_name(color)
    elif type(color) != Color:
        raise Exception('Invalid color: {}'.format(color))
    opacity = max(0.0, min(1.0, opacity))
    return Fill(color.with_alpha(round(opacity * color.alpha)))


def config_painter(painter, mode):
    if type(mode) == str:
        painter.setBrush(QColor(255, 255, 255, 0))
        painter.setPen(Color.by_name(mode)._qcolor())
    elif type(mode) == Color:
        painter.setBrush(QColor(255, 255, 255, 0))
        painter.setPen(mode._qcolor())
    elif type(mode) == Fill:
        painter.setBrush(mode.color._qcolor())
        painter.setPen(QColor(255, 255, 255, 0))
    else:
        raise Exception('Invalid mode: {}'.format(mode))


#######################################
# Primitive images
#
# TODO: create Rhombus, Star, RegularPolygon


class Image:
    pass


@dataclass
class Square(Image):
    side: float
    mode: Mode

    @property
    def width(self):
        return self.side

    @property
    def height(self):
        return self.side

    def draw(self, painter, origin):
        config_painter(painter, self.mode)
        painter.drawRect(origin[0], origin[1], self.side, self.side)


@dataclass
class Rectangle(Image):
    width: float
    height: float
    mode: Mode

    def draw(self, painter, origin):
        config_painter(painter, self.mode)
        painter.drawRect(origin[0], origin[1], self.width, self.height)


@dataclass
class Triangle(Image):
    side: float
    mode: Mode

    @property
    def width(self):
        return self.side

    @property
    def height(self):
        return round((3/4) ** 0.5 * self.side)

    def draw(self, painter, origin):
        config_painter(painter, self.mode)
        a = QPoint(origin[0], origin[1] + self.height)
        b = QPoint(origin[0] + self.side, origin[1] + self.height)
        c = QPoint(round(origin[0] + self.side / 2), origin[1])
        points = QPolygon()
        points.append(a)
        points.append(b)
        points.append(c)
        painter.drawPolygon(points)


@dataclass
class Circle(Image):
    radius: float
    mode: Mode

    @property
    def width(self):
        return 2 * self.radius

    @property
    def height(self):
        return 2 * self.radius

    def draw(self, painter, origin):
        config_painter(painter, self.mode)
        painter.drawEllipse(origin[0], origin[1], self.width, self.height)


@dataclass
class Ellipse(Image):
    width: float
    height: float
    mode: Mode

    def draw(self, painter, origin):
        config_painter(painter, self.mode)
        painter.drawEllipse(origin[0], origin[1], self.width, self.height)


@dataclass
class Text(Image):
    text: str
    size: float
    color: Color

    def _font(self):
        f = QFont()
        f.setPixelSize(self.size)
        return f

    @property
    def width(self):
        return QFontMetricsF(self._font()).size(Qt.TextSingleLine, self.text).width()

    @property
    def height(self):
        return QFontMetricsF(self._font()).size(Qt.TextSingleLine, self.text).height()

    def draw(self, painter, origin):
        config_painter(painter, self.color)
        painter.setFont(self._font())
        painter.drawText(origin[0], origin[1] +
                         self.height - self.height / 4, self.text)


@dataclass
class Pixmap(Image):
    pixmap: QPixmap

    @property
    def width(self):
        return self.pixmap.width()

    @property
    def height(self):
        return self.pixmap.height()

    def draw(self, painter, origin):
        painter.drawPixmap(origin[0], origin[1], self.pixmap)


def _pixmap(path):
    app = QApplication(sys.argv)
    pixmap = QPixmap(path)
    if pixmap.isNull():
        raise Exception('Invalid pixmap: {}'.format(path))
    return Pixmap(pixmap)


#######################################
# Image combinations
#
# TODO: create OverlayXY


@dataclass
class Beside(Image):
    align: str
    images: List[Image]

    @property
    def width(self):
        return sum(i.width for i in self.images)

    @property
    def height(self):
        return max(i.height for i in self.images)

    def draw(self, painter, origin):
        h = self.height
        dx = 0
        dy = _y_align(self.align)
        for image in self.images:
            image.draw(painter, (origin[0] + dx,
                                 origin[1] + dy(h, image.height)))
            dx += image.width


@dataclass
class Above(Image):
    align: str
    images: List[Image]

    @property
    def width(self):
        return max(i.width for i in self.images)

    @property
    def height(self):
        return sum(i.height for i in self.images)

    def draw(self, painter, origin):
        w = self.width
        dx = _x_align(self.align)
        dy = 0
        for image in self.images:
            image.draw(painter, (origin[0] + dx(w, image.width),
                                 origin[1] + dy))
            dy += image.height


@dataclass
class Overlay(Image):
    x_align: str
    y_align: str
    images: List[Image]

    @property
    def width(self):
        return max(i.width for i in self.images)

    @property
    def height(self):
        return max(i.height for i in self.images)

    def draw(self, painter, origin):
        w = self.width
        h = self.height
        dx = _x_align(self.x_align)
        dy = _y_align(self.y_align)
        for image in reversed(self.images):
            image.draw(painter, (origin[0] + dx(w, image.width),
                                 origin[1] + dy(h, image.height)))


@dataclass
class Place(Image):
    image: Image
    x_align: str
    x: float
    y_align: str
    y: float
    scene: Image

    @property
    def width(self):
        return self.scene.width

    @property
    def height(self):
        return self.scene.height

    def draw(self, painter, origin):
        self.scene.draw(painter, origin)
        dx = _x_align(self.x_align)(self.image.width, 0)
        dy = _y_align(self.y_align)(self.image.height, 0)
        painter.save()
        painter.setClipRect(origin[0], origin[1],
                            self.scene.width, self.scene.height)
        self.image.draw(
            painter, (origin[0] + self.x - dx, origin[1] + self.y - dy))
        painter.restore()


def _x_align(align):
    def center(a, b):
        return round((a - b) / 2)

    def left(a, b):
        return 0

    def right(a, b):
        return a - b

    if align == 'center':
        return center
    elif align == 'left':
        return left
    elif align == 'right':
        return right
    else:
        raise Exception('Invalid x align: {}'.format(align))


def _y_align(align):
    def center(a, b):
        return round((a - b) / 2)

    def top(a, b):
        return 0

    def bottom(a, b):
        return a - b

    if align == 'center':
        return center
    elif align == 'top':
        return top
    elif align == 'bottom':
        return bottom
    else:
        raise Exception('Invalid y align: {}'.format(align))


#######################################
# World creation


def _create(world, to_draw, on_tick=None, ticks_per_second=None, on_key=None):
    app = QApplication(sys.argv)
    w = WorldWidget(world, to_draw, on_key)
    w.show()


    if ticks_per_second == None:
        ticks_per_second = 60

    if on_tick != None:
        def timeout():
            nonlocal on_tick
            nonlocal w
            w.world = on_tick(w.world)
            w.update()

        timer = QTimer()
        timer.timeout.connect(timeout)
        timer.setTimerType(Qt.PreciseTimer)
        timer.setInterval(round(1000 / ticks_per_second))
        timer.start()

    ret = app.exec_()
    if ret != 0:
        print('The program finished with error code:', ret)

    return w.world


def _image_view(image):
    create(image, lambda x: x)


def _image_save(image, filename):
    import sys
    app = QApplication(sys.argv)
    svg = QSvgGenerator()
    svg.setSize(QSize(image.width + 2, image.height + 2))
    svg.setViewBox(QRect(0, 0, image.width + 2, image.height + 2))
    svg.setFileName(filename)
    painter = QPainter()
    painter.begin(svg)
    image.draw(painter, (1, 1))
    painter.end()


class WorldWidget(QWidget):
    def __init__(self, world, to_draw, on_key=None):
        super().__init__()
        self.world = world
        self.to_draw = to_draw
        self.on_key = on_key
        self.image = to_draw(world)
        self.initial_size = (self.image.width, self.image.height)
        self.resize(self.image.width + 2, self.image.height + 2)
        self.buffer = QPixmap(self.width(), self.height())

    def paintEvent(self, evt):
        self.image = self.to_draw(self.world)
        cur_size = (self.image.width, self.image.height)
        if self.initial_size != cur_size:
            raise Exception(
                'The word image changed its size. Initial size was {}, but changed to {}.'
                .format(self.initial_size, cur_size)
            )
        self.painter = QPainter(self.buffer)
        self.painter.setRenderHint(QPainter.Antialiasing)
        self.painter.setBrush(Color.WHITE._qcolor())
        self.painter.drawRect(0, 0, self.width(), self.height())
        self.image.draw(self.painter, (1, 1))
        self.painter = None
        pp = QPainter(self)
        pp.drawPixmap(0, 0, self.buffer)

    def keyPressEvent(self, event):
        if self.on_key == None:
            return
        k = event.text()
        if event.key() in KEYS:
            k = KEYS[event.key()]
        if event.key() in KEYS or len(k) == 1:
            self.world = self.on_key(self.world, k)
            self.update()


#######################################
# Constants


KEYS = {
    Qt.Key_Left: 'left',
    Qt.Key_Right: 'right',
    Qt.Key_Up: 'up',
    Qt.Key_Down: 'down',
    Qt.Key_Return: 'return',
    Qt.Key_Escape: 'escape',
}

# extracted from racket source code
Color.ORANGERED = Color(255, 69, 0)
Color.TOMATO = Color(255, 99, 71)
Color.DARKRED = Color(139, 0, 0)
Color.RED = Color(255, 0, 0)
Color.FIREBRICK = Color(178, 34, 34)
Color.CRIMSON = Color(220, 20, 60)
Color.DEEPPINK = Color(255, 20, 147)
Color.MAROON = Color(176, 48, 96)
Color.INDIANRED = Color(205, 92, 92)
Color.MEDIUMVIOLETRED = Color(199, 21, 133)
Color.VIOLETRED = Color(208, 32, 144)
Color.LIGHTCORAL = Color(240, 128, 128)
Color.HOTPINK = Color(255, 105, 180)
Color.PALEVIOLETRED = Color(219, 112, 147)
Color.LIGHTPINK = Color(255, 182, 193)
Color.ROSYBROWN = Color(188, 143, 143)
Color.PINK = Color(255, 192, 203)
Color.ORCHID = Color(218, 112, 214)
Color.LAVENDERBLUSH = Color(255, 240, 245)
Color.SNOW = Color(255, 250, 250)
Color.CHOCOLATE = Color(210, 105, 30)
Color.SADDLEBROWN = Color(139, 69, 19)
Color.BROWN = Color(132, 60, 36)
Color.DARKORANGE = Color(255, 140, 0)
Color.CORAL = Color(255, 127, 80)
Color.SIENNA = Color(160, 82, 45)
Color.ORANGE = Color(255, 165, 0)
Color.SALMON = Color(250, 128, 114)
Color.PERU = Color(205, 133, 63)
Color.DARKGOLDENROD = Color(184, 134, 11)
Color.GOLDENROD = Color(218, 165, 32)
Color.SANDYBROWN = Color(244, 164, 96)
Color.LIGHTSALMON = Color(255, 160, 122)
Color.DARKSALMON = Color(233, 150, 122)
Color.GOLD = Color(255, 215, 0)
Color.YELLOW = Color(255, 255, 0)
Color.OLIVE = Color(128, 128, 0)
Color.BURLYWOOD = Color(222, 184, 135)
Color.TAN = Color(210, 180, 140)
Color.NAVAJOWHITE = Color(255, 222, 173)
Color.PEACHPUFF = Color(255, 218, 185)
Color.KHAKI = Color(240, 230, 140)
Color.DARKKHAKI = Color(189, 183, 107)
Color.MOCCASIN = Color(255, 228, 181)
Color.WHEAT = Color(245, 222, 179)
Color.BISQUE = Color(255, 228, 196)
Color.PALEGOLDENROD = Color(238, 232, 170)
Color.BLANCHEDALMOND = Color(255, 235, 205)
Color.MEDIUMGOLDENROD = Color(234, 234, 173)
Color.PAPAYAWHIP = Color(255, 239, 213)
Color.MISTYROSE = Color(255, 228, 225)
Color.LEMONCHIFFON = Color(255, 250, 205)
Color.ANTIQUEWHITE = Color(250, 235, 215)
Color.CORNSILK = Color(255, 248, 220)
Color.LIGHTGOLDENRODYELLOW = Color(250, 250, 210)
Color.OLDLACE = Color(253, 245, 230)
Color.LINEN = Color(250, 240, 230)
Color.LIGHTYELLOW = Color(255, 255, 224)
Color.SEASHELL = Color(255, 245, 238)
Color.BEIGE = Color(245, 245, 220)
Color.FLORALWHITE = Color(255, 250, 240)
Color.IVORY = Color(255, 255, 240)
Color.GREEN = Color(0, 255, 0)
Color.LAWNGREEN = Color(124, 252, 0)
Color.CHARTREUSE = Color(127, 255, 0)
Color.GREENYELLOW = Color(173, 255, 47)
Color.YELLOWGREEN = Color(154, 205, 50)
Color.OLIVEDRAB = Color(107, 142, 35)
Color.MEDIUMFORESTGREEN = Color(107, 142, 35)
Color.DARKOLIVEGREEN = Color(85, 107, 47)
Color.DARKSEAGREEN = Color(143, 188, 139)
Color.LIME = Color(0, 255, 0)
Color.DARKGREEN = Color(0, 100, 0)
Color.LIMEGREEN = Color(50, 205, 50)
Color.FORESTGREEN = Color(34, 139, 34)
Color.SPRINGGREEN = Color(0, 255, 127)
Color.MEDIUMSPRINGGREEN = Color(0, 250, 154)
Color.SEAGREEN = Color(46, 139, 87)
Color.MEDIUMSEAGREEN = Color(60, 179, 113)
Color.AQUAMARINE = Color(112, 216, 144)
Color.LIGHTGREEN = Color(144, 238, 144)
Color.PALEGREEN = Color(152, 251, 152)
Color.MEDIUMAQUAMARINE = Color(102, 205, 170)
Color.TURQUOISE = Color(64, 224, 208)
Color.LIGHTSEAGREEN = Color(32, 178, 170)
Color.MEDIUMTURQUOISE = Color(72, 209, 204)
Color.HONEYDEW = Color(240, 255, 240)
Color.MINTCREAM = Color(245, 255, 250)
Color.ROYALBLUE = Color(65, 105, 225)
Color.DODGERBLUE = Color(30, 144, 255)
Color.DEEPSKYBLUE = Color(0, 191, 255)
Color.CORNFLOWERBLUE = Color(100, 149, 237)
Color.STEELBLUE = Color(70, 130, 180)
Color.LIGHTSKYBLUE = Color(135, 206, 250)
Color.DARKTURQUOISE = Color(0, 206, 209)
Color.CYAN = Color(0, 255, 255)
Color.AQUA = Color(0, 255, 255)
Color.DARKCYAN = Color(0, 139, 139)
Color.TEAL = Color(0, 128, 128)
Color.SKYBLUE = Color(135, 206, 235)
Color.CADETBLUE = Color(95, 158, 160)
Color.DARKSLATEGRAY = Color(47, 79, 79)
Color.LIGHTSLATEGRAY = Color(119, 136, 153)
Color.SLATEGRAY = Color(112, 128, 144)
Color.LIGHTSTEELBLUE = Color(176, 196, 222)
Color.LIGHTBLUE = Color(173, 216, 230)
Color.POWDERBLUE = Color(176, 224, 230)
Color.PALETURQUOISE = Color(175, 238, 238)
Color.LIGHTCYAN = Color(224, 255, 255)
Color.ALICEBLUE = Color(240, 248, 255)
Color.AZURE = Color(240, 255, 255)
Color.MEDIUMBLUE = Color(0, 0, 205)
Color.DARKBLUE = Color(0, 0, 139)
Color.MIDNIGHTBLUE = Color(25, 25, 112)
Color.NAVY = Color(36, 36, 140)
Color.BLUE = Color(0, 0, 255)
Color.INDIGO = Color(75, 0, 130)
Color.BLUEVIOLET = Color(138, 43, 226)
Color.MEDIUMSLATEBLUE = Color(123, 104, 238)
Color.SLATEBLUE = Color(106, 90, 205)
Color.PURPLE = Color(160, 32, 240)
Color.DARKSLATEBLUE = Color(72, 61, 139)
Color.DARKVIOLET = Color(148, 0, 211)
Color.DARKORCHID = Color(153, 50, 204)
Color.MEDIUMPURPLE = Color(147, 112, 219)
Color.MEDIUMORCHID = Color(186, 85, 211)
Color.MAGENTA = Color(255, 0, 255)
Color.FUCHSIA = Color(255, 0, 255)
Color.DARKMAGENTA = Color(139, 0, 139)
Color.VIOLET = Color(238, 130, 238)
Color.PLUM = Color(221, 160, 221)
Color.LAVENDER = Color(230, 230, 250)
Color.THISTLE = Color(216, 191, 216)
Color.GHOSTWHITE = Color(248, 248, 255)
Color.WHITE = Color(255, 255, 255)
Color.WHITESMOKE = Color(245, 245, 245)
Color.GAINSBORO = Color(220, 220, 220)
Color.LIGHTGRAY = Color(211, 211, 211)
Color.SILVER = Color(192, 192, 192)
Color.GRAY = Color(190, 190, 190)
Color.DARKGRAY = Color(169, 169, 169)
Color.DIMGRAY = Color(105, 105, 105)
Color.BLACK = Color(0, 0, 0)
