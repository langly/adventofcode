#!/usr/bin/env python3
inputs = []

with open("input.txt") as fh:
    for line in fh:
        l = line.strip()
        inputs.append( l )

def countChar(string,char):
    i = 0
    for c in string:
        if c == char:
            i = i + 1

    return i

matches = 0

for line in inputs:
    (rule,password) = line.split(":")

    (occ, char) = rule.strip().split(" ")
    (lower, upper) = occ.split("-")

    c = countChar(password, char)

    if c <= int(upper) and c >= int(lower):
        print(line)
        matches = matches + 1


print("Matches: " , matches)
