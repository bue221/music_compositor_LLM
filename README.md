# Music Compositor

A modern web application for music composition with an intuitive interface and powerful features.

## 🎹 Features

### Melody Composition

- Interactive piano roll interface for note input
- Support for multiple scales (major, minor, pentatonic, etc.)
- Real-time playback of created melodies
- MIDI keyboard support

### General Features

- Save and load compositions
- Export to MIDI and audio formats (WAV, MP3)
- Visual representation of compositions (waveforms, bars)
- Undo/Redo functionality
- Project management

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- Conda package manager

### Environment Setup

1. Create a new conda environment:

```bash
conda create -n music-compositor python=3.11
conda activate music-compositor
```

2.Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

```bash
python src/main.py
```

## 🛠️ Technical Stack

- Python 3.11
- PyQt6 for GUI
- SoundDevice for audio processing
- MIDIUtil for MIDI file handling

## 📁 Project Structure

```
music-compositor/
├── src/                # Source code
├── tests/             # Test files
├── docs/              # Documentation
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
