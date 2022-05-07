import librosa
import os
import numpy as np

#path = '../data/lazy-vocal.mp3'
path = '../data/happy-full.wav'
assert os.path.exists(path), "The file does not exist."
y, sr = librosa.load(path)
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
print('Estimated tempo: {:.2f} beats per minute'.format(tempo))
beat_times = librosa.frames_to_time(beat_frames, sr=sr)
print(beat_times)

gaps = []
for i in range(len(beat_times)):
    if i > 0:
        gap = beat_times[i] - beat_times[i-1]
        gaps.append(gap)

np_gaps = np.array(gaps)

print("max gap:", max(gaps))
print("min gap:", min(gaps))
print("avg gap:", np.mean(np_gaps))
mean = np.mean(np_gaps)
print("median gap:", np.median(np_gaps))
std_dev = np.std(np_gaps)
print("std gap:", np.std(np_gaps))

index_dic = {}
for i in range(len(beat_times)):
    if i > 0:
        gap = beat_times[i] - beat_times[i-1]
        index_dic[i] = gap
        if gap > mean + std_dev:
            print("gap:", i, ":", gap)

print("beat frames", beat_frames)
print("sampling rate", sr)