import librosa

y, sr = librosa.load("test.wav", sr=44100, mono=True)
print(len(y), sr)

