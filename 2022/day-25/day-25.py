# @author: Ezedin Fedlu
# @date: 2022-12-25
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 25

import sys

VALUES = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}
MODULS = {0: '0', 1:'1', 2:'2', 3: '=', 4: '-'}

def parse_input(filename):
    with open(filename) as f:
        return f.read().splitlines()

def from_snauf(s):
    value = 0
    for i in s:
        value = 5*value + VALUES[i]
    return value

def to_snauf(n):
    if n == 0:
        return ''
    v = MODULS[n % 5]
    n -= VALUES[v]
    return to_snauf(n//5) + v

def main():
    lines = parse_input(sys.argv[1])
    total = 0
    for line in lines:
        total += from_snauf(line)
    print(f"part 1: {to_snauf(total)}")

if __name__ == '__main__':
    main()