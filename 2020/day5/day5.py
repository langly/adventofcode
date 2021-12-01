#!/usr/bin/env python3


def convertBinary(line, ch):
    line = "".join((list(map( lambda x: '1' if x == ch else '0', line))))

    return int(line,2)


with open("input.txt") as fh:
    val = 0

    for line in fh:
        line = line.strip()

        row = convertBinary(line[:-3], 'B')
        col = convertBinary(line[-3:], 'R')

        seat_id = (row * 8 ) + col

        if seat_id > val:
            val = seat_id

    print(val)
