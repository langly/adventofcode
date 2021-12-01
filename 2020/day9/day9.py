#!/usr/bin/env python3

window = []

def check_stuff(n):
    assert len(window) == 25

    for val in window:
        i = n-val

        if i in window:
            return True

    return False


with open("input.txt") as fh:
    for line_num,line in enumerate(fh):
        line = line.strip()
        number = int(line)

        if int(line_num) >= 25:
            if not check_stuff(number):
                print(number)
                break
            window = window[1:]

        window.append(number)


