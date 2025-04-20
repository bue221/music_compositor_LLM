from langgraph.graph import StateGraph, END

from src.states.compositor_state import MusicState
from src.graphs.compositor_music.nodes import (
    melody_generator,
    harmony_generator,
    rhythm_generator,
    style_adapter,
    midi_converter,
)

workflow = StateGraph(MusicState)

workflow.add_node("melody_generator", melody_generator)
workflow.add_node("harmony_creator", harmony_generator)
workflow.add_node("rhythm_analyzer", rhythm_generator)
workflow.add_node("style_adapter", style_adapter)
workflow.add_node("midi_converter", midi_converter)

workflow.set_entry_point("melody_generator")

workflow.add_edge("melody_generator", "harmony_creator")
workflow.add_edge("harmony_creator", "rhythm_analyzer")
workflow.add_edge("rhythm_analyzer", "style_adapter")
workflow.add_edge("style_adapter", "midi_converter")
workflow.add_edge("midi_converter", END)

app = workflow.compile()
