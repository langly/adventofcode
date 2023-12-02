#!/usr/bin/env python3

rep = [
    ("one", 1),
    ("two", 2),
    ("three", 3),
    ("four", 4),
    ("five", 5),
    ("six", 6),
    ("seven", 7),
    ("eight", 8),
    ("nine", 9),
]

def sub(inp):
    ## A bit strange this one. Doing it this way to handle the case of e.g.
    # eightwo being both eight and two.
    x = inp

    num = []

    for s in range(len(inp)):
        sub = inp[s:]
        if inp[s].isdigit():
            num.append(inp[s])
        for (k,v) in rep:
            if sub.startswith(k):
                num.append(v)
                continue

    return num


with open("input.txt") as fh:
    l = []
    for line in fh:
        line = line.strip()
        numbers = sub(line)

        x = int(numbers[0])*10 + int(numbers[-1])
        l.append(x)


print(sum(l))
