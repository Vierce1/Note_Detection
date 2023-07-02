import librosa as ls
from librosa import onset, beat
import matplotlib.pyplot as plt
import numpy as np

class Audio_Handler:
    def __init__(self, file_path: str):
        # self.audio_file = open(file_path)
        audio_series, sample_rate = ls.load(path=file_path, mono=True)  # (ndarray, float)
        # print(self.audio_series)
        self.duration = ls.get_duration(y=audio_series)
        bpm, beat_frames = self.get_bpm(audio_series=audio_series, sampling_array=sample_rate)
        print(f'bpm = {bpm}')
        # audio_frames = self.time_to_frames(audio_series=audio_series, sampling_rate=sample_rate)
        self.compute_freqs(audio_series=audio_series, sampling_rate=sample_rate, beat_frames=beat_frames)


    def get_bpm(self, audio_series: np.ndarray, sampling_array: float):  # can use to gauge accuracy of tempo
        tempo, beat_frames = beat.beat_track(y=audio_series, sr=sampling_array)
        print('beat frames: ')
        for b in beat_frames:
            print(b)
        print('\n')
        return tempo, beat_frames


    def time_to_frames(self, audio_series: np.ndarray, sampling_rate: float):  # can pass in hop length if not default
        return ls.time_to_frames(times=audio_series, sr=sampling_rate)


    def compute_freqs(self, audio_series: np.ndarray, sampling_rate: float, beat_frames: list[int]):
        beat_times = ls.frames_to_time(frames=beat_frames, sr=sampling_rate)
        print('beats: ')
        [print(b) for b in beat_times]


        # onset_strength = onset.onset_strength(y=audio_series, sr=sampling_rate)
        # correlation = ls.autocorrelate(onset_strength)
        # fig, axis = plt.subplots()
        # axis.plot(correlation)
        # axis.set(title='Auto-correlation', xlabel='Lag (frames)')
        # plt.show()
        # for x in audio_series:
        #     try:
        #         # note = ls.hz_to_note(x)
        #         print(x)
        #     except: pass
