import json
import time
from pyo import *

# Download parametres
with open("params.json", "r") as f:
    params = json.load(f)

# Setting
tempo = params.get("tempo", 120)
duration = params.get("duration", 5)
notes = params.get("notes", [440])
waveform = params.get("waveform", "sine")
volume = params.get("volume", 0.5)

# Initializing the server
s = Server().boot()
s.recordOptions(dur=duration, filename="output.wav", fileformat=0)
s.start()
s.recstart()

# Sound generation
instruments = []

for i, freq in enumerate(notes):
    if waveform == "sine":
        osc = Sine(freq=freq, mul=volume).out()
    elif waveform == "square":
        osc = Square(freq=freq, mul=volume).out()
    elif waveform == "saw":
        osc = Saw(freq=freq, mul=volume).out()
    else:
        osc = Sine(freq=freq, mul=volume).out()
    instruments.append(osc)

time.sleep(duration)

s.recstop()
s.stop()
s.shutdown()
print("New Track: output.wav")
