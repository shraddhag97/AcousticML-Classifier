import librosa
import matplotlib.pyplot as plt

audio_path = "samples/test.wav"

signal, sr = librosa.load(audio_path)

print("Sample rate:", sr)
print("Signal shape:", signal.shape)

plt.figure(figsize=(10,4))
plt.plot(signal)
plt.title("Audio Waveform")
plt.xlabel("Samples")
plt.ylabel("Amplitude")

plt.savefig("outputs/waveform.png")
plt.show()