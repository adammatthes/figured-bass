from romannumeral import *


I = Roman_Numeral(Numeral.I, Inversion.ROOT, Mode.MAJOR)
ii = Roman_Numeral(Numeral.ii, Inversion.ROOT, Mode.MINOR)
iii = Roman_Numeral(Numeral.iii, Inversion.ROOT, Mode.MINOR)
IV = Roman_Numeral(Numeral.IV, Inversion.ROOT, Mode.MAJOR)
V = Roman_Numeral(Numeral.V, Inversion.ROOT, Mode.MAJOR)
vi = Roman_Numeral(Numeral.vi, Inversion.ROOT, Mode.MINOR)
vii = Roman_Numeral(Numeral.vii, Inversion.ROOT, Mode.DIMINISHED)

class Harmony_Graph():
    def __init__(self):
        self.graph = {
            I: {iii, IV, V, vi, vii},
            ii: {IV, V, vi, vii},
            iii: {V, vi, vii},
            IV: {V, vi, vii, I},
            V: {I, vi, vii},
            vi: {V, IV, ii},
            vii: {I}
        }
