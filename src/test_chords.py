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

    def test_scale_content(self):
        rn = Roman_Numeral(Numeral.I, Inversion.ROOT, Mode.MAJOR)
        c = Chord(rn, Natural.C)
        self.assertEqual(c.scale, [Natural(n) for n in ['c', 'd', 'e', 'f', 'g', 'a', 'b']])
        c = Chord(rn, Flat.E)
        self.assertEqual(c.scale, [Natural(n) if len(n) == 1 else Flat(n) for n in ['eb', 'f', 'g', 'ab', 'bb', 'c', 'd']])
        c = Chord(rn, Sharp.F)
        self.assertEqual(c.scale, [Sharp(n) if len(n) > 1 else Natural(n) for n in ['f#', 'g#', 'a#', 'b', 'c#', 'd#', 'e#']])
        rn = Roman_Numeral(Numeral.I, Inversion.ROOT, Mode.MINOR)
        c = Chord(rn, Natural.B)
        self.assertEqual(c.scale, [Natural(n) if len(n) == 1 else Sharp(n) for n in ['b', 'c#', 'd', 'e', 'f#', 'g', 'a']])
        c = Chord(rn, Flat.A)
        self.assertEqual(c.scale, [Flat(n) for n in ['ab', 'bb', 'cb', 'db', 'eb', 'fb', 'gb']])
        c = Chord(rn, Sharp.C)
        self.assertEqual(c.scale, [Sharp(n) if len(n) > 1 else Natural(n) for n in ['c#', 'd#', 'e', 'f#', 'g#', 'a', 'b']])
