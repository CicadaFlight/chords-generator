# chords-generator
A simple Python app that generates semi-random chord progressions.

DEMO: https://youtu.be/Pj6JNkYeW0Y

To start the program, run ChordsGeneratorGUI.py

DISCLAIMER: The code is a damn mess becuase I banged it out in a day and 
I didn't think I would be sharing it with anyone until I decided to post 
it on reddit. I'm convinced that the same program could be written with 
far less code given more time (or a more skilled dev *wink wink*).

The input parameters are:
**Root chord**: Whether the tonic should be major or minor (this could 
possibly have options for other scales in future versions). 
**Amount**: The number of chords to generate.
**Jazziness**: The probability of a 7th chord being generated. Setting Amount 
to 0 will be a 0% chance of 7th chords, and 100 will be 100% 7th chords.
**Include dim**: If this is unchecked, diminished chords will be omitted.

Essentially, the program logic is taken care of in the MusicScript.py file.
It consists of a single function that takes in a few parameters and
generates a semi-random chord progression (taking those parameters
into account).

The ChordsGeneratorGUI.py file contains the UI. This is the file to run 
to start the application.

// Cicada Flight
