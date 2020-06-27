from argparse import ArgumentParser
from pathlib import Path

import scipy.io.wavfile as wav
import numpy as np
import matplotlib.pyplot as plt
#import time

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

def Goertzel(filename, WantedFrequency):
    samplerate, sample = extract_data(filename)
    N = len(sample)
    k = 0.5 + (N * WantedFrequency / samplerate)
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

def DTMF(file):
    #check for all cases
    print("Extracted numbers :")
    freq_table_1 = np.array([697, 770, 852, 941])
    freq_table_2 = np.array([1209, 1336, 1477, 1633])
    freq_num_table = np.array([[1, 2, 3, 10],
                               [4, 5, 6, 11],
                               [7, 8, 9, 12],
                               [13, 0, 14, 15]])
    for i in range(0, 4):
        if (Goertzel(file, freq_table_1[i]) >= 1):
            for j in range(0, 4):
                if (Goertzel(file, freq_table_2[j]) >= 1):
                    print(f"{freq_num_table[i][j]}")                
    
    #print the graph
    print("\nGraph Info :")
    Print_Graph(file, args.Audio_File)

if __name__ == "__main__":
    parser = ArgumentParser(description = "DTMF decoder")
    parser.add_argument('Audio_File', help = "need a .wav file")

    args = parser.parse_args()

    file = Path(args.Audio_File).absolute()
    
    #computation
    DTMF(file)
    
    #freq = 852
    #Goertzel = Goertzel(file, freq)
    #print("Computation :")
    #print(f"power = {Goertzel}")