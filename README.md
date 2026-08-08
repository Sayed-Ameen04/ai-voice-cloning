# 🎙️ AI Voice Cloning

> **A multilingual voice cloning application that transforms text into speech using a reference voice.**

AI Voice Cloning is a Python desktop application built around **Coqui XTTS v2**. It allows users to provide a reference voice either by uploading a WAV file or recording directly through the microphone, then generate speech in the selected language.

Currently supported:

🇬🇧 English · 🇮🇳 Hindi · 🇮🇳 Marathi

## ✨ Features

* 🎙️ **Record a reference voice** directly from the microphone
* 📁 **Upload WAV reference audio**
* 🗣️ **Voice cloning using XTTS v2**
* 🌍 **Multilingual speech generation**
* 🇬🇧 English
* 🇮🇳 Hindi
* 🇮🇳 Marathi
* 🔊 **Generate and play synthesized speech**
* 🖥️ **Desktop GUI built with Tkinter**
* ⚡ **Background generation** using Python threading

## 🧠 How It Works

```text
        Reference Voice
          /         \
         ↓           ↓
    Upload WAV    Microphone
         \           /
          ↓         ↓
        Reference Audio
               ↓
            XTTS v2
               ↓
      Text + Language
               ↓
       Synthesized Speech
               ↓
          output.wav
               ↓
          Audio Playback
```

The reference recording provides the speaker characteristics used by XTTS v2 when generating the requested speech.

## 🛠️ Tech Stack

| Technology      | Purpose                          |
| --------------- | -------------------------------- |
| 🐍 Python       | Core application                 |
| 🗣️ XTTS v2     | Voice cloning & speech synthesis |
| 🖥️ Tkinter     | Desktop GUI                      |
| 🎙️ SoundDevice | Microphone recording             |
| 🔢 NumPy        | Audio processing                 |
| 🔊 SciPy        | WAV file handling                |
| 🧵 Threading    | Non-blocking voice generation    |

## 📁 Project Structure

```text
ai-voice-cloning/
│
├── main.py              # Application entry point
├── gui.py               # Tkinter user interface
├── voice_engine.py      # XTTS v2 voice generation
├── audio_recorder.py    # Microphone recording
├── requirements.txt     # Python dependencies
└── .gitignore           # Ignored files
```

The project follows a modular structure where the GUI, audio recording, and voice generation logic are separated into independent components.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Sayed-Ameen04/ai-voice-cloning.git
cd ai-voice-cloning
```

### 2. Create a virtual environment

```bash
python -m venv voice_env
```

Activate it on Windows:

```bash
voice_env\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python main.py
```

The XTTS model will load when the application starts. Depending on your system, the initial setup and model loading may take some time.

## 🧠 What I Learned

Building this project helped me explore:

* Text-to-speech systems
* Voice cloning with a pretrained speech model
* Audio recording and WAV processing
* Working with microphone streams
* Multilingual speech generation
* Tkinter event-driven programming
* Python threading
* Modular application architecture
* Separating UI logic from application logic

## 🔮 Future Improvements

* 🎚️ Adjustable speech parameters
* 🎧 Improved audio controls
* 📊 Audio waveform visualization
* 🌍 Additional language support
* 💾 Custom output file selection
* 🎨 More polished desktop interface

## ⚠️ Responsible Use

This project is intended for **consensual and educational use**.

Only use voices that you own or have explicit permission to clone. Do not use voice cloning to impersonate or deceive others.

---

### Built with Python & XTTS v2

**Experiment → Build → Learn → Improve 🚀**
