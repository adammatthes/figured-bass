from enum import Enum

class Numeral(Enum):
    I = "i"
    ii = "ii"
    iii = "iii"
    IV = "iv"
    V = "v"
    vi = "vi"
    vii = "vii"


class Inversion(Enum):
    ROOT = "5/3"
    FIRST_INVERSION = "6/3"
    SECOND_INVERSION = "6/4"
    DOMINANT_ROOT = "7"
    DOMINANT_FIRST_INVERSION = "6/5"
    DOMINANT_SECOND_INVERSION = "4/3"
    DOMINANT_THIRD_INVERSION = "4/2"


class Mode(Enum):
    MAJOR = 'major'
    MINOR = 'minor'
    DIMINISHED = 'dim'


class Roman_Numeral():
    def __init__(self, numeral, inversion, mode):
        self.numeral = numeral
        self.inversion = inversion
        self.mode = mode

    def __str__(self):
        return f'{self.numeral.value.upper() if self.mode == Mode.MAJOR else self.numeral.value} {"o" if self.mode == Mode.DIMINISHED else ""}{self.inversion.value}'

    def arabic(self):
        match self.numeral:
            case Numeral.I:
                return 1
            case Numeral.ii:
                return 2
            case Numeral.iii:
                return 3
            case Numeral.IV:
                return 4
            case Numeral.V:
                return 5
            case Numeral.vi:
                return 6
            case Numeral.vii:
                return 7
