from array import array
from enum import IntEnum
import random

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

ODDS = {
    6: 1,
    8: 7,
    7: 5,
    9: 3,
}


assert sum(ODDS.values()) == 16, 'sum must be 16'

outcome_groups = ([result] * chances for result, chances in ODDS.items())
OUTCOMES = array('B', (o for group in outcome_groups for o in group))

assert len(OUTCOMES) == 16, 'length of OUTCOMES must be 16'
assert sum(o % 2 for o in OUTCOMES) == 8, 'count of odd outcomes must be 8'

class Yao(IntEnum):
    OLD_YIN = 6
    YANG = 7
    YIN = 8
    OLD_YANG = 9

    def draw(self):
        return LINE_DRAWINGS[self.value]

    def mutate(self):
        if self is Yao.OLD_YIN:
            return Yao.YANG
        elif self is Yao.OLD_YANG:
            return Yao.YIN
        return self

    @classmethod
    def pick(cls):
        return cls(random.choice(OUTCOMES))


Yao.NAMES = {y.value: y.name.replace('_', ' ').title() for y in Yao}



