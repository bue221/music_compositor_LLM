# Musical scales and modes
scales = {
    # Major scales and modes
    "C major": ["C", "D", "E", "F", "G", "A", "B"],
    "C ionian": ["C", "D", "E", "F", "G", "A", "B"],
    "C dorian": ["C", "D", "Eb", "F", "G", "A", "Bb"],
    "C phrygian": ["C", "Db", "Eb", "F", "G", "Ab", "Bb"],
    "C lydian": ["C", "D", "E", "F#", "G", "A", "B"],
    "C mixolydian": ["C", "D", "E", "F", "G", "A", "Bb"],
    "C aeolian": ["C", "D", "Eb", "F", "G", "Ab", "Bb"],
    "C locrian": ["C", "Db", "Eb", "F", "Gb", "Ab", "Bb"],
    # Minor scales
    "C natural minor": ["C", "D", "Eb", "F", "G", "Ab", "Bb"],
    "C harmonic minor": ["C", "D", "Eb", "F", "G", "Ab", "B"],
    "C melodic minor": ["C", "D", "Eb", "F", "G", "A", "B"],
    "C melodic minor descending": ["C", "D", "Eb", "F", "G", "Ab", "Bb"],
    "C minor pentatonic": ["C", "Eb", "F", "G", "Bb"],
    "C minor blues": ["C", "Eb", "F", "Gb", "G", "Bb"],
    "C minor bebop": ["C", "D", "Eb", "F", "G", "Ab", "A", "Bb"],
    "C minor diminished": ["C", "D", "Eb", "F", "Gb", "Ab", "A", "B"],
    "C minor augmented": ["C", "D", "Eb", "F", "G#", "A", "B"],
    "C minor double harmonic": ["C", "D", "Eb", "F#", "G", "Ab", "B"],
    "C minor hungarian": ["C", "D", "Eb", "F#", "G", "Ab", "B"],
    "C minor neapolitan": ["C", "Db", "Eb", "F", "G", "Ab", "Bb"],
    # Pentatonic scales
    "C major pentatonic": ["C", "D", "E", "G", "A"],
    "C blues": ["C", "Eb", "F", "Gb", "G", "Bb"],
    # Exotic scales
    "C whole tone": ["C", "D", "E", "F#", "G#", "A#"],
    "C diminished": ["C", "D", "Eb", "F", "Gb", "Ab", "A", "B"],
    "C augmented": ["C", "D#", "E", "G", "G#", "B"],
    "C hungarian minor": ["C", "D", "Eb", "F#", "G", "Ab", "B"],
    "C persian": ["C", "Db", "E", "F", "Gb", "Ab", "B"],
    "C japanese": ["C", "Db", "F", "G", "Ab"],
    "C hirajoshi": ["C", "Db", "E", "G", "Ab"],
}

# Chord progressions and voicings
chords = {
    # Triads
    "C major": ["C4", "E4", "G4"],
    "C minor": ["C4", "Eb4", "G4"],
    "C diminished": ["C4", "Eb4", "Gb4"],
    "C augmented": ["C4", "E4", "G#4"],
    "C suspended 2": ["C4", "D4", "G4"],
    "C suspended 4": ["C4", "F4", "G4"],
    # Seventh chords
    "C major 7": ["C4", "E4", "G4", "B4"],
    "C dominant 7": ["C4", "E4", "G4", "Bb4"],
    "C minor 7": ["C4", "Eb4", "G4", "Bb4"],
    "C minor major 7": ["C4", "Eb4", "G4", "B4"],
    "C half-diminished 7": ["C4", "Eb4", "Gb4", "Bb4"],
    "C fully diminished 7": ["C4", "Eb4", "Gb4", "A4"],
    "C augmented 7": ["C4", "E4", "G#4", "Bb4"],
    # Extended chords
    "C major 9": ["C4", "E4", "G4", "B4", "D5"],
    "C dominant 9": ["C4", "E4", "G4", "Bb4", "D5"],
    "C minor 9": ["C4", "Eb4", "G4", "Bb4", "D5"],
    "C major 11": ["C4", "E4", "G4", "B4", "D5", "F5"],
    "C dominant 13": ["C4", "E4", "G4", "Bb4", "D5", "F5", "A5"],
    # Altered chords
    "C7b5": ["C4", "E4", "Gb4", "Bb4"],
    "C7#5": ["C4", "E4", "G#4", "Bb4"],
    "C7b9": ["C4", "E4", "G4", "Bb4", "Db5"],
    "C7#9": ["C4", "E4", "G4", "Bb4", "D#5"],
    "C7b5b9": ["C4", "E4", "Gb4", "Bb4", "Db5"],
    "C7#5#9": ["C4", "E4", "G#4", "Bb4", "D#5"],
    # Add chords
    "C add9": ["C4", "E4", "G4", "D5"],
    "C add11": ["C4", "E4", "G4", "F5"],
    "C add13": ["C4", "E4", "G4", "A5"],
    "C6": ["C4", "E4", "G4", "A4"],
    "C6/9": ["C4", "E4", "G4", "A4", "D5"],
}

# Common chord progressions
CHORD_PROGRESSIONS = {
    "I-IV-V": ["C major", "F major", "G major"],
    "I-V-vi-IV": ["C major", "G major", "A minor", "F major"],
    "ii-V-I": ["D minor", "G major", "C major"],
    "I-vi-ii-V": ["C major", "A minor", "D minor", "G major"],
    "I-V-vi-iii-IV": ["C major", "G major", "A minor", "E minor", "F major"],
    "I-vi-IV-V": ["C major", "A minor", "F major", "G major"],
    "vi-IV-I-V": ["A minor", "F major", "C major", "G major"],
    "I-IV-vi-V": ["C major", "F major", "A minor", "G major"],
}

# Common scale patterns
SCALE_PATTERNS = {
    "major": [2, 2, 1, 2, 2, 2, 1],  # W-W-H-W-W-W-H
    "natural minor": [2, 1, 2, 2, 1, 2, 2],  # W-H-W-W-H-W-W
    "harmonic minor": [2, 1, 2, 2, 1, 3, 1],  # W-H-W-W-H-WH-H
    "melodic minor": [2, 1, 2, 2, 2, 2, 1],  # W-H-W-W-W-W-H
    "dorian": [2, 1, 2, 2, 2, 1, 2],  # W-H-W-W-W-H-W
    "phrygian": [1, 2, 2, 2, 1, 2, 2],  # H-W-W-W-H-W-W
    "lydian": [2, 2, 2, 1, 2, 2, 1],  # W-W-W-H-W-W-H
    "mixolydian": [2, 2, 1, 2, 2, 1, 2],  # W-W-H-W-W-H-W
    "locrian": [1, 2, 2, 1, 2, 2, 2],  # H-W-W-H-W-W-W
}
