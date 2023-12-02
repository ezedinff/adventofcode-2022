# @author: Ezedin Fedlu
# @date: 2021-12-03
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 3
import sys
from pathlib import Path
from typing import List, Tuple

def parse_input(input_file: Path) -> List[List[str]]:
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()
    return lines

def get_rucksacks_part_1(lines: List[str]) -> List[Tuple[str, str]]:
    rucksacks = []
    for line in lines:
        rucksacks.append([line[:len(line)//2], line[len(line)//2:]])
    return rucksacks    

def part_1(rucksacks: List[List[str]]) -> int:
    total = 0
    for rucksack in rucksacks:
        for item in rucksack[0]:
            if item in rucksack[1]:
                total += ord(item) - 96 if item.islower() else ord(item) - 38
                break
    return total

def get_rucksacks_part_2(lines: List[str]) -> List[List[str]]:
    rucksacks = []
    for i in range(0, len(lines), 3):
        rucksacks.append([lines[i], lines[i+1], lines[i+2]])
    return rucksacks

def part_2(rucksacks: List[List[str]]) -> int:
    total = 0
    for rucksack in rucksacks:
        for item in rucksack[0]:
            if item in rucksack[1] and item in rucksack[2]:
                total += ord(item) - 96 if item.islower() else ord(item) - 38
                break
    return total

def main():
    input_file = Path(sys.argv[1])
    rucksacks_part_1 = get_rucksacks_part_1(parse_input(input_file))
    rucksacks_part_2 = get_rucksacks_part_2(parse_input(input_file))
    print(f'Part 1: {part_1(rucksacks_part_1)}')
    print(f'Part 2: {part_2(rucksacks_part_2)}')

if __name__ == '__main__':
    main()
