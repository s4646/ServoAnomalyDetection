import os
import librosa
import numpy as np
from scipy.io.wavfile import read
from torch.utils.data import Dataset

class Data(Dataset):
    def __init__(self, directory: str) -> None:
        self.X = []
        self.y = []
        for label in os.listdir(directory):
            for file in os.listdir(f"{directory}/{label}"):
                if file == "original": continue
                self.X.append(f"{directory}/{label}/{file}")
                self.y.append(int(label))

        self.len = len(self.X)
    
    def __getitem__(self, index) -> tuple:
        rate, audio = read(self.X[index])
        audio = librosa.resample(audio.astype(float), orig_sr=rate, target_sr=8000)
        label = self.y[index]
        return audio, label

    def __len__(self) -> int:
        return self.len