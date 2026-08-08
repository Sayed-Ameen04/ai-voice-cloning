
import tkinter as tk
from tkinter import filedialog, ttk
import winsound
import threading
import os


class VoiceCloningGUI:
    def __init__(self, window, voice_engine, recorder):
        self.window = window
        self.voice_engine = voice_engine
        self.recorder = recorder

        self.reference_path = "reference.wav"
        self.output_path = "output.wav"

        self._setup_window()
        self._create_widgets()

    # ---------------- WINDOW ----------------

    def _setup_window(self):
        self.window.title("AI Voice Cloning System")
        self.window.geometry("600x550")
        self.window.configure(bg="#1e1e2f")

    # ---------------- WIDGETS ----------------

    def _create_widgets(self):

        title_label = tk.Label(
            self.window,
            text="AI Voice Cloning System",
            font=("Segoe UI", 18, "bold"),
            bg="#1e1e2f",
            fg="white"
        )
        title_label.pack(pady=20)

        main_frame = tk.Frame(
            self.window,
            bg="#1e1e2f"
        )
        main_frame.pack(pady=10)

        # Upload button

        upload_button = tk.Button(
            main_frame,
            text="Upload Reference Voice",
            command=self.upload_file,
            font=("Segoe UI", 10),
            bg="#4e73df",
            fg="white",
            width=25,
            relief="flat"
        )
        upload_button.pack(pady=8)

        # Recording buttons

        record_button = tk.Button(
            main_frame,
            text="Start Recording",
            command=self.start_recording,
            font=("Segoe UI", 10),
            bg="#e74a3b",
            fg="white",
            width=25,
            relief="flat"
        )
        record_button.pack(pady=5)

        stop_button = tk.Button(
            main_frame,
            text="Stop Recording",
            command=self.stop_recording,
            font=("Segoe UI", 10),
            bg="#858796",
            fg="white",
            width=25,
            relief="flat"
        )
        stop_button.pack(pady=5)

        # Language

        language_label = tk.Label(
            main_frame,
            text="Select Language:",
            font=("Segoe UI", 11),
            bg="#1e1e2f",
            fg="white"
        )
        language_label.pack(pady=(15, 5))

        self.language_var = tk.StringVar()

        language_dropdown = ttk.Combobox(
            main_frame,
            textvariable=self.language_var,
            values=["English", "Hindi", "Marathi"],
            state="readonly",
            width=22
        )
        language_dropdown.pack()

        language_dropdown.current(0)

        # Text input

        text_label = tk.Label(
            main_frame,
            text="Enter Text:",
            font=("Segoe UI", 11),
            bg="#1e1e2f",
            fg="white"
        )
        text_label.pack(pady=(15, 5))

        self.text_entry = tk.Entry(
            main_frame,
            width=50,
            font=("Segoe UI", 11),
            relief="flat"
        )
        self.text_entry.pack(pady=8, ipady=5)

        # Generate button

        self.generate_button = tk.Button(
            main_frame,
            text="Generate Voice",
            command=self.generate_voice,
            font=("Segoe UI", 10),
            bg="#1cc88a",
            fg="white",
            width=25,
            relief="flat"
        )
        self.generate_button.pack(pady=10)

        # Play button

        self.play_button = tk.Button(
            main_frame,
            text="Play Audio",
            command=self.play_audio,
            font=("Segoe UI", 10),
            bg="#f6c23e",
            fg="black",
            width=25,
            relief="flat",
            state="disabled"
        )
        self.play_button.pack(pady=8)

        # Status

        self.status_label = tk.Label(
            self.window,
            text="Status: Ready",
            font=("Segoe UI", 10),
            bg="#1e1e2f",
            fg="#4e73df"
        )
        self.status_label.pack(pady=20)

    # ---------------- FILE UPLOAD ----------------

    def upload_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("WAV files", "*.wav")]
        )

        if file_path:
            self.reference_path = file_path
            self.status_label.config(
                text="Reference File Selected"
            )

    # ---------------- RECORDING ----------------

    def start_recording(self):
        self.recorder.start()

        self.status_label.config(
            text="Recording... Speak clearly"
        )

    def stop_recording(self):
        self.recorder.stop(self.reference_path)

        self.status_label.config(
            text="Recording Saved Successfully"
        )

    # ---------------- VOICE GENERATION ----------------

    def generate_voice(self):

        text = self.text_entry.get().strip()
        language = self.language_var.get()

        if not text:
            self.status_label.config(
                text="Please enter text"
            )
            return

        if not os.path.exists(self.reference_path):
            self.status_label.config(
                text="Upload or record reference audio"
            )
            return

        self.generate_button.config(state="disabled")
        self.play_button.config(state="disabled")

        self.status_label.config(
            text="Generating voice... Please wait"
        )

        threading.Thread(
            target=self._generate_voice_thread,
            args=(text, language),
            daemon=True
        ).start()

    def _generate_voice_thread(self, text, language):

        try:

            self.voice_engine.generate(
                text,
                self.reference_path,
                language,
                self.output_path
            )

            self.window.after(
                0,
                self._generation_success
            )

        except Exception as error:

            self.window.after(
                0,
                lambda: self._generation_error(error)
            )

    def _generation_success(self):

        self.status_label.config(
            text="Voice Generated Successfully"
        )

        self.play_button.config(
            state="normal"
        )

        self.generate_button.config(
            state="normal"
        )

    def _generation_error(self, error):

        self.status_label.config(
            text=f"Error: {error}"
        )

        self.generate_button.config(
            state="normal"
        )

    # ---------------- AUDIO PLAYBACK ----------------

    def play_audio(self):

        if os.path.exists(self.output_path):

            winsound.PlaySound(
                self.output_path,
                winsound.SND_FILENAME | winsound.SND_ASYNC
            )

            self.status_label.config(
                text="Playing Audio..."
            )

        else:

            self.status_label.config(
                text="No generated file found"
            )

