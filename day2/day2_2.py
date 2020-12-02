#!/usr/bin/env python3
inputs = []

with open("input.txt") as fh:
    for line in fh:
        l = line.strip()
        inputs.append( l )

matches = 0

for line in inputs:
    (rule,password) = line.split(":")

    (occ, char) = rule.strip().split(" ")
    (lower, upper) = occ.split("-")
    password = password.strip()

    a = password[int(lower)-1] == char
    b = password[int(upper)-1] == char

    if a ^ b:
        matches = matches + 1


print("Matches: " , matches)
