from argparse import ArgumentParser
from pathlib import Path

import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt


def Print_Graph(filename, title):
    samplerate, data = extract_data(filename)
    print(f"Sample rate = {samplerate}")

    length = data.shape[0] / samplerate
    print(f"length = {length}s")

    time = np.linspace(0., length, data.shape[0])
    plt.title(title)
    plt.plot(time, data, label = "Sound Wave")
    plt.legend()
    plt.xlabel("time[s]")
    plt.ylabel("Amplitude")
    plt.show()

    return 0

def extract_data(filename):
    samplerate, data = wav.read(filename)
    return samplerate, data

def Goertzel(WantedFrequency, sample, samplerate):
    N = len(sample)
    k = int(0.5 + (N * WantedFrequency / samplerate))
    w = 2 * np.pi * k / N
    cos = np.cos(w)
    sin = np.sin(w)
    coeff = 2 * cos
    scale = N / 2
    
    a = 0
    b = 0
    c = 0
    
    for i in range(0, N):
        a = sample[i] + (coeff * b) - c
        c = b
        b = a
    
    real = (a - (b * cos)) / scale
    image = (- b * sin) / scale
    power = np.sqrt(real * real + image * image)
    
    return power

def DTMF(filename):
    #check for all cases
    freq_table_1 = np.array([697, 770, 852, 941])
    freq_table_2 = np.array([1209, 1336, 1477, 1633])
    freq_num_table = np.array([[1, 2, 3, "A"],
                               [4, 5, 6, "B"],
                               [7, 8, 9, "C"],
                               ["*", 0, "#", "D"]])
    
    samplerate, sample = extract_data(filename)
    
    begin = 0
    end = 800
    
    nb_blocs = (sample.shape[0] / samplerate) * 1000 / 100
    sample_bloc = sample[begin : end]
    
    for k in range(0, int(nb_blocs)):
        begin += 800
        end += 800
        for i in range(0, 4):
            if (Goertzel(freq_table_1[i], sample_bloc, samplerate) >= 15):
                for j in range(0, 4):
                    if (Goertzel(freq_table_2[j], sample_bloc, samplerate) >= 15):
                        print(f"{freq_num_table[i][j]}")   
        sample_bloc = sample[begin : end]

if __name__ == "__main__":
    parser = ArgumentParser(description = "DTMF decoder")
    parser.add_argument('Audio_File', help = "need a .wav file")
    parser.add_argument('-p', '--print', action = "store_true", 
    help = "print some infos and a graph")

    args = parser.parse_args()

    filename = Path(args.Audio_File).absolute()
    
    #computation
    DTMF(filename)
    
    #print the graph
    if args.print:
        print("\nGraph Info :")
        Print_Graph(filename, args.Audio_File)