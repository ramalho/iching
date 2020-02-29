from enum import Enum
from typing import List


# U+2501  ━  BOX DRAWINGS HEAVY HORIZONTAL
LINE_DRAWINGS = {
    7: '━━━━━━━━━',
    8: '━━━   ━━━',
}


FIRST_TRIGRAM_CODE = 0x2630


TRIGRAM_DATA = {
    'HEAVEN'  : (7, 7, 7),  # ☰
    'LAKE'    : (7, 7, 8),  # ☱
    'FIRE'    : (7, 8, 7),  # ☲
    'THUNDER' : (7, 8, 8),  # ☳
    'WIND'    : (8, 7, 7),  # ☴
    'WATER'   : (8, 7, 8),  # ☵
    'MOUNTAIN': (8, 8, 7),  # ☶
    'EARTH'   : (8, 8, 8),  # ☷
}


class Trigram:

    def __init__(self, lines: List[int], name, char):
        if len(lines) != 3:
            raise ValueError(f'expected 3' + 
                             f' lines, got {len(lines)}')
        self.lines = lines[:]
        self.name = name
        self.char = char

    def __str__(self):
        return f'{self.char} {self.name}'        

    def __repr__(self):
        return f'<Trigram {self}>'

    @classmethod
    def generate_all(cls):
        for i, (name, lines) in enumerate(TRIGRAM_DATA.items()):
            yield Trigram(lines, name, chr(FIRST_TRIGRAM_CODE + i))

    @classmethod
    def show_all(cls):
        for trigram in cls.generate_all():
            print(repr(trigram))

    def draw(self, label=False):
        for i, line in enumerate(reversed(self.lines)):
            drawing = LINE_DRAWINGS[line]
            if label and i == 0:
                print(drawing, self)
            else:
                print(drawing)

    @classmethod
    def draw_all(cls):
        for trigram in cls.generate_all():
            trigram.draw(True)
            print()


if __name__ == '__main__':
    Trigram.show_all()
    Trigram.draw_all()
