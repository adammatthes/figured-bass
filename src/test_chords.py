import unittest
from chords import Chord, Natural, Flat, Sharp
from romannumeral import Roman_Numeral, Numeral, Inversion, Mode


class TestChords(unittest.TestCase):
    def test_chord_from_numeral(self):
        rn = Roman_Numeral(Numeral.I, Inversion.ROOT, Mode.MAJOR)
        c = Chord(rn, Natural.C)
        self.assertEqual(c.__str__(), "c major 5/3")
        rn = Roman_Numeral(Numeral.I, Inversion.ROOT, Mode.MINOR)
        c = Chord(rn, Natural.C)
        self.assertEqual(c.__str__(), "c minor 5/3")
        rn = Roman_Numeral(Numeral.I, Inversion.FIRST_INVERSION, Mode.MAJOR)
        c = Chord(rn, Natural.D)
        self.assertEqual(c.__str__(), "d major 6/3")
        rn = Roman_Numeral(Numeral.I, Inversion.SECOND_INVERSION, Mode.MINOR)
        c = Chord(rn, Natural.F)
        self.assertEqual(c.__str__(), "f minor 6/4")
