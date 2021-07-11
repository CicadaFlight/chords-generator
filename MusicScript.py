import random

triads_maj = [
    "I",
    "ii",
    "iii",
    "IV",
    "V",
    "vi",
    "viidim"
]
four_note_maj = [
    "Imaj7",
    "iimin7",
    "iiimin7",
    "IVmaj7",
    "V7",
    "vimin7",
    "viimin7b5"
]
triads_min = [  # 2nd and 7th chords swapped for ternary expression in method
    "i",
    "VII",
    "III",
    "iv",
    "v",
    "VI",
    "iidim"
]
four_note_min = [ # 2nd and 7th chords swapped for ternary expression in method
    "imin7",
    "VII7",
    "IIImaj7",
    "ivmin7",
    "vmin7",
    "VImaj7",
    "iimin7b5"
]


def generate_chord_progression(type:str, chords=4, probabilityOf7ths=0, includeDiminished=False):
    progression = []

    # root chord placement
    root_placement = random.randrange(0, chords)

    # chords to use for received parameters
    max_chord_index = 7 if includeDiminished else 6
    four_note = four_note_maj if type == 'Major' else four_note_min
    triads = triads_maj if type == 'Major' else triads_min

    # put random chords in there
    for i in range(0, chords):
        # determine if triad or 4 note
        if random.random() < probabilityOf7ths:
            progression.append(four_note[random.randrange(0, max_chord_index)])
        else:
            progression.append(triads[random.randrange(0, max_chord_index)])

    # inject root if root isnt in
    if triads[0] not in progression:
        if random.random() < probabilityOf7ths:
            progression[root_placement] = four_note[0]
        else:
            progression[root_placement] = triads[0]

    return progression


if __name__ == "__main__":
    print(generate_chord_progression("minor", 4, 0.2))