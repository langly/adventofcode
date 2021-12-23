#!/usr/bin/env python3


opens = ["(", "[", "{", "<"]
close = [")", "]", "}", ">"]

points = [3, 57, 1197, 25137]

s = 0

def stackme(line):
    global s
    stack = []

    for c in line:
        if c in opens:
            stack.append(c)
        elif c in close:
            o = stack.pop()

            oIdx = opens.index(o)
            cIdx = close.index(c)

            if not cIdx == oIdx:
                s += points[cIdx]
                return

with open("input.txt") as fh:
    for line in fh:
        line = line.strip()

        stackme(line)

print(s)
