#!/usr/bin/env python3
inputs = []

with open("input.txt") as fh:
    for line in fh:
        l = line.strip()
        inputs.append( l )

checks = [ (1,1), (3,1), (5,1), (7,1), (1,2) ]
offsets = []
matches = []

for c in range(len(checks)):
    offsets.append(0)
    matches.append(0)


for (num,line) in enumerate(inputs):
    line = line.strip()

    for i,(skip,skipline) in enumerate(checks):
        if ( num % skipline == 0 ):
            offset = offsets[i]

            if line[offset] == '#':
                matches[i] = matches[i] + 1

            offset = (offset + skip) % len(line)
            offsets[i] = offset


print("Matches: " , matches)

from functools import reduce
product = reduce(lambda x, y : x*y, matches)
print("Product: " , product )
