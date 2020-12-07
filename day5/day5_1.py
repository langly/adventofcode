#!/usr/bin/env python3


def convertBinary(line, ch):
    line = "".join((list(map( lambda x: '1' if x == ch else '0', line))))

    return int(line,2)

finds = []
for i in range(1024):
    finds.append(0)

with open("input.txt") as fh:
    val = 0

    for line in fh:
        line = line.strip()

        row = convertBinary(line[:-3], 'B')
        col = convertBinary(line[-3:], 'R')

        seat_id = (row * 8 ) + col
        finds[seat_id] = 1


for i, val in enumerate(finds):
    if val == 0:
        if ( i > 0 and i < 1024):
            if finds[i-1] and finds[i+1]:
                print(i)
