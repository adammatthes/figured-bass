import unittest
from chords import Chord, Natural, Flat, Sharp
from romannumeral import Roman_Numeral, Numeral, Inversion, Mode


class TestChords(unittest.TestCase):
    def test_chord_from_numeral(self):
        rn = Roman_Numeral(Numeral.I, Inversion.ROOT, Mode.MAJOR)
        c = Chord(rn, Natural.C)
        self.assertEqual(c.__str__(), "c major 5/3")
