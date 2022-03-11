import time
import rtmidi
from utils import utils

midiout = rtmidi.MidiOut()

midiout.open_port(1)


while True:
    counter = 0

    print("twiddling knob 1 for 10 seconds")
    control = [0xB0, 0x10, ]


