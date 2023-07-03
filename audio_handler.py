import librosa as ls
from librosa import onset, beat
import matplotlib.pyplot as plt
import numpy as np

class Audio_Handler:
    def __init__(self, file_path: str):
        audio_series, sample_rate = ls.load(path=file_path, mono=True)  # (ndarray, float)
        self.duration = ls.get_duration(y=audio_series)
        bpm, beat_frames = self.get_bpm(audio_series=audio_series, sampling_array=sample_rate)
        print(f'bpm = {bpm}')
        # audio_frames = self.time_to_frames(audio_series=audio_series, sampling_rate=sample_rate)
        self.compute_freqs(audio_series=audio_series, sampling_rate=sample_rate, beat_frames=beat_frames)


    def get_bpm(self, audio_series: np.ndarray, sampling_array: float):  # can use to gauge accuracy of tempo
        tempo, beat_frames = beat.beat_track(y=audio_series, sr=sampling_array)
        # print('beat frames: ')
        # for b in beat_frames:
        #     print(b)
        return tempo, beat_frames


    def time_to_frames(self, audio_series: np.ndarray, sampling_rate: float):  # can pass in hop length if not default
        return ls.time_to_frames(times=audio_series, sr=sampling_rate)


    def compute_freqs(self, audio_series: np.ndarray, sampling_rate: float, beat_frames: list[int]):
        pitches, magnitudes = ls.piptrack(y=audio_series, sr=sampling_rate, fmin=75, fmax=1600)
        for i, b in enumerate(beat_frames):
            time = b
            index = magnitudes[:, time].argmax()
            pitch = pitches[index, time]
            note = ls.hz_to_note(pitch)
            print(note)  # 494hz = A4




