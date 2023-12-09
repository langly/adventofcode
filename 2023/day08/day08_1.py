#!/usr/bin/env python3

import re

reMatch = re.compile("(\w+) = \((\w+), (\w+)\)")


with open("input.txt") as fh:
    lineno = 0

    graph = dict()

    root = None
    last = None

    for line in fh:
        line = line.strip()

        if lineno == 0:
            path = line


        if lineno > 1:
            match = reMatch.match(line)
            if match:
                node = match.group(1).strip()
                left = match.group(2).strip()
                right = match.group(3).strip()

                entry = {}
                entry['l'] = left
                entry['r'] = right
                entry['n'] = node

                if root == None:
                    root = node

                graph[node] = entry
                last = node

        lineno += 1

    root = 'AAA'
    last = 'ZZZ'
    print(f"Finding path from {root} to {last}")
    print(path)
    steps = 0

    curNode = graph[root]

    while(True):
        step = steps % len(path)
        left = path[step] == "L"

        #print(curNode['n'])
        if curNode['n'] == last:
            print(steps)
            break


        curNode = graph[curNode['l']] if left else graph[curNode['r']]
        steps +=1
