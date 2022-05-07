import librosa
import os
import numpy as np
from IPython.display import Audio
import mir_eval.sonify

path = '../data/happy-full.wav'
assert os.path.exists(path), "The file does not exist."

y, sr = librosa.load(path)

audio = Audio(data=y, rate=sr)
print(audio)


'''
hop_length = 512
n_fft = 2048

y_harmonic, y_percussive = librosa.effects.hpss(y)

tempo, beat_frames = librosa.beat.beat_track(y=y_percussive, sr=sr)

mfcc = librosa.feature.mfcc(y=y_harmonic, sr=sr, hop_length=hop_length, n_mfcc=13)

mfcc_delta = librosa.feature.delta(mfcc)

beat_mfcc_delta = librosa.util.sync(np.vstack([mfcc, mfcc_delta]), beat_frames)

chromogram = librosa.feature.chroma_cqt(y=y_harmonic, sr=sr)

beat_chroma = librosa.util.sync(chromogram, beat_frames, aggregate=np.median)

beat_features = np.vstack([beat_chroma, beat_mfcc_delta])

print(len(beat_frames))
print(beat_features.shape)
print(tempo)
'''