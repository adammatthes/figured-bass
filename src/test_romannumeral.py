import unittest
from romannumeral import *

class TestRomanNumeral(unittest.TestCase):
    def test_roman_numeral_init(self):
        r_numeral = Roman_Numeral(Numeral.I, Inversion.ROOT, Mode.MAJOR)
        self.assertEqual(r_numeral.__str__(), "I 5/3")
        r_numeral = Roman_Numeral(Numeral.I, Inversion.FIRST_INVERSION, Mode.MINOR)
        self.assertEqual(r_numeral.__str__(), "i 6/3")
        r_numeral = Roman_Numeral(Numeral.vii, Inversion.DOMINANT_SECOND_INVERSION, Mode.DIMINISHED)
        self.assertEqual(r_numeral.__str__(), "vii o4/3")
