from TTS.api import TTS


class VoiceEngine:
    def __init__(self):
        print("Loading XTTS model...")

        self.tts = TTS(
            model_name="tts_models/multilingual/multi-dataset/xtts_v2"
        )

        print("Model Loaded Successfully")

    def generate(self, text, reference_path, language, output_path):
        language_codes = {
            "English": "en",
            "Hindi": "hi",
            "Marathi": "mr"
        }

        lang_code = language_codes[language]

        text = text.replace(".", ". ")

        self.tts.tts_to_file(
            text=text,
            speaker_wav=reference_path,
            language=lang_code,
            file_path=output_path,
            split_sentences=True
        )