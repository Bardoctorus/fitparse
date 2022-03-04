from fitparse import FitFile
import math
import time
import rtmidi
from utils import utils


midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

for i in available_ports:
    print(i)
if available_ports:
    print("opening port 1 which should be loop midi")
    midiout.open_port(1)
    

enhanced_speed_list = list()
power_list = list()
counter = 0
fitfile = FitFile('441657585374887937.fit')
# Get all data messages that are of type record
for record in fitfile.get_messages('record'):

    # Go through all the data entries in this record
    for record_data in record:
        # activity type isn't relevant i.e run/ride
        if record_data.name == "activity_type":
            continue

#        if record_data.name == "accumulated_power":
#            print('accumulated power/1000: {}, Sine = {}'.format(record_data.value/1000,math.sin(record_data.value/1000)))

        if record_data.name == "enhanced_speed":
            if(record_data.value == None):
                continue
            else:
                enhanced_speed_list.append(record_data.value)

        if record_data.name == "power":
            if(record_data.value == None):
                continue
            else:
                power_list.append(record_data.value)
            

        # Print the records name and value (and units if it has any)
#        if record_data.units:
#            print("yep")
#            print(" * %s: %s %s" % (record_data.name, record_data.value, record_data.units,))
#                record_data.name, record_data.value, record_data.units,
#            ))
#        else:
 #           print(" * %s: %s" % (record_data.name, record_data.value)) 
    #print()

print(max(enhanced_speed_list))
print(min(enhanced_speed_list))

g = 0
maxg = len(enhanced_speed_list)
with midiout:
    while True:
        #every second do thing
        if (counter == 50):
            
            speedmidi = utils.map2midi(enhanced_speed_list[g],min(enhanced_speed_list),max(enhanced_speed_list))
            powermidi = utils.map2midi(power_list[g],min(power_list),max(power_list))
            print("100 reached") 
            note_on =[0x90,speedmidi,powermidi]
            midiout.send_message(note_on)
    
        if  (counter == 70):
            note_off =[0x80,speedmidi,0]
            midiout.send_message(note_off)
            counter = 0
            print("reset counter")
        time.sleep(0.01)
        counter+=1
        g+=1
        if(g > maxg):
            g = 0