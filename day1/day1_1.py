#!/usr/bin/env python3

inputs = []

with open("input.txt") as fh:
    for line in fh:
        l = line.strip()
        inputs.append( int(l) )

for x in range(len(inputs)):
    for y in range(x+1, len(inputs)):
        for z in range(y+1, len(inputs)):
            iX = inputs[x]
            iY = inputs[y]
            iZ = inputs[z]

            if sum((iX,iY,iZ)) == 2020:
                print(iX, iY, iZ)
                print(iX * iY * iZ)

