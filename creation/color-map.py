#!/usr/bin/python3

from creation import *

def color_map():
    def stamp(c, n):
        ct = Color.BLACK
        if c == ct:
            ct = Color.WHITE
        return overlay('center', 'center', text(n.lower(), 16, ct), rectangle(170, 50, fill(c)))

    table = []
    line = []
    for key in Color.__dict__:
        if key[0].isupper():
            line.append(stamp(Color.__dict__[key], key))
            if len(line) == 18:
                table.append(above('center', *line))
                line.clear()
    if len(line) != 0:
        table.append(above('center', *line))
    return beside('top', *table)

image_save(color_map(), "../target/creation/color-map.svg")
