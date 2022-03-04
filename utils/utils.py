#takes any value and returns a valid midi value
def map2midi(val, minval, maxval):
    newval = 0
    valrange = maxval - minval
    if (valrange == 0):
        return 0
    else:
        newval = int(((val - minval)*127)/valrange)
        if (newval
# handle erronous values if less than 0 or more than 127 before return

    return newval


