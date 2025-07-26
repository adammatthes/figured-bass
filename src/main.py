#! /usr/bin/python3

from romannumeral import Roman_Numeral
from chords import Chord
from progression import Progression
import subprocess

def setup_output_folder():
    folder_not_found = subprocess.run(['find', 'lily_output'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode
    if folder_not_found:
        subprocess.run(['mkdir', 'lily_output'])
    else:
        subprocess.run(['rm', 'lily_output/*'])




def main():

    setup_output_folder()







if __name__ == "__main__":
    main()
