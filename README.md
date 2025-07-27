# Figured Bass

## About the program

This is a program I created over the weekend of 25-27 July 2025 for a Hackathon hosted by the website [boot.dev](https://boot.dev). Structurally, I explored going from harmonic roman numerals, to chords, to midi file, which is then played and supplemented with a visual in pygame. Not useful to anyone, but it's kinda neat.

## Requirements

Run the script _install.sh_ to install requirements in addition to python. Those requirements include:

- lilypond: think LaTeX for sheet music. Go [here](https://lilypond.org/doc/v2.23/Documentation/web/index) for more information.

- pygame: a library for making games, also happened to be one of the simpler ways to get a program to play a midi file.

- timidity: this is the midi player pygame needed

It might be worth mentioning that a function that sets up an output folder for the lilypond file uses the _find_ command as a check, in case your distribution doesn't have it.

## Running the program

```
./main.sh
```

or 

```
./main.sh [number of chords] [beats per minute]
```

If arguments are not provided, the default number of chords is 20 and default bpm is 60.

## Explanation of classes

- Roman\_Numeral:
	- class that holds enums for a roman numeral, a chord inversion, and mode.
	- relative representation of harmony that is used to traverse the Harmony\_Graph and convert to Chord.

- Chord:
	- class that holds information about an absolute harmony derived from its roman numeral representation and a specified tonic.
	- has a method to create the required chord representation in lilypond

- Progression
	- class that holds a list of roman numerals and chord equivalents.
	- has a method to create the entire content of a lilypond file based on the its progression

- Harmony\_Graph:
	- an adjacency list that holds edges to each available roman numeral 

## Flaws that are painfully obvious

- The range of the Harmony\_Graph is limited. It's really only accounting for the major scale. I setup the enums to support minor as well, so hopefully I might be able to extend it out to get more variety in each run.

- To try and alleviate the first program, I decided to try and introduce a Neopolitan chord to the Harmony\_Graph; I somehow introduced some new, inadvertent harmonies as well, though I guess it makes output a little more colorful, even if it's technically stretching functional tonal harmony.

- I don't think I had a very strong plan for how to make a visual. It came about when I learned that pygame could play MIDI, so I tried to syncronize something. I did get the spawning of lines to line up with the tempo, but that was about it. It is kinda amusing, though, if you bump up the bpm to 200+.

- There's more I need to learn about lilypond. There's certain threshold notes that cause the chord to leap an octave; the voicing isn't as good as it could be. 
