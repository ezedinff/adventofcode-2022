# @author: Ezedin Fedlu
# @date: 2022-12-05
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 5

import sys
from pathlib import Path
from typing import List

def parse_crates(f) -> List[List[str]]:
    lines = []
    while '1' not in (line := f.readline()):
        lines.append(line)
    n = int(line.strip().split()[-1])
    crates = [[] for _ in range(n)]
    while lines:
        line = lines.pop()
        for i in range(n):
            p = 1 + 4*i
            if p < len(line) and line[p] != ' ':
                crates[i].append(line[p])
    return crates


def parse_program(f) -> List[List[int]]:
    program = []
    while line := f.readline():
        _, k, _, fm, _, to = line.strip().split()
        program.append((int(k), int(fm), int(to)))
    return program


def part_1(crates, program) -> str:
    crates = [crate[:] for crate in crates]
    for k, fm, to in program:
        [crates[to - 1].append(crates[fm - 1].pop()) for _ in range(k)]
    return ''.join(crate[-1] for crate in crates)


def part_2(crates, program) -> str:
    crates = [crate[:] for crate in crates]
    for k, fm, to in program:
        tmp = [crates[fm-1].pop() for _ in range(k)]
        [crates[to-1].append(tmp.pop()) for _ in range(k)]
    return ''.join(crate[-1] for crate in crates)


def main():
    file_path = Path(sys.argv[1])
    with open(file_path, 'r') as f:
        crates = parse_crates(f)
        if line := f.readline().strip() != '':
            print('bad input')  # empty line
        program = parse_program(f)
        print(part_1(crates, program))
        print(part_2(crates, program))


if __name__ == '__main__':
    main()

