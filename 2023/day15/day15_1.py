#!/usr/bin/env python3

with open("input.txt") as fh:
    sum = 0

    for line in fh:
        line = line.strip()
        init = line.split(",")

        for s in init:
            current_value = 0
            for c in s:
                val = ord(c)
                current_value += val
                current_value *= 17
                current_value = current_value % 256
            print(s,current_value)
            sum += current_value


    print(sum)
