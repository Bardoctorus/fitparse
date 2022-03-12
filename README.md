# Parsing FIT files because fuck APIs

Ok that's a bit dramatic. It just looks like using the raw fit data from the watch is gonna be better for getting super granular data for sonification.

This uses the fit-parse python library. 

Also RTmidi seems to be the simple way to punch midi data out using abritrary values. Map values to midi ranges, turn some of them into LFOs etc.
## The Basics of RTmidi

So the current miditest.py has examples of how to map a controller to things in Ableton. The hex bindings for all these controllers can be found in C:\Users\ianmb\git\fitparse\venv\Lib\site-packages\rtmidi\midiconstants.py

Don't forget you also need to configure your loopMIDI channel to be tracked and remoted in Ableton's midi settings to assign it to controls.


## Parsing Fit Files

The current lib is simple enough and gives us a load of values measured every second or so. Next job is to step through those values in real time (i.e follow the timestamps in the file) and return those values for processing

## Processing the data stream

All the data that comes in will need to be converted to Midi - but how? Several things come to mind:

straight remapping:

- direct numbers to notes for a note
- another number (time of day maybe) for major minor on a chord (can work with the above choosing note)
- feeding a number into sin() that might make interesting changes over time (HR, especially on runs with strides?)

Also - how to deal with data over time that could work momentarily? If I know lowest HR and highest HR, it could be mapped to a general purpose filter that opens and screams when the HR gets high...

This bit is proper thinky. How much can you manipulate this before it's not from the data any more? God damn it data sonification is a philisophical nightmare





## TODO

Big fucking todo is check if these todos still make sense

- Pull the data to visualize it
- Create parallels (one raw, one quantized, one smoothed)
- Timeline it (?!? how tho)
- Package it to be fed into Ableton
- labelling. Lots of labelling
 
