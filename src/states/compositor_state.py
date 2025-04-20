from typing_extensions import TypedDict


class InputState(TypedDict):
    musician_input: str
    style: str


class OutputState(TypedDict):
    musician_input: str
    melody: str
    harmony: str
    rhythm: str
    style: str
    composition: str
    midi_file: str


class MusicState(InputState, OutputState):
    pass
