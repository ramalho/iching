#!/usr/bin/env python3

"""
``Hexagram`` represents an I Ching hexagram.

The ``Hexagram.build_all()`` class method is invoked when the module 
is loaded to create every ``Hexagram`` instance and store them in
``Hexagram.all`` in King Wen order.

    >>> Hexagram.all[0]
    <Hexagram 1 ䷀ THE CREATIVE HEAVEN>
    >>> Hexagram.all[1]
    <Hexagram 2 ䷁ THE RECEPTIVE EARTH>
    >>> Hexagram.all[63]
    <Hexagram 64 ䷿ BEFORE COMPLETION>

To get an hexagram using its traditional number in the King Wen
order, retrieve it from the class itself (requires Python ≥ 3.7)::

    >>> Hexagram[1]
    <Hexagram 1 ䷀ THE CREATIVE HEAVEN>
    >>> Hexagram[2]
    <Hexagram 2 ䷁ THE RECEPTIVE EARTH>
    >>> Hexagram[64]
    <Hexagram 64 ䷿ BEFORE COMPLETION>

The `.draw()` instance method draws an hexagram on the console:

    >>> Hexagram[56].draw()
    ━━━━━━━━━
    ━━━   ━━━
    ━━━━━━━━━
    ━━━━━━━━━
    ━━━   ━━━
    ━━━   ━━━

The hexagram drawing can have be labeled:

    >>> Hexagram[22].draw(label=True)
    ━━━━━━━━━ 22 ䷕ GRACE
    ━━━   ━━━
    ━━━   ━━━
    ━━━━━━━━━
    ━━━   ━━━
    ━━━━━━━━━


"""

import unicodedata

from trigrams import Gua, Trigram

LOOKUP_TABLE = [
    # ☰   ☳   ☵   ☶   ☷   ☴   ☲   ☱ 
    ( 1, 34,  5, 26, 11,  9, 14, 43), # ☰
    (25, 51,  3, 27, 24, 42, 21, 17), # ☳
    ( 6, 40, 29,  4,  7, 59, 64, 47), # ☵
    (33, 62, 39, 52, 15, 53, 56, 31), # ☶ 
    (12, 16,  8, 23,  2, 20, 35, 45), # ☷
    (44, 32, 48, 18, 46, 57, 50, 28), # ☴
    (13, 55, 63, 22, 36, 37, 30, 49), # ☲
    (10, 54, 60, 41, 19, 61, 38, 58), # ☱
]

FIRST_HEXAGRAM = 0x4DC0
NAME_PREFIX = 'HEXAGRAM FOR '


class Hexagram(Gua):

    all = [None] * 64
    lines_map = {}

    def __init__(self, lines, char, name, number):
        super().__init__(lines, char, name)
        self.number = number

    def __str__(self):
        return f'{self.number} {self.char} {self.name}'        

    @classmethod
    def build_all(cls):
        for row, lower_tri in zip(LOOKUP_TABLE, Trigram.all):
            for n, upper_tri in zip(row, Trigram.all):
                lines = lower_tri.lines + upper_tri.lines
                char = chr(FIRST_HEXAGRAM + n - 1)
                name = unicodedata.name(char).replace(NAME_PREFIX, '')
                hexa = Hexagram(lines, char, name, n)
                cls.all[n-1] = hexa
                cls.lines_map[tuple(lines)] = hexa

    def __class_getitem__(cls, item):
        if not isinstance(item, int) or item < 1 or item > 64:
            raise KeyError('hexagram numbers are 1 to 64 (including)')
        return cls.all[item-1]


Hexagram.build_all()


def demo():
    for n in range(1, 65):
        indent = ' ' if n < 10 else ''
        print(f'{indent}{Hexagram[n]}')
    print()

    gutter = '   '
    print(' ', *(t.char for t in Trigram.all), sep=gutter)
    print()
    for row, tri in zip(LOOKUP_TABLE, Trigram.all):
        print(tri.char, end=gutter)
        for n in row:
            print(Hexagram[n].char, end=gutter)
        print()
        print()


if __name__ == '__main__':
    demo()
