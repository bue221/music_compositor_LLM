from typing import Dict
from langchain.prompts import ChatPromptTemplate
import music21
import random
import tempfile

from src.states.compositor_state import MusicState
from src.graphs.compositor_music.config import llm


def melody_generator(state: MusicState) -> Dict:
    prompt = ChatPromptTemplate.from_template(
        "Genera la melodia base para la siguiente entrada: {input}. "
        "Representando las notas como strings en el formato music21."
    )

    chain = prompt | llm
    melody = chain.invoke({"input": state["musician_input"]})

    return {"melody": melody.content}


def harmony_generator(state: MusicState) -> Dict:
    prompt = ChatPromptTemplate.from_template(
        "Crea la armonia para la siguiente melodia: {melody}. "
        "Representando los acordes como strings en el formato music21."
    )

    chain = prompt | llm
    harmony = chain.invoke({"melody": state["melody"]})

    return {"harmony": harmony.content}


def rhythm_generator(state: MusicState) -> Dict:
    prompt = ChatPromptTemplate.from_template(
        "Analiza y sugiere un ritmo para la siguiente melodia y armonia: "
        "{melody} y {harmony}. Representando la duracion como strings en el formato music21."
    )

    chain = prompt | llm
    rhythm = chain.invoke({"melody": state["melody"], "harmony": state["harmony"]})

    return {"rhythm": rhythm.content}


def style_adapter(state: MusicState) -> Dict:
    prompt = ChatPromptTemplate.from_template(
        "Adapta la siguiente composición al {style} style: "
        "Melodia: {melody}, Armonia: {harmony}, Ritmo: {rhythm}. "
        "Entrega el resultado en formato music21."
    )

    chain = prompt | llm
    composition = chain.invoke(
        {
            "melody": state["melody"],
            "harmony": state["harmony"],
            "rhythm": state["rhythm"],
            "style": state["style"],
        }
    )

    return {"composition": composition.content}


def midi_converter(state: MusicState) -> Dict:
    piece = music21.stream.Score()
    description = music21.expressions.TextExpression(state["composition"])
    piece.append(description)

    scales = {
        "C major": ["C", "D", "E", "F", "G", "A", "B"],
        "C minor": ["C", "D", "Eb", "F", "G", "Ab", "Bb"],
        "C harmonic minor": ["C", "D", "Eb", "F", "G", "Ab", "B"],
        "C melodic minor": ["C", "D", "Eb", "F", "G", "A", "B"],
        "C dorian": ["C", "D", "Eb", "F", "G", "A", "Bb"],
        "C phrygian": ["C", "Db", "Eb", "F", "G", "Ab", "Bb"],
        "C lydian": ["C", "D", "E", "F#", "G", "A", "B"],
        "C mixolydian": ["C", "D", "E", "F", "G", "A", "Bb"],
        "C locrian": ["C", "Db", "Eb", "F", "Gb", "Ab", "Bb"],
        "C whole tone": ["C", "D", "E", "F#", "G#", "A#"],
        "C diminished": ["C", "D", "Eb", "F", "Gb", "Ab", "A", "B"],
    }

    chords = {
        "C major": ["C4", "E4", "G4"],
        "C minor": ["C4", "Eb4", "G4"],
        "C diminished": ["C4", "Eb4", "Gb4"],
        "C augmented": ["C4", "E4", "G#4"],
        "C dominant 7th": ["C4", "E4", "G4", "Bb4"],
        "C major 7th": ["C4", "E4", "G4", "B4"],
        "C minor 7th": ["C4", "Eb4", "G4", "Bb4"],
        "C half-diminished 7th": ["C4", "Eb4", "Gb4", "Bb4"],
        "C fully diminished 7th": ["C4", "Eb4", "Gb4", "A4"],
    }

    def create_melody(scale_name, duration):
        melody = music21.stream.Part()
        scale = scales[scale_name]
        for i in range(duration):
            note = music21.note.Note(random.choice(scale) + "4")
            note.quarterLength = 1
            melody.append(note)
        return melody

    def create_chord_progression(duration):
        harmony = music21.stream.Part()
        for i in range(duration):
            chord_name = random.choice(list(chords.keys()))
            chord = music21.chord.Chord(chords[chord_name])
            chord.quarterLength = 1
            harmony.append(chord)
        return harmony

    user_input = state["musician_input"].lower()

    if "minor" in user_input:
        scale_name = "C minor"
    elif "major" in user_input:
        scale_name = "C major"
    else:
        scale_name = random.choice(list(scales.keys()))

    melody = create_melody(scale_name, 10)
    harmony = create_chord_progression(10)

    final_note = music21.note.Note(scales[scale_name][0] + "4")
    final_note.quarterLength = 1
    melody.append(final_note)

    final_chords = music21.chord.Chord(
        chords[scale_name.split()[0] + " " + scale_name.split()[1]]
    )
    final_chords.quarterLength = 1
    harmony.append(final_chords)

    piece.append(melody)
    piece.append(harmony)

    piece.insert(0, music21.tempo.MetronomeMark(number=60))

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mid") as temp_midi:
        piece.write("midi", temp_midi.name)

    return {"midi_file": temp_midi.name}
