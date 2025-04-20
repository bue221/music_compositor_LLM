from typing import Dict
from langchain.prompts import ChatPromptTemplate
import music21
import random
import datetime

from src.states.compositor_state import MusicState
from src.graphs.compositor_music.config import llm
from src.graphs.compositor_music.constants import scales, chords


def melody_generator(state: MusicState) -> Dict:
    prompt = ChatPromptTemplate.from_template(
        "Crea una melodía sofisticada inspirada en las técnicas compositivas de Bach y Beethoven. "
        "La melodía debe:\n"
        "- Tener una duración mínima de 30 segundos\n"
        "- Incluir elementos de contrapunto\n"
        "- Utilizar escalas y modos apropiados\n"
        "- Tener una estructura musical clara (ej: forma A-B-A)\n"
        "- Incluir variaciones en dinámica y articulación\n"
        "- Combinar movimientos por grados conjuntos y saltos\n"
        "- Considerar principios de conducción de voces\n"
        "Contexto de entrada: {input}\n"
        "Representa las notas como strings en formato music21."
    )

    chain = prompt | llm
    melody = chain.invoke({"input": state["musician_input"]})

    return {"melody": melody.content}


def harmony_generator(state: MusicState) -> Dict:
    prompt = ChatPromptTemplate.from_template(
        "Crea una progresión armónica rica para la siguiente melodía: {melody}\n"
        "La armonía debe:\n"
        "- Utilizar principios de armonía funcional\n"
        "- Incluir dominantes secundarias y modulaciones\n"
        "- Considerar conducción de voces y resoluciones apropiadas\n"
        "- Añadir suspensiones y notas de paso apropiadas\n"
        "- Crear puntos de tensión y resolución\n"
        "Representa los acordes como strings en formato music21."
    )

    chain = prompt | llm
    harmony = chain.invoke({"melody": state["melody"]})

    return {"harmony": harmony.content}


def rhythm_generator(state: MusicState) -> Dict:
    prompt = ChatPromptTemplate.from_template(
        "Analiza y crea un ritmo sofisticado para la siguiente melodía y armonía:\n"
        "Melodía: {melody}\n"
        "Armonía: {harmony}\n"
        "El ritmo debe:\n"
        "- Incluir sincopación y polirritmos\n"
        "- Variar entre compases simples y compuestos\n"
        "- Crear tensión y resolución rítmica\n"
        "- Usar marcas de articulación apropiadas\n"
        "- Considerar el estilo de Bach y Beethoven\n"
        "Representa la duración como strings en formato music21."
    )

    chain = prompt | llm
    rhythm = chain.invoke({"melody": state["melody"], "harmony": state["harmony"]})

    return {"rhythm": rhythm.content}


def style_adapter(state: MusicState) -> Dict:
    prompt = ChatPromptTemplate.from_template(
        "Adapta la siguiente composición al estilo {style} manteniendo la sofisticación clásica:\n"
        "Melodía: {melody}\n"
        "Armonía: {harmony}\n"
        "Ritmo: {rhythm}\n"
        "Asegúrate que la adaptación:\n"
        "- Preserva la integridad musical\n"
        "- Mantiene la duración mínima de 30 segundos\n"
        "- Conserva el nivel de complejidad de Bach/Beethoven\n"
        "- Adapta la instrumentación apropiadamente\n"
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
        scale_name = "C minor blues"
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

    # Generate filename with timestamp
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"music/composition_{timestamp}.mid"

    piece.write("midi", filename)

    return {"midi_file": filename}
