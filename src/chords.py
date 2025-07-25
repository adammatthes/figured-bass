from enum import Enum

from romannumeral import Mode

class Natural(Enum):
    A = 'a'
    B = 'b'
    C = 'c'
    D = 'd'
    E = 'e'
    F = 'f'
    G = 'g'


class Flat(Enum):
    A = 'ab'
    B = 'bb'
    C = 'cb'
    D = 'db'
    E = 'eb'
    F = 'fb'
    G = 'gb'


class Sharp(Enum):
    A = 'a#'
    B = 'b#'
    C = 'c#'
    D = 'd#'
    E = 'e#'
    F = 'f#'
    G = 'g#'


class Chord():
    
    def __init__(self, roman_numeral, tonic=Natural.C):
        self.scale = self.get_scale(roman_numeral, tonic)
        self.tonic = tonic
        self.mode = roman_numeral.mode
        self.inversion = roman_numeral.inversion


    def __str__(self):
        return f'{self.tonic.value} {self.mode.value} {self.inversion.value}'

    def get_scale(self, roman_numeral, tonic):
        order_sharps = ['f', 'c', 'g', 'd', 'a', 'e', 'b']
        order_flats = order_sharps[::-1]

        # keys with quantities marked 'None' contain double sharps or double flats and will not be supported
        accidental_quantity = {
                'c': {'major': {'sharp': 0, 'flat': 0}, 'minor': {'sharp': 0, 'flat': 3}},
                'd': {'major': {'sharp': 2, 'flat': 0}, 'minor': {'sharp': 0, 'flat': 1}},
                'e': {'major': {'sharp': 4, 'flat': 0}, 'minor': {'sharp': 1, 'flat': 0}},
                'f': {'major': {'sharp': 0, 'flat': 1}, 'minor': {'sharp': 0, 'flat': 4}},
                'g': {'major': {'sharp': 1, 'flat': 0}, 'minor': {'sharp': 0, 'flat': 2}},
                'a': {'major': {'sharp': 3, 'flat': 0}, 'minor': {'sharp': 0, 'flat': 0}},
                'b': {'major': {'sharp': 5, 'flat': 0}, 'minor': {'sharp': 2, 'flat': 0}},

                'c#': {'major': {'sharp': 7, 'flat': 0}, 'minor': {'sharp': 4, 'flat': 0}},
                'd#': {'major': None, 'minor': {'sharp': 6, 'flat': 0}},
                'e#': {'major': None, 'minor': None},
                'f#': {'major': {'sharp': 6, 'flat': 0}, 'minor': {'sharp': 3, 'flat': 0}},
                'g#': {'major': None, 'minor': {'sharp': 5, 'flat': 0}},
                'a#': {'major': None, 'minor': None},
                'b#': {'major': None, 'minor': None},

                'cb': {'major': {'sharp': 0, 'flat': 7}, 'minor': None},
                'db': {'major': {'sharp': 0, 'flat': 5}, 'minor': None},
                'eb': {'major': {'sharp': 0, 'flat': 3}, 'minor': {'sharp': 0, 'flat': 6}},
                'fb': {'major': None, 'minor': None},
                'gb': {'major': {'sharp': 0, 'flat': 6}, 'minor': None},
                'ab': {'major': {'sharp': 0, 'flat': 4}, 'minor': {'sharp': 0, 'flat': 7}},
                'bb': {'major': {'sharp': 0, 'flat': 2}, 'minor': {'sharp': 0, 'flat': 5}}
                }

        sharp_or_flat = accidental_quantity[tonic.value][roman_numeral.mode.value]

        signature = []
        scale = [n for n in Natural]
        if not sharp_or_flat['sharp']:
            signature = order_flats[:sharp_or_flat['flat']]
            for sig in signature:
                for i, s in ennumerate(scale):
                    if s.value.startswith(sig):
                        scale[i] = Flat(f'{sig}b')
        else:
            signature = order_sharps[:sharp_or_flat['sharp']]
            for sig in signature:
                for i, s in enumerate(scale):
                    if s.value.startswith(sig):
                        scale[i] = Sharp(f'{sig}#')

        return scale





