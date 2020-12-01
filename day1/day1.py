#!/usr/bin/env python3

inputs = []

with open("input.txt") as fh:
    for line in fh:
        l = line.strip()
        inputs.append( int(l) )

for i in range(len(inputs)):
    ori = inputs[i]
    for y in range(i+1, len(inputs)):
        s = inputs[y]

        if ( s + ori == 2020 ):
            print(s, ori)
            print(s*ori)
