
# @author: Ezedin Fedlu
# @date: 2022-12-10
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 10


import sys

def part1():
    x = 1

    o = []

    with open(sys.argv[1]) as f:
        for line in f:
            if line == "noop\n":
                o.append(x)
            else:
                l = line.split()
                if len(l) == 2:
                    v = int(line.split()[1])
                    o.append(x)
                    o.append(x)
                    x += v

    return sum(x * y + y for x, y in list(enumerate(o))[19::40])

def part2():
    x = 1
    o = []
    for line in open(sys.argv[1]):
        if line == "noop\n":
            o.append(x)
        else:
            if len(line.split()) == 2:
                v = int(line.split()[1])
                o.append(x)
                o.append(x)
                x += v

    for i in range(0, len(o), 40):
        for j in range(40):
            if i + j < len(o):
                print(end = "##" if abs(o[i + j] - j) <= 1 else "  ")
        print()

if __name__ == "__main__":
    #part1()
    part2()