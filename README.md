# Dual-tone multi-frequency Decoder

This is a Dual-tone multi-frequency (DTMF) decoder that takes one (.wav
8bits 8KHz) sound and print on standard output all numbers that it contains.

## Installation

there are some required libraries.
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install 
requierments.

```bash
pip install --user requierments.txt
```

## Usage

```python
python decoder.py your_8bit_sound.py
```

## Process

I started by making a main function to parse arguments

Then I focused on the reading of a soundfile using scipy.io.wavfile.read 
and printing a graph

Once that was achieved I started to try implement 
the Goertzel algorithm in python (reading on all sound at once)

On top of this I implemented my DTMF function 
to split the sound into 100ms chunks and check for all combinasons 
and print the number stored in a table

## GitHub

[My GitHub](https://github.com/topodoco/octave.genest-jenny)

## Source

[Goertzel Algorithm Wikipedia](https://en.wikipedia.org/wiki/Goertzel_algorithm)