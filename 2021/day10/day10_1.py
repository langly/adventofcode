#!/usr/bin/env python3


opens = ["(", "[", "{", "<"]
close = [")", "]", "}", ">"]

points = [3, 57, 1197, 25137]

s = 0
complete = []

def stackme(line):
    global s
    global complete
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

    stack.reverse()
    total = 0
    for c in stack:
        total = (5*total) + opens.index(c) + 1

    complete.append(total)

with open("input.txt") as fh:
    for line in fh:
        line = line.strip()

        stackme(line)

print(s)
complete.sort()
l = len(complete)
print(complete[int(l/2)])
