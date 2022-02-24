import time
import rtmidi


midiout = rtmidi.MidiOut()

available_ports = midiout.get_ports()

for i in available_ports: 
    print(i)

if available_ports:
        print("Opening available midi port")
        midiout.open_port(1)
else:
    print("No port available, opening virtual port")
    midiout.open_virtual_port("My Virtual Output")


with midiout:
    note_on = [0x90, 60, 112]
    note_off = [0x80, 60, 0]
    while True:
        midiout.send_message(note_on)
        time.sleep(0.5)
        midiout.send_message(note_off)
        time.sleep(0.3)

