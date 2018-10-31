#!/usr/bin/python3

import sys
from creation import *


def run(infile, f):
    ex = []
    comment = ''
    buffer = ''
    base = infile[:-3]  # remove .py
    for line in open(infile).readlines():
        if line[0] == '#':
            if buffer != '':
                ex.append((comment, buffer))
            comment = line[1:].strip()
            buffer = ''
        else:
            buffer += line

    if buffer != '':
        ex.append((comment, buffer))

    i = 0
    lcount = 0
    for comment, cmd in ex:
        lcount += cmd.count('\n')
        if lcount > 2 or i == 0:
            print('## `{}`\n'.format(base), file=f)
            if i != 0:
                lcount = 0
        print(comment, file=f)
        print(file=f)
        print('```python\n>>> {}```\n'.format(cmd), file=f)
        print('![](figs/{}-{}.pdf)\n\n'.format(base, i), file=f)
        eval('image_save({}, "../target/creation/{}-{}.svg")'.format(cmd, base, i))
        i += 1


def main():
    if len(sys.argv) < 2:
        print('Invalid arguments number')
        sys.exit(1)

    f = open('../target/creation/exemplos.md', 'w')
    for infile in sys.argv[1:]:
        run(infile, f)


if __name__ == "__main__":
    main()
