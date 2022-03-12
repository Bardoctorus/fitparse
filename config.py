<<<<<<< HEAD
import time
import rtmidi
from utils import utils

midiout = rtmidi.MidiOut()

# TODO make a better way of choosing midi port - with arg + backup
midiout.open_port(0)


while True:
    with midiout:
        counter = 0

        print("twiddling knob 1 for 10 seconds")
        for i in range(10):
            control = [0xB0, 0x10, i]
            midiout.send_message(control)
            print(control)
            time.sleep(1) 

