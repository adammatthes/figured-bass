from romannumeral import *


I = Roman_Numeral(Numeral.I, Inversion.ROOT, Mode.MAJOR)
I6 = Roman_Numeral(Numeral.I, Inversion.FIRST_INVERSION, Mode.MAJOR)

ii = Roman_Numeral(Numeral.ii, Inversion.ROOT, Mode.MINOR)
ii6 = Roman_Numeral(Numeral.ii, Inversion.FIRST_INVERSION, Mode.MINOR)
bII6 = Roman_Numeral(Numeral.bII6, Inversion.FIRST_INVERSION, Mode.MAJOR)

iii = Roman_Numeral(Numeral.iii, Inversion.ROOT, Mode.MINOR)
iii6 = Roman_Numeral(Numeral.iii, Inversion.FIRST_INVERSION, Mode.MINOR)

IV = Roman_Numeral(Numeral.IV, Inversion.ROOT, Mode.MAJOR)
IV6 = Roman_Numeral(Numeral.IV, Inversion.FIRST_INVERSION, Mode.MAJOR)

V = Roman_Numeral(Numeral.V, Inversion.ROOT, Mode.MAJOR)
V6 = Roman_Numeral(Numeral.V, Inversion.FIRST_INVERSION, Mode.MAJOR)
V64 = Roman_Numeral(Numeral.V, Inversion.SECOND_INVERSION, Mode.MAJOR)

vi = Roman_Numeral(Numeral.vi, Inversion.ROOT, Mode.MINOR)
vi6 = Roman_Numeral(Numeral.vi, Inversion.FIRST_INVERSION, Mode.MINOR)

viio = Roman_Numeral(Numeral.vii, Inversion.ROOT, Mode.DIMINISHED)
viio6 = Roman_Numeral(Numeral.vii, Inversion.FIRST_INVERSION, Mode.DIMINISHED)

class Harmony_Graph():
    def __init__(self):
        self.graph = {
            I: {bII6, iii, IV, IV6, V, V6, vi, viio},
            I6: {IV, V, ii, V6, IV6, V64},
            ii: {IV, V, V6, viio6},
            ii6: {V, V6, V64, viio6},
            bII6: {V64, V},
            iii: {IV, vi},
            iii6: {IV, vi},
            IV: {V, V6, ii, I, I6},
            IV6: {V, I, V6, I6},
            V: {I, vi, viio, I6},
            V6: {I, I6, vi},
            V64: {V},
            vi: {V, IV, ii, I},
            vi6: {ii, IV, V, I},
            viio: {I, I6},
            viio6: {I, I6}
        }
