"""
Class Trigram represents an I Ching trigram.

The ``Trigram.build_all()`` class method is invoked when the module 
is loaded to create class attributes named after the trigrams::

    >>> Trigram.MOUNTAIN
    <Trigram ☶ MOUNTAIN>

The ``Trigram.all()`` class generator method yields every trigram:

    >>> for trigram in Trigram.all():
    ...     print(repr(trigram))
    <Trigram ☰ HEAVEN>
    <Trigram ☳ THUNDER>
    <Trigram ☵ WATER>
    <Trigram ☶ MOUNTAIN>
    <Trigram ☷ EARTH>
    <Trigram ☴ WIND>
    <Trigram ☲ FIRE>
    <Trigram ☱ LAKE>

The `.draw()` instance method draws a trigram on the console:

    >>> Trigram.WIND.draw()
    ━━━━━━━━━
    ━━━━━━━━━
    ━━━   ━━━

The trigram drawing can have be labeled:

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

class Trigram:
    def __init__(self, lines, char, name):
        self.lines = lines[:]
        self.name = name
        self.char = char

    def __str__(self):
        return f'{self.char} {self.name}'        

    def __repr__(self):
        return f'<Trigram {self}>'

    @classmethod
    def build_all(cls):
        for lines, char, name in TRIGRAM_DATA:
            setattr(cls, name, Trigram(lines, char, name))

    @classmethod
    def all(cls):
        for _, _, name in TRIGRAM_DATA:
            yield getattr(cls, name)

    def draw(self, label=False):
        for i, line in enumerate(reversed(self.lines)):
            drawing = LINE_DRAWINGS[line]
            if label and i == 0:
                print(drawing, self)
            else:
                print(drawing)


Trigram.build_all()


def demo():
    for trigram in Trigram.all():
        trigram.draw(True)
        print()



if __name__ == '__main__':
    demo()