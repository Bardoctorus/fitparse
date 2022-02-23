from fitparse import FitFile


outputFile = open("out.txt", "a")

fitfile = FitFile('441657585374887937.fit')
counter =0
# Get all data messages that are of type record
for record in fitfile.get_messages('record'):

    # Go through all the data entries in this record
    for record_data in record:
        if record_data.name == "activity_type":
            continue





        # Print the records name and value (and units if it has any)
        if record_data.units:
#            print(" * %s: %s %s" % (record_data.name, record_data.value, record_data.units,))
            outputFile.write(" * %s: %s %s\n" % (
                record_data.name, record_data.value, record_data.units,
            ))
        else:
 #           print(" * %s: %s" % (record_data.name, record_data.value)) 
            outputFile.write(" * %s: %s\n" % (record_data.name, record_data.value))
    #print()

    outputFile.write("\n")
    counter+=1
print(counter)


outputFile.close()

