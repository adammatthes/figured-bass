#! /usr/bin/python3

from romannumeral import Roman_Numeral
from chords import Chord
from progression import Progression
from harmony_graph import Harmony_Graph, I
from present import present
import subprocess
import sys
import random
import pygame


def setup_output_folder():
    folder_not_found = subprocess.run(['find', 'lily_output'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL).returncode
    if folder_not_found:
        subprocess.run(['mkdir', '-m', '744', 'lily_output'])
    else:
        subprocess.run(['rm', 'lily_output/*'],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL)




def main():
    try:
        progression_length = int(sys.argv[1])
    except (IndexError, ValueError):
        progression_length = 20


    setup_output_folder()

    hg = Harmony_Graph()

    numerals = [I]
    
    for _ in range(progression_length):
        choices = list(hg.graph[numerals[-1]])
        numerals.append(choices[random.randrange(0, len(choices))])

    p = Progression(numerals)

    content = p.to_lily()

    with open('lily_output/output.ly', 'w') as lily_file:
        lily_file.write(content)

    subprocess.run(['lilypond', '-dbackend=null', 'lily_output/output.ly'],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL)

    present('output.midi')







if __name__ == "__main__":
    main()
