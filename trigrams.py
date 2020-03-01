#!/usr/bin/env python3

"""
Class ``Trigram`` represents an I Ching trigram.

The ``Trigram.build_all()`` class method is invoked when the module 
is loaded to create class attributes named after the trigrams,
and store a list of them in ``Trigram.all``::

    >>> Trigram.MOUNTAIN
    <Trigram ☶ MOUNTAIN>

The ``Trigram.all`` class attribute holds every trigram::

    >>> for trigram in Trigram.all:
    ...     print(repr(trigram))
    <Trigram ☰ HEAVEN>
    <Trigram ☳ THUNDER>
    <Trigram ☵ WATER>
    <Trigram ☶ MOUNTAIN>
    <Trigram ☷ EARTH>
    <Trigram ☴ WIND>
    <Trigram ☲ FIRE>
    <Trigram ☱ LAKE>

The ``.draw()`` instance method draws a trigram on the console::

    >>> Trigram.MOUNTAIN.draw()
    ━━━━━━━━━
    ━━━   ━━━
    ━━━   ━━━

The trigram drawing can be labeled::

    >>> Trigram.WIND.draw(label=True)
    ━━━━━━━━━ ☴ WIND
    ━━━━━━━━━
    ━━━   ━━━

"""

# U+2501  ━  BOX DRAWINGS HEAVY HORIZONTAL
LINE_DRAWINGS = {
    7: '━━━━━━━━━',
    8: '━━━   ━━━',
}


FIRST_TRIGRAM_CODE = 0x2630

# line values ordered from bottom to top
TRIGRAM_DATA = (
    [(7, 7, 7), '☰', 'HEAVEN'],
    [(7, 8, 8), '☳', 'THUNDER'],
    [(8, 7, 8), '☵', 'WATER'],
    [(8, 8, 7), '☶', 'MOUNTAIN'],
    [(8, 8, 8), '☷', 'EARTH'],
    [(8, 7, 7), '☴', 'WIND'],
    [(7, 8, 7), '☲', 'FIRE'],
    [(7, 7, 8), '☱', 'LAKE'],
)


class Gua:

    def __init__(self, lines, char, name):
        self.lines = list(lines)
        self.name = name
        self.char = char

    def __str__(self):
        return f'{self.char} {self.name}'        

    def __repr__(self):
        cls_name = type(self).__name__
        return f'<{cls_name} {self}>'

    def draw(self, label=False, line_drawings=LINE_DRAWINGS):
        for i, line in enumerate(reversed(self.lines)):
            drawing = line_drawings[line]
            if label and i == 0:
                print(drawing, self)
            else:
                print(drawing)


class Trigram(Gua):

    @classmethod
    def build_all(cls):
        cls.all = []
        for lines, char, name in TRIGRAM_DATA:
            trigram = Trigram(lines, char, name)
            setattr(cls, name, trigram)
            cls.all.append(trigram)


Trigram.build_all()


def demo():
    for trigram in Trigram.all:
        trigram.draw(True)
        print()


if __name__ == '__main__':
    demo()