# @author: Ezedin Fedlu
# @date: 2022-12-13
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 13

import sys
from functools import cmp_to_key

def parse_input():
    with open(sys.argv[1]) as f:
        return [group for group in f.read().strip().split("\n\n")]


def compare(p1,p2):
    if isinstance(p1, int) and isinstance(p2,int):
        if p1 < p2:
            return -1
        elif p1 == p2:
            return 0
        else:
            return 1
    elif isinstance(p1, list) and isinstance(p2, list):
        i = 0
        while i<len(p1) and i<len(p2):
            c = compare(p1[i], p2[i])
            if c==-1:
                return -1
            if c==1:
                return 1
            i += 1
        if i==len(p1) and i<len(p2):
            return -1
        elif i==len(p2) and i<len(p1):
            return 1
        else:
            return 0
    elif isinstance(p1, int) and isinstance(p2, list):
        return compare([p1], p2)
    else:
        return compare(p1, [p2])

def part1(packets, data):
    packets = []
    ans = 0
    for i,group in enumerate(data):
        p1,p2 = group.split('\n')
        p1 = eval(p1)
        p2 = eval(p2)
        packets.append(p1)
        packets.append(p2)
        if compare(p1, p2)==-1:
            ans += 1+i
    packets.append([[2]])
    packets.append([[6]])
    return ans, packets

def part2(packets):
    packets = sorted(packets, key=cmp_to_key(lambda p1,p2: compare(p1,p2)))
    ans = 1
    for i,p in enumerate(packets):
        if p==[[2]] or p==[[6]]:
            ans *= i+1
    return ans

def main():
    data = parse_input()
    ans, packets = part1([], data)
    print(f"Part 1: {ans}")
    print(f"Part 2: {part2(packets)}")

if __name__ == "__main__":
    main()