#!/usr/bin/env python3

import re

reLine = re.compile("Game (\d+):(.*)")

def is_legal_game(r):
    r = r.strip()
    vals = [x.strip() for x in r.split(',')]

    r = g = b= 0

    for v in vals:
        v= v.strip()
        (amt,col) = v.split()
        amt = int(amt)

        if (col == "red"):
            r = amt
        if (col == "green"):
            g = amt
        if (col == "blue"):
            b = amt

    return (r,g,b)

from functools import reduce

with open("input.txt") as fh:
    sum =0

    for line in fh:
        line = line.strip()
        m = reLine.match(line)

        if m:
            game = int(m.group(1))
            rest = m.group(2).split(";")
            valid = True

            found = (0,0,0)

            for game in rest:
                game = game.strip()
                l = is_legal_game(game)
                f = list(zip(found,l))
                found = [ max(x) for x in f ]

            part = reduce(lambda x,y: x*y, found)
            sum += part

    print(sum)



