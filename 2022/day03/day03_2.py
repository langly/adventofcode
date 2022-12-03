#!/usr/bin/env python3

def find(arr):
    l = set(filter(lambda x: x in arr[1] and x in arr[2], arr[0]))
    assert(len(l) == 1)

    return ord(list(l)[0])

with open("input.txt") as fh: 
    s = 0
    col = []

    for line in fh: 
        line = line.strip()

        col.append(line)

        ## Every third one, fetch the variable.
        if len(col) == 3:
            i = find(col)
            bias = i & 32       ## Fetch the upper case bit
            val  = i & (32-1)   ## Fetch the value 

            s += val + (26 if bias == 0 else 0)
            col = []


    print(s)
