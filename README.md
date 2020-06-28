# Dual-tone nulti-frequency Decoder

This is a Dual-tone multi-frequency (DTMF) decoder that takes one (.wav)
8bits sound and print on standard output all numbers that it contains.

## Installation

there are some required libraries

```bash
pip install --user requierments.txt
```

## Usage

```python
python decoder.py your_8bit_sound.py
```

## Process

J'ai tout d'abord comemncé par faire un main pour prendre des arguments,
puis je me suis concentré sur la lecture du sons et sa transformation 
en graph.

Il me reste desormais � traduire ce son en chiffre,

et enfin je m'occuperais du temps limite entre deux sons