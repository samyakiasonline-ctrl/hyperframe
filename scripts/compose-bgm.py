"""Compose an original uplifting piano + strings bed from FluidR3_GM note samples (CC-BY 3.0).

Usage: python compose-bgm.py <samples-dir> <out.mp3>, where <samples-dir> holds
<instrument>/<Note><Octave>.mp3 files from gleitz/midi-js-soundfonts (FluidR3_GM).
"""
import subprocess, sys
import numpy as np

SAMPLES, OUT = sys.argv[1], sys.argv[2]
SR = 44100
BPM = 84
BEAT = 60 / BPM
BAR = 4 * BEAT
LENGTH = 16.5
_cache = {}

def note(inst, name):
    key = (inst, name)
    if key not in _cache:
        raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f"{SAMPLES}/{inst}/{name}.mp3",
                              "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"],
                             capture_output=True, check=True).stdout
        _cache[key] = np.frombuffer(raw, dtype=np.float32).copy()
    return _cache[key]

mix = np.zeros((2, int(SR * (LENGTH + 4))), dtype=np.float32)

def place(inst, name, t, gain, pan=0.0, length=None, attack=0.0):
    s = note(inst, name).copy()
    if length is not None:
        n = min(len(s), int(length * SR))
        s = s[:n]
        rel = min(int(0.35 * SR), n)
        s[-rel:] *= np.linspace(1, 0, rel) ** 2
    if attack > 0:
        a = min(int(attack * SR), len(s))
        s[:a] *= np.linspace(0, 1, a)
    i = int(t * SR)
    l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    mix[0, i:i + len(s)] += s * gain * l
    mix[1, i:i + len(s)] += s * gain * r

# (bass, arpeggio notes, pad notes, melody on beats 1 & 3) per half bar
C  = ("C2", ["C3", "G3", "C4", "E4"], ["C4", "E4", "G4"])
G  = ("G2", ["G2", "D3", "G3", "B3"], ["D4", "G4", "B4"])
Am = ("A2", ["A2", "E3", "A3", "C4"], ["C4", "E4", "A4"])
F  = ("F2", ["F2", "C3", "F3", "A3"], ["C4", "F4", "A4"])
HALVES = [C, C, G, G, Am, Am, F, F, F, G, C, C]
MELODY = ["E5", "G5", "D5", "B4", "C5", "E5", "A4", "C5", "A4", "B4", "E5", None]
ARP = [0, 1, 2, 3]

for h, (bass, arp, pad) in enumerate(HALVES):
    t0 = h * BAR / 2
    last = h >= len(HALVES) - 2
    if h % 2 == 0 or HALVES[h - 1] is not HALVES[h]:
        place("acoustic_grand_piano", bass, t0, 0.55)
    for k in range(4):  # eighth-note arpeggio
        if last and k > 0 and h == len(HALVES) - 1:
            break
        nn = arp[ARP[k]]
        place("acoustic_grand_piano", nn, t0 + k * BEAT / 2, 0.30 if k == 0 else 0.22,
              pan=(-0.35, 0.15, 0.35, -0.1)[k], length=1.6)
    for p, nn in enumerate(pad):  # sustained strings, slow swell
        place("string_ensemble_1", nn, t0, 0.16, pan=(-0.5, 0.0, 0.5)[p], attack=0.5)
    if MELODY[h]:
        place("acoustic_grand_piano", MELODY[h], t0, 0.38, pan=0.1, length=2.4 if last else 1.9)

# Final chord rings out.
for nn in ["C3", "G3", "C4", "E4", "G4", "C5"]:
    place("acoustic_grand_piano", nn, 10 * BAR / 2 + BEAT, 0.16, length=3.0)

# Reverb: deterministic decaying-noise impulse response.
rng = np.random.default_rng(7)
ir_len = int(1.9 * SR)
env = np.exp(-np.linspace(0, 7, ir_len))
wet = np.zeros_like(mix)
for ch in range(2):
    ir = rng.standard_normal(ir_len).astype(np.float32) * env
    ir /= np.sqrt(np.sum(ir ** 2))
    n = mix.shape[1] + ir_len
    nfft = 1 << (n - 1).bit_length()
    wet[ch] = np.fft.irfft(np.fft.rfft(mix[ch], nfft) * np.fft.rfft(ir, nfft), nfft)[:mix.shape[1]]
out = 0.78 * mix + 0.32 * wet

out = out[:, :int(LENGTH * SR)]
fi, fo = int(0.25 * SR), int(1.6 * SR)
out[:, :fi] *= np.linspace(0, 1, fi)
out[:, -fo:] *= np.linspace(1, 0, fo) ** 1.5
out *= 0.89 / np.max(np.abs(out))

subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ac", "2", "-ar", str(SR), "-i", "-",
                "-c:a", "libmp3lame", "-b:a", "256k", OUT],
               input=out.T.astype(np.float32).tobytes(), check=True)
print("wrote", OUT)
