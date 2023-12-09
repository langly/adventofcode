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

    start_nodes = [ x for x in graph.keys() if x[2] == 'A' ]

    print(start_nodes)
    totals = []

    for n in start_nodes:
        steps = 0
        curNode = graph[n]

        while(True):
            step = steps % len(path)
            left = path[step] == "L"

            if curNode['n'][2] == 'Z':# == last:
                print(steps)
                totals.append(steps)
                break


            curNode = graph[curNode['l']] if left else graph[curNode['r']]
            steps +=1

    from math import lcm
    p = lcm(*totals)
    print(p)
