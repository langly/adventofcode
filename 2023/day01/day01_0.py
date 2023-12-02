#!/usr/bin/env python3

with open("input.txt") as fh:
    l = []
    for line in fh:
        line = line.strip()

        numbers = [ x for x in line if x.isdigit() ]
        x = int(numbers[0])*10 + int(numbers[-1])
        l.append(x)


print(sum(l))
