from librosa import *

class Audio_Handler:
    def __init__(self, file_path: str):
        # self.audio_file = open(file_path)
        self.audio_file = load(path=file_path)