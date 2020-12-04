#!/usr/bin/env python3

ids = []

found = 0

def validate(curDict):
    req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for r in req:
        if not r in curDict:
            return 0

    return 1

with open("input.txt") as fh:
    curDict = {}
    for line in fh:
        if line == '\n':
            ids.append(curDict)

            valid = validate(curDict)
            found = found + valid

            curDict = {}
        else:
            s = list(map(lambda x: x.strip(),line.split(" ")))
            for e in s:
                (key,value) = e.split(":")
                curDict[key] = value

    ## We need the last line.
    found = found + validate(curDict)

print(found)
