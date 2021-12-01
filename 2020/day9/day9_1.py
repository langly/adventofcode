#!/usr/bin/env python3

window = []

##
# This is the number we will find: 22406676
##

magic_number = 22406676


def check_stuff(n):
    assert len(window) == 25

    for val in window:
        i = n-val

        if i in window:
            return True

    return False

def getLine(fh):
    return int(fh.readline().strip())


with open("input.txt") as fh:
    window.append(getLine(fh))
    window.append(getLine(fh))

    while True:
        total = sum(window)

        if ( total > magic_number ):
            window = window[1:]
        elif ( total < magic_number ):
            window.append(getLine(fh))
        else:
            print(min(window) + max(window))
            break

