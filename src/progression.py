from chords import Chord
from romannumeral import Roman_Numeral


class Progression():
    def __init__(self, numerals):
        self.numerals = numerals
        self.chords = [Chord(n) for n in self.numerals]

    def __str__(self):
        return ' '.join(str(s) for s in self.numerals)

    def to_lily(self):
        content = []
        content.append('version "2.22.1"')
        content.append('\score {')
        content.append("\chordmode {")
        #content.append("\\new Staff {")
        for c in self.chords:
            content.append('\invertChords ' + f'{c.to_lily(4)}{chr(10)}')

        
        content.append("}")
        content.append("\midi { }")
        content.append("}")
        return ''.join(content)
