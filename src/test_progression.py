import unittest
from progression import Progression
from chords import Chord
from romannumeral import Roman_Numeral
from harmony_graph import *
import subprocess

class TestProgression(unittest.TestCase):
    def test_lily_format(self):
        numerals = [I, IV, vi, ii, V, I]
        p = Progression(numerals)
        lily_content = p.to_lily()
        with open('tmp.ly', 'w') as lily_file:
            lily_file.write(lily_content)
        subprocess.run(['lilypond', 'tmp.ly'])
        subprocess.run(['rm', 'tmp.ly'])
        numerals = [I, iii6, V, vi, V64, V, I]
        p = Progression(numerals)
        lily_content = p.to_lily()
        with open('tmp.ly', 'w') as lily_file:
            lily_file.write(lily_content)
        subprocess.run(['lilypond', 'tmp.ly'])
        subprocess.run(['rm', 'tmp.ly', 'tmp.pdf'])

