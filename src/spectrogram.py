import librosa
import librosa.display
import matplotlib.pyplot as plt

audio_path = "samples/test.wav"

signal, sr = librosa.load(audio_path)

spectrogram = librosa.stft(signal)
spectrogram_db = librosa.amplitude_to_db(abs(spectrogram))

plt.figure(figsize=(10,4))
librosa.display.specshow(spectrogram_db, sr=sr, x_axis="time", y_axis="hz")
plt.colorbar(format="%+2.0f dB")
plt.title("Spectrogram")

plt.savefig("outputs/spectrogram.png")
plt.show()