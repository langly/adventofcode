#!/usr/bin/env python3

program = []

with open("input.txt") as fh:
    for line in fh:
        line = line.strip()

        op = line.split()

        program.append( [0] + op )

pc  = 0
acc = 0
done = 0

while not done:
    visited, op, imm = program[pc]

    if visited == 1:
        done = 1
        print(acc)
        break


    program[pc][0] = 1

    if op == "jmp":
        pc = pc + int(imm)
        continue
    elif op  == "acc":
        acc = acc + int(imm)

    pc = pc + 1
