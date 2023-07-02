import librosa as ls

class Audio_Handler:
    def __init__(self, file_path: str):
        # self.audio_file = open(file_path)
        self.audio_series = ls.load(path=file_path)
        # print(self.audio_series)
        self.duration = ls.get_duration(y=self.audio_series[0])

        print(self.duration)

        # ls.hz_to_note()