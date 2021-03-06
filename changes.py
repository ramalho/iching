#!/usr/bin/env python3

"""
Class ``Changing`` holds an I Ching hexagram with changing lines.
It is built from an hexagram and one or more numbers from 1 to 6
(including) identifying the changing lines::

    >>> ch11 = Changing.from_(Hexagram[11], 1, 5)
    >>> ch11
    <Changing 11 ䷊ PEACE (1, 5)>
    >>> ch11.draw(label=True)
    ━━━   ━━━ 11 ䷊ PEACE
    ━━━ ⨯ ━━━
    ━━━   ━━━
    ━━━━━━━━━
    ━━━━━━━━━
    ━━━━⊖━━━━

A changing hexagram can produce the hexagram resulting from
applying the changes::

    >>> new = ch11.to()
    >>> new.draw(label=True)
    ━━━   ━━━ 48 ䷯ THE WELL
    ━━━━━━━━━
    ━━━   ━━━
    ━━━━━━━━━
    ━━━━━━━━━
    ━━━   ━━━

The ``.draw_pair()`` method draws the changing hexagram and the
resulting hexagram side-by-side::

    >>> ch22 = Changing.from_(Hexagram[22], 1, 4)
    >>> ch22
    <Changing 22 ䷕ GRACE (1, 4)>
    >>> ch22.to()
    <Hexagram 56 ䷷ THE WANDERER>
    >>> ch22.draw_pair()
    ━━━━━━━━━    ━━━━━━━━━
    ━━━   ━━━    ━━━   ━━━
    ━━━ ⨯ ━━━    ━━━━━━━━━
    ━━━━━━━━━    ━━━━━━━━━
    ━━━   ━━━    ━━━   ━━━
    ━━━━⊖━━━━    ━━━   ━━━

Calling ``my_changing.draw_pair(label=True)`` outputs labels::

    >>> ch3 = Changing.from_(Hexagram[3], 5)
    >>> ch3
    <Changing 3 ䷂ DIFFICULTY AT THE BEGINNING (5)>
    >>> ch3.to()
    <Hexagram 24 ䷗ RETURN>
    >>> ch3.draw_pair(label=True)
    ━━━   ━━━                         ━━━   ━━━
    ━━━━⊖━━━━                         ━━━   ━━━
    ━━━   ━━━                         ━━━   ━━━
    ━━━   ━━━                         ━━━   ━━━
    ━━━   ━━━                         ━━━   ━━━
    ━━━━━━━━━                         ━━━━━━━━━
    3 ䷂ DIFFICULTY AT THE BEGINNING   24 ䷗ RETURN

"""

from hexagrams import Hexagram

# U+2501  ━  BOX DRAWINGS HEAVY HORIZONTAL
# U+2715  ✕  MULTIPLICATION X
# U+2296  ⊖  CIRCLED MINUS
# U+2501  ━  BOX DRAWINGS HEAVY HORIZONTAL
LINE_DRAWINGS = {
    6: '━━━ ⨯ ━━━',
    7: '━━━━━━━━━',
    8: '━━━   ━━━',
    9: '━━━━⊖━━━━',
}


class Changing(Hexagram):

    @classmethod
    def from_(cls, hexagram, *changes):
        changing = cls(hexagram.lines, hexagram.char,
                       hexagram.name, hexagram.number)
        changing.changes = tuple(changes)
        for change in changes:
            if not isinstance(change, int) or change < 1 or change > 6:
                raise KeyError('changes must be integers 1 to 6 (including)')
            if changing.lines[change-1] == 8:
                changing.lines[change-1] = 6
            elif changing.lines[change-1] == 7:
                changing.lines[change-1] = 9
        return changing

    def __repr__(self):
        cls_name = type(self).__name__
        changes = ', '.join(str(n) for n in self.changes)
        return f'<{cls_name} {self} ({changes})>'

    def to(self):
        new_lines = []
        for line in self.lines:
            if line == 6:
                line = 7
            elif line == 9:
                line = 8
            new_lines.append(line)
        return Hexagram.from_lines(*new_lines)

    def draw(self, label=False, line_drawings=LINE_DRAWINGS):
        super().draw(label, line_drawings)

    def draw_pair(self, label=False, line_drawings=LINE_DRAWINGS):
        new = self.to()
        gutter = ' ' * 3
        spacing = ' ' * (len(str(self)) - len(line_drawings[6])) + gutter
        lines = list(zip(self.lines, new.lines))
        for line_from, line_to in reversed(lines):
            print(line_drawings[line_from], line_drawings[line_to], sep=spacing)
        if label:
            print(self, new, sep=gutter)


def demo():
    from random import randint
    starting = Hexagram[randint(1, 64)]
    changes = []
    for _ in range(randint(1, 3)):
        changes.append(randint(1, 6))
    changing = Changing.from_(starting, *changes)
    new = changing.to()
    changing.draw_pair(label=True)

if __name__ == '__main__':
    demo()
