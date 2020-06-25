from argparse import ArgumentParser
from pathlib import Path

import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
#import time

def Print_Graph(filename):
    print(filename)
    samplerate, data = sio.wavfile.read(filename)

    print(f"number of channels = {data.shape[1]}")

    length = data.shape[0] / samplerate
    print(f"length = {length}s")

    time = np.linspace(0., length, data.shape[0])
    plt.plot(time, data[:, 0], label = "Left channel")
    plt.plot(time, data[:, 1], label = "Rigth channel")
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
