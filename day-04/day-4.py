# @author: Ezedin Fedlu
# @date: 2022-12-03
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 4

import sys
from pathlib import Path
from typing import List, Tuple

def parse_input(input_file: Path) -> List[Tuple[Tuple[int, int], Tuple[int, int]]]:
    with open(input_file, 'r') as f:
        return [tuple(map(parse_range, line.split(','))) for line in f]

def parse_range(range_str: str) -> Tuple[int, int]:
    return tuple(map(int, range_str.split('-')))

def is_range_contained(range1: Tuple[int, int], range2: Tuple[int, int]) -> bool:
    return range1[0] >= range2[0] and range1[1] <= range2[1]

def part_1(ranges):
    return sum(is_range_contained(r1, r2) or is_range_contained(r2, r1) for r1, r2 in ranges)

def is_overlap(range1: Tuple[int, int], range2: Tuple[int, int]) -> bool:
    return range1[0] <= range2[1] and range1[1] >= range2[0]

def part_2(ranges):
    return sum(is_overlap(r1, r2) for r1, r2 in ranges)    

def main():
    input_file = Path(sys.argv[1])
    ranges = parse_input(input_file)
    print(f'Part 1: {part_1(ranges)}')
    print(f'Part 2: {part_2(ranges)}')



if __name__ == '__main__':
    main()