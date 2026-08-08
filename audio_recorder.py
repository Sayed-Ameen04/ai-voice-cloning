import sounddevice as sd
import numpy as np
from scipy.io.wavfile import write


class AudioRecorder:
    def __init__(self, sample_rate=24000):
        self.sample_rate = sample_rate
        self.recording_data = []
        self.recording_stream = None
        self.is_recording = False

    def _audio_callback(self, indata, frames, time, status):
        self.recording_data.append(indata.copy())

    def start(self):
        self.recording_data = []
        self.is_recording = True

        self.recording_stream = sd.InputStream(
            samplerate=self.sample_rate,
            channels=1,
            callback=self._audio_callback
        )

        self.recording_stream.start()

    def stop(self, output_path):
        if not self.recording_stream or not self.is_recording:
            return

        self.recording_stream.stop()
        self.recording_stream.close()

        self.is_recording = False

        audio = np.concatenate(self.recording_data, axis=0)

        # Normalize audio
        max_amplitude = np.max(np.abs(audio))

        if max_amplitude > 0:
            audio = audio / max_amplitude

        # Convert to 16-bit PCM
        audio = np.int16(audio * 32767)

        write(output_path, self.sample_rate, audio)
