from argparse import ArgumentParser
from pathlib import Path

import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
#import time

def Print_Graph(filename):
    print(filename)
    samplerate, data = wav.read(filename)

    length = data.shape[0] / samplerate
    print(f"length = {length}s")

    time = np.linspace(0., length, data.shape[0])
    print(time)
    plt.plot(time, data, label = "Sound Wave")
    plt.legend()
    plt.xlabel("time[s]")
    plt.ylabel("Amplitude")
    plt.show()

    return 0

if __name__ == "__main__":
    parser = ArgumentParser(description = "DTMF decoder")
    parser.add_argument('Audio_File', help = "need a .wav file")

    args = parser.parse_args()

    print(args.Audio_File)
    file = Path(args.Audio_File).absolute()
    print(file)

    Print_Graph(file)