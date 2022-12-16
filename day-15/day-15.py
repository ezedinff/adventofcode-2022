#!/usr/bin/python3

# @author: Ezedin Fedlu
# @date: 2022-12-15
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 15

import sys
import math
from copy import deepcopy
from collections import defaultdict, deque


def parse_input(file_path):
    with open(file_path) as f:
        return [line.strip() for line in f.readlines()]

def part_1(l):
    Y = 2000000

    c = [0 for _ in range(20000000)]

    for i in l:
        i = i.split()
        sx, sy = int(i[2][2:-1]), int(i[3][2:-1])
        bx, by = int(i[8][2:-1]), int(i[9][2:])

        if by == Y:
            c[bx] = 2

        r = abs(sx - bx) + abs(by - sy)
        w = r - abs(sy - Y)
        for i in range(-w, w + 1):
            c[sx - i] = max(c[sx - i], 1)
    
    return c.count(1)

def part_2(l):
    M = 4000000

    s = []

    for i in l:
        i = i.split()
        sx, sy = int(i[2][2:-1]), int(i[3][2:-1])
        bx, by = int(i[8][2:-1]), int(i[9][2:])

        r = abs(sx - bx) + abs(by - sy)
        s.append((sx, sy, r))

    for i in range(len(s)):
        ax, ay, ar = s[i]
        for nx in range(max(0, ax - ar - 1), min(M + 1, ax + ar + 2)):
            for side in range(1 + (-ar <= nx <= ar)):
                ny = ay + (ar + 1 - abs(nx - ax)) * (2 * side - 1)
                if ny < 0 or ny > M:
                    continue

                for b in s:
                    bx, by, br = b
                    if abs(bx - nx) + abs(by - ny) <= br:
                        break
                else:
                    return nx * 4000000 + ny

def main():
    l = parse_input(sys.argv[1])
    print(f"Part 1: {part_1(l)}")
    print(f"Part 2: {part_2(l)}")

if __name__ == "__main__":
    main()