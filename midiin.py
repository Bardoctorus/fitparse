#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# midiclock.py
#
"""Receive MIDI clock and print out current BPM.

MIDI clock (status 0xF8) is sent 24 times per quarter note by clock generators.

"""

# TODO: strip the core of this out and use it as a basic trigger in

import time
from collections import deque

from rtmidi.midiconstants import (TIMING_CLOCK, SONG_CONTINUE, SONG_START, SONG_STOP)
from rtmidi.midiutil import open_midiinput
import rtmidi


class MIDIClockReceiver:
    def __init__(self, bpm=None):
        self.bpm = bpm if bpm is not None else 120.0
        self.sync = False
        self.running = True
        self._samples = deque()
        self._last_clock = None
        self.clockcount = 0

    def __call__(self, event, data=None):
        msg, _ = event
       
        if msg[0] == TIMING_CLOCK:
            now = time.time()

            if self._last_clock is not None:
                self._samples.append(now - self._last_clock)

            self._last_clock = now

            if len(self._samples) > 24:
                self._samples.popleft()
            

            if len(self._samples) >= 2:
                self.bpm = 2.5 / (sum(self._samples) / len(self._samples))
                self.sync = True
            self.clockcount += 1    
            if self.clockcount > 96:
                self.clockcount = 0

        elif msg[0] in (SONG_CONTINUE, SONG_START):
            self.running = True
            print("START/CONTINUE received.")
        elif msg[0] == SONG_STOP:
            self.running = False
            print("STOP received.")


def main(args=None):

    clock = MIDIClockReceiver()
    note_on = [0x90, 40, 112]
    note_off = [0x80, 40, 0]
    try:
        m_in, port_name = open_midiinput(0)
        m_out = rtmidi.MidiOut()
        m_out.open_port(1)
    except (EOFError, KeyboardInterrupt):
        return 1

    m_in.set_callback(clock)
    # Important: enable reception of MIDI Clock messages (status 0xF8)
    m_in.ignore_types(timing=False)
    try:
        print("Waiting for clock sync...")
        while True:

  #          time.sleep(0.1)

            if clock.running:
                if clock.sync:
                    print(clock.clockcount)
                    if (clock.clockcount == 0):
                        m_out.send_message(note_on)
                    elif clock.clockcount > 20 and clock.clockcount < 22:

                        m_out.send_message(note_off)
                    else:
                        continue
#                    print("%.2f bpm" % clock.bpm)
#                else:
#                    print("%.2f bpm (no sync)" % clock.bpm)

    except KeyboardInterrupt:
        pass
    finally:
        m_in.close_port()
        del m_in


if __name__ == '__main__':
    import sys
    sys.exit(main() or 0)