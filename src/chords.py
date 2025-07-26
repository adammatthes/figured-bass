from enum import Enum

from romannumeral import Mode, Inversion

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
        self.note = self.scale[roman_numeral.arabic() - 1]

    def __str__(self):
        return f'{self.tonic.value} {self.mode.value} {self.inversion.value}'

    def to_lily(self, duration=1):
        val = 0
        match self.inversion:
            case Inversion.ROOT:
                val = 0
            case Inversion.FIRST_INVERSION:
                val = 1
            case Inversion.SECOND_INVERSION:
                val = 2
        
        accidental = ''
        if len(self.tonic.value) > 1:
            match self.tonic.value[1]:
                case 'b':
                    accidental = 'es'
                case '#':
                    accidental = 'is'
                case _:
                    accidental = ''
 

        mode_abr = ":" + self.mode.value[:3] if self.mode != Mode.MAJOR else ''
        return f'{val} {self.note.value[0] + accidental}{duration}{mode_abr}{"7" if "DOMINANT" in self.inversion.name else ""}'

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

        
        enharmonic_subs = {
                'd#': Flat('eb'),
                'e#': Natural('f'),
                'g#': Flat('ab'),
                'a#': Flat('bb'),
                'b#': Natural('c'),
                'cb': Natural('b'),
                'db': Sharp('c#'),
                'fb': Natural('e'),
                'gb': Sharp('f#')
                }

        
        try:
            sharp_or_flat = accidental_quantity[tonic.value][roman_numeral.mode.value]
        except KeyError:
            sharp_or_flat = accidental_quantity[tonic.value]['major']
        if sharp_or_flat is None:
            tonic = enharmonic_subs[tonic.value]
            sharp_or_flat = accidental_quantity[tonic.value][roman_numeral.mode.value]

        signature = []
        scale = [n for n in Natural]
        if sharp_or_flat['sharp'] == 0:
            signature = order_flats[:sharp_or_flat['flat']]
            for sig in signature:
                for i, s in enumerate(scale):
                    if s.value.startswith(sig):
                        scale[i] = Flat(f'{sig}b')
        else:
            signature = order_sharps[:sharp_or_flat['sharp']]
            for sig in signature:
                for i, s in enumerate(scale):
                    if s.value.startswith(sig):
                        scale[i] = Sharp(f'{sig}#')

        rotate_index = scale.index(tonic)
        scale = scale[rotate_index:] + scale[:rotate_index]
        return scale





