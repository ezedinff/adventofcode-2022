# @author: Ezedin Fedlu
# @date: 2022-12-07
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 7

import sys
import re

def parse_file(lines):
    cwd = root = {}
    stack = []
    for line in lines:
        line = line.strip()
        if line[0] == "$":
            if line[2] == "c":
                directory = line[5:]
                if directory == "/":
                    cwd = root
                    stack = []
                elif directory == "..":
                    cwd = stack.pop()
                else:
                    if directory not in cwd:
                        cwd[directory] = {}
                    stack.append(cwd)
                    cwd = cwd[directory]
        else:
            x, y = line.split()
            if x == "dir":
                if y not in cwd:
                    cwd[y] = {}
            else:
                cwd[y] = int(x)
    return root

def size(directory):
    if type(directory) == int:
        return directory
    return sum(map(size, directory.values()))

def part_1(directory):
    if type(directory) == int:
        return (directory, 0)
    size = 0
    ans = 0
    for child in directory.values():
        s, a = part_1(child)
        size += s
        ans += a
    if size <= 100000:
        ans += size
    return (size, ans)

def part_2(directory, t):
    ans = float("inf")
    if size(directory) >= t:
        ans = size(directory)
    for child in directory.values():
        if type(child) == int:
            continue
        q = part_2(child, t)
        ans = min(ans, q)
    return ans

def main():
    root = parse_file(open(sys.argv[1], "r"))
    print(f"Part 1: {part_1(root)[1]}")
    print(f"Part 2: {part_2(root, size(root) - 40_000_000)}")

if __name__ == "__main__":
    main()

    


