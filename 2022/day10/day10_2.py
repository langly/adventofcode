#!/usr/bin/env python3

lines = []

def within(cycle, acc):

    pixel = (cycle - 1) %40

    return (pixel >= acc - 1) and (pixel <= acc + 1)

lines = []

with open("input.txt") as fh:
    acc = 1
    cycle = 1

    for line in fh:
        line = line.strip()

        s = line.split()

        if within(cycle, acc):
            lines.append("#")
        else:
            lines.append(".")

        cycle += 1

        ## We have an add instruction consuming two cycles
        if len(s) == 2:
            if within(cycle, acc):
                lines.append("#")
            else:
                lines.append(".")

            acc += int(s[1])
            cycle += 1

### Pretty print this stuff to be able to read
steps = 40
for l in range(0,len(lines),steps):
    f = lines[l:l+steps]
    print("".join(f))
