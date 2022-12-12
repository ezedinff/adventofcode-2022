# @author: Ezedin Fedlu
# @date: 2021-12-01
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 1
import sys
from pathlib import Path
from typing import List, Tuple

def parse_input(input_file: Path) -> List[List[int]]:
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
    elves = []
    elf = []
    for line in lines:
        if line == '':
            elves.append(elf)
            elf = []
        else:
            try:
                elf.append(int(line))
            except ValueError:
                continue
    elves.append(elf)
    return elves

def find_largest_elf(elves: List[List[int]]) -> int:
    total_elves_calories = []
    for elf in elves:
        total_elves_calories.append(sum(elf))
    return max(total_elves_calories)


def find_top_three_elves(elves: List[List[int]]) -> int:
    total_elves_calories = []
    for elf in elves:
        total_elves_calories.append(sum(elf))
    total_elves_calories.sort(reverse=True)
    return sum(total_elves_calories[:3])

def part_1(elves: List[List[int]]) -> int:
    return find_largest_elf(elves)

def part_2(elves: List[List[int]]) -> int:
    return find_top_three_elves(elves)

def main():
    input_file = sys.argv[1]
    elves = parse_input(input_file)
    print(f'Part 1: {part_1(elves)}')
    print(f'Part 2: {part_2(elves)}')

if __name__ == '__main__':
    main()