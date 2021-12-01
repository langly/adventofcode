#!/usr/bin/env python3

##
#
# Basically, the approach is to convert the string to a binary number,
# and then do a pop count.
#
###

def strToInt(string):
    offset = ord('a')
    retMe = 0

    for i in string:
        val = ord(i) - offset
        retMe = retMe | ( 1<< val)

    return retMe

groups = []

with open('input.txt') as fh:
    val = ~0
    for line in fh:
        if line == '\n':
            groups.append(val)
            val = ~0
        else:
            line = line.strip()
            val = val & strToInt(line)

    groups.append(val)



l = list(map(lambda x: bin(x).count("1"), groups))
print(sum(l))
#
