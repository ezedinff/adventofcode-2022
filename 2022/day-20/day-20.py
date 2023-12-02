# @author: Ezedin Fedlu
# @date: 2022-12-20
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 20

import sys

def parse_input(file_path):
    with open(file_path) as f:
        return list(map(int, f.read().splitlines()))

def solve(lines, repeat):
    nums = list(enumerate(lines))
    new = nums[:]
    for _ in range(repeat):
        for p in nums:
            i = new.index(p)
            new.remove(p)
            target = (i + p[1]) % len(new)
            new.insert(target, p)
    zero = [n for _, n in new].index(0)
    return sum(new[(zero + i) % len(new)][1] for i in (1000, 2000, 3000))


def main():
    lines = parse_input(sys.argv[1])
    print("Part 1:", solve(lines, 1))
    print("Part 2:", solve(map(lambda x: x * 811589153, lines), 10))

if __name__ == "__main__":
    main()