from langgraph.graph import StateGraph


class MusicState(StateGraph):
    musician_input: str
    melody: str
    rhythm: str
    harmony: str
    output: str
    style: str
    composition: str
    midi_file: str
