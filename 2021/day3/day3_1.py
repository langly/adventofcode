#!/usr/bin/env python3

mVal = "101000111100"

def findRating(lst, maks, pos):
    if len(lst) == 1:
        return lst[0]

    split = len(mVal)

    p = split - pos -1

    for idx in range(len(lst)-1):
        this = lst[idx]
        nxt = lst[idx+1]

        if not (this >> p)&1 == (nxt>>p)&1:
            lower = lst[:idx+1]
            upper = lst[idx+1:]

            lLower = len(lower)
            lUpper = len(upper)

            if ( maks ):
                mux = lower if lLower > lUpper else upper
            else:
                mux = lower if lLower <= lUpper else upper

            return findRating(mux, maks, pos +1)

    return findRating(lst, maks, pos +1)

with open("input.txt") as fh:

    fnord = fh.readlines()
    mask = (2**len(mVal))-1
    fnord = list(map(lambda x: int(x.strip() ,2)& mask, fnord))
    fnord.sort()

    f = findRating(fnord,True,0)
    o = findRating(fnord,False,0)

    print("rating:", f)
    print("rating:", o)

    print(f*o)
