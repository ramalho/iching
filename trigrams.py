#!/usr/bin/env python3

"""
Class ``Trigram`` represents an I Ching trigram.

The ``Trigram.build_all()`` class method is invoked when the module
is loaded to create class attributes named after the trigrams::

    >>> Trigram.MOUNTAIN
    <Trigram ☶ MOUNTAIN>

The ``Trigram.all`` class attribute provides access to every trigram::

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


Given 3 line values from bottom to top, where 7 is Yang (closed)
and 8 is Yin (open), the ``Trigram.from_lines()`` method returns
a matching trigram:

    >>> Trigram.from_yaos(7, 8, 8)
    <Trigram ☳ THUNDER>

The ``.draw()`` instance method draws a trigram on the console::

    >>> print(Trigram.MOUNTAIN.draw())
    ━━━━━━━━━
    ━━━   ━━━
    ━━━   ━━━

The trigram drawing can be labeled::

    >>> print(Trigram.WIND.draw(label=True))
    ━━━━━━━━━ ☴ WIND
    ━━━━━━━━━
    ━━━   ━━━

"""

from yao import Yao

class Gua:

    def __init__(self, yaos, char, name):
        self.yaos = yaos
        self.name = name
        self.char = char

    def __str__(self):
        return f'{self.char} {self.name}'

    def __repr__(self):
        cls_name = type(self).__name__
        return f'<{cls_name} {self}>'

    def draw(self, label=False):
        lines = []
        for i, yao in enumerate(reversed(self.yaos)):
            if label and i == 0:
                lines.append(f'{yao.draw()} {self}')
            else:
                lines.append(yao.draw())
        return '\n'.join(lines)


# yao values ordered from bottom to top in tuples
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


class Trigram(Gua):

    _yao_map = {}
    all = _yao_map.values()

    @classmethod
    def build_all(cls):
        for numbers, char, name in TRIGRAM_DATA:
            yaos = [Yao(n) for n in numbers]
            trigram = Trigram(yaos, char, name)
            setattr(cls, name, trigram)
            cls._yao_map[tuple(yaos)] = trigram

    @classmethod
    def from_yaos(cls, bottom, middle, top):
        return cls._yao_map[(bottom, middle, top)]


Trigram.build_all()


def demo():
    for trigram in Trigram.all:
        print(trigram.draw(True))
        print()


if __name__ == '__main__':
    demo()