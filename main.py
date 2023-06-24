import tkinter as tk
import sounddevice as sd
import threading

class VoiceRecorder:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Recorder")

        self.record_button = tk.Button(self.root, text="Record", command=self.start_recording)
        self.record_button.pack(pady=10)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_recording)
        self.stop_button.pack(pady=5)

        self.status_label = tk.Label(self.root, text="Status: Not recording")
        self.status_label.pack(pady=5)

        self.recording = False
        self.filename = "recording.wav"

    def start_recording(self):
        self.recording = True
        self.status_label.config(text="Status: Recording")

        # Create a new thread to handle audio recording
        self.recording_thread = threading.Thread(target=self.record_audio)
        self.recording_thread.start()

    def stop_recording(self):
        self.recording = False
        self.status_label.config(text="Status: Not recording")

    def record_audio(self):
        fs = 44100  # Sample rate
        duration = 10  # Recording duration in seconds

        recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished

        if self.recording:
            self.status_label.config(text="Status: Recording saved")

            # Save the recording to a WAV file
            sd.write(self.filename, recording, fs)

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    root = tk.Tk()
    voice_recorder = VoiceRecorder(root)
    voice_recorder.run()
