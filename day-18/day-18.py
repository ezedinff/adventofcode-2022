# @author: Ezedin Fedlu
# @date: 2022-12-18
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 18

import sys
import re

def parse_input(file_path):
    with open(file_path) as f:
        return set(tuple(int(i) for i in re.findall(r'-?\d+', line)) for line in f.read().strip().split('\n'))

def free_neighbors(point, drops):
    for i in range(3):
        for d in (-1, 1):
            p = list(point)
            p[i] += d
            p = tuple(p)
            if p not in drops:
                yield p, i


def floodfill(cc, mins, maxs, drops, pockets, outside):
    todo = [cc]
    connected = set()
    while todo:
        c = todo.pop()
        for n, i in free_neighbors(c, drops):
            if n[i] < mins[i] or n[i] > maxs[i]:
                outside.update(connected)
                return True
            if n not in connected:
                connected.add(n)
                todo.append(n)
    pockets.update(connected)
    return False

def part1(drops):
    return sum(sum(1 for n, _ in free_neighbors(c, drops)) for c in drops)

def part2(drops):
    mins = [min(c[i] for c in drops) for i in range(3)]
    maxs = [max(c[i] for c in drops) for i in range(3)]
    pockets, outside = set(), set()
    part2 = 0
    for c in drops:
        for n, _ in free_neighbors(c, drops):
            if n not in pockets and (n in outside or floodfill(n, mins, maxs, drops, pockets, outside)):
                part2 += 1
    return part2

def main():
    drops = parse_input(sys.argv[1])
    print("Part 1:", part1(drops))
    print("Part 2:", part2(drops))


import unittest

class Test(unittest.TestCase):
    def setUp(self):
        self.drops = parse_input("inputs/day-18.txt")
    def test_part1(self):
        self.assertEqual(part1(self.drops), 4310)

    def test_part2(self):
        self.assertEqual(part2(self.drops), 2466)

if __name__ == '__main__':
    unittest.main(argv=["first-arg-is-ignored"], exit=False)