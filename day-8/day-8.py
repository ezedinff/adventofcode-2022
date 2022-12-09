# @author: Ezedin Fedlu
# @date: 2022-12-08
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 8

import sys
from pathlib import Path
from typing import List

def parse_input(filename: str) -> List[List[int]]:
    with open(filename) as f:
        return [list(map(int, line)) for line in f.read().splitlines()]

def part_1(grid: List[List[int]]) -> int:
    visible_trees = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if is_visible(grid, c, r):
                visible_trees += 1
    return visible_trees

def is_visible(grid: List[List[int]], c: int, r: int) -> bool:
    k = grid[r][c]
    return all(grid[r][x] < k for x in range(c)) or \
            all(grid[r][x] < k for x in range(c + 1, len(grid[r]))) or \
            all(grid[x][c] < k for x in range(r)) or \
            all(grid[x][c] < k for x in range(r + 1, len(grid)))

def part_2(grid: List[List[int]]) -> int:
    t = 0
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            k = grid[r][c]
            L = R = U = D = 0
            for x in range(c - 1, -1, -1):
                L += 1
                if grid[r][x] >= k:
                    break
            for x in range(c + 1, len(grid[r])):
                R += 1
                if grid[r][x] >= k:
                    break
            for x in range(r - 1, -1, -1):
                U += 1
                if grid[x][c] >= k:
                    break
            for x in range(r + 1, len(grid)):
                D += 1
                if grid[x][c] >= k:
                    break
            t = max(t, U * D * L * R)
    return t

def main():
    grid = parse_input(sys.argv[1])
    print(f"Part 1: {part_1(grid)}")
    print(f"Part 2: {part_2(grid)}")

if __name__ == '__main__':
    main()