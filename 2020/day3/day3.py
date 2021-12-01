#!/usr/bin/env python3
inputs = []

with open("input.txt") as fh:
    for line in fh:
        l = line.strip()
        inputs.append( l )

matches = 0
offset  = 0

for line in inputs:
    line = line.strip()

    if line[offset] == '#':
        matches = matches + 1

    offset = (offset + 3) % len(line)


print("Matches: " , matches)
