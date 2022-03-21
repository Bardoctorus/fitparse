import time
import rtmidi
from rtmidi.midiconstants import CONTROL_CHANGE, GENERAL_PURPOSE_CONTROLLER_1
from utils import utils
import sys



midiout = rtmidi.MidiOut()

if (len(sys.argv) < 2):

    available_ports = midiout.get_ports()
    print("available MIDI ports:")
    for i in available_ports: 
        print(i)
    
    port = int(input("choose midi port\n"))

else:
    port = int(sys.argv[1])
midiout.open_port(port)

x = range (1,100,10)

with midiout:
    while True:
        knob = input("which control knob do you want to set?")
        
        print("twiddling knob 1 for 10 seconds")
        for i in x:
            control = [CONTROL_CHANGE, GENERAL_PURPOSE_CONTROLLER_1, i]
            midiout.send_message(control)
            print(control)
            time.sleep(1) 

