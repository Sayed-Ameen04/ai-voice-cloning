
import tkinter as tk

from voice_engine import VoiceEngine
from audio_recorder import AudioRecorder
from gui import VoiceCloningGUI


def main():
    # Initialize AI voice engine
    voice_engine = VoiceEngine()

    # Initialize audio recorder
    recorder = AudioRecorder()

    # Create Tkinter window
    window = tk.Tk()

    # Create application GUI
    VoiceCloningGUI(
        window,
        voice_engine,
        recorder
    )

    # Start GUI event loop
    window.mainloop()


if __name__ == "__main__":
    main()

