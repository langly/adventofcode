#!/usr/bin/env python3

ids = []

found = 0

def intRange(least,maximum, val,lencheck):
    try:
        if not len(val) == 4 and (lencheck ==1):
            return 0

        val = int(val)
        a = (val <= maximum) and (val >= least)
        return a

    except:
        return 0 ## We are not a valid integer

def heightRange(height):
    if height.endswith("cm"):
        return intRange(150, 193, height[:-2],0)
    elif height.endswith("in"):
        return intRange(59, 76, height[:-2],0)
    else:
        return 0


def validate(curDict):
    req = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    print(curDict)

    for r in req:
        if not r in curDict:
            return 0

        val = curDict[r]

        ## The checks here.
        if (r == "byr") and (not intRange(1920, 2002, val,1)):
            return 0
        if (r == "iyr") and (not intRange(2010, 2020, val,1)):
            return 0
        if (r == "eyr") and (not intRange(2020, 2030, val,1)):
            return 0
        if (r == "hgt") and (not heightRange(val)):
            return 0
        if (r == "hcl"):
            print(val)
            try:
                val.startswith("#")
                int(val[1:],16)
                if not len(val) == 7:
                    return 0
            except:
                return 0
        if (r == "ecl"):
            if not val in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"):
                return 0

        if r == "pid":
            try:
                int(val)
                if not len(val) == 9:
                    return 0
            except:
                return 0

    return 1

#with open("input_test.txt") as fh:
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
