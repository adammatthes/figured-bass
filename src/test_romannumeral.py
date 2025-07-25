import unittest
from romannumeral import *

class TestRomanNumeral(unittest.TestCase):
    def test_roman_numeral_init(self):
        r_numeral = Roman_Numeral(Numeral.I, Inversion.ROOT, Mode.MAJOR)
        self.assertEqual(r_numeral.__str__(), "I 5/3")
