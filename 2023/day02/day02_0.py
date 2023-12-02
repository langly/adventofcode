#!/usr/bin/env python3

import re

reLine = re.compile("Game (\d+):(.*)")

def is_legal_game(r):
    r = r.strip()
    vals = [x.strip() for x in r.split(',')]

    for v in vals:
        v= v.strip()
        (amt,col) = v.split()
        amt = int(amt)

        if (col == "red") and (amt > 12):
            return False
        if (col == "green") and (amt > 13):
            return False
        if (col == "blue") and (amt > 14):
            return False

    return True

with open("input.txt") as fh:
    sum =0

    for line in fh:
        line = line.strip()
        m = reLine.match(line)

        if m:
            game = int(m.group(1))
            rest = m.group(2).split(";")
            valid = True
            for r in rest:
                r = r.strip()
                if not is_legal_game(r):
                    valid = False

            if valid:
                sum += game
    print(sum)



