# @author: Ezedin Fedlu
# @date: 2022-12-23
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 23

import sys
from collections import deque

class GameOfElf:
    NEIGHBORS = (
        (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)
    )

    def __init__(self, elves):
        self.directions = deque(
            [
                ({0, 1, 2}, -1, 0),
                ({4, 5, 6}, 1, 0),
                ({6, 7, 0}, 0, -1),
                ({2, 3, 4}, 0, 1),
            ]
        )
        self.__step = 0
        self.elves = elves

    def empty_area(self):
        min_i, max_i = None, None
        min_j, max_j = None, None
        for i, j in self.elves:
            if min_i is None or i < min_i:
                min_i = i
            if max_i is None or i > max_i:
                max_i = i
            if min_j is None or j < min_j:
                min_j = j
            if max_j is None or j > max_j:
                max_j = j
        return (max_i - min_i + 1) * (max_j - min_j + 1) - len(self.elves)

    def elf_indices(self, i, j):
        return {
            k
            for k, (di, dj) in enumerate(GameOfElf.NEIGHBORS)
            if (i + di, j + dj) in self.elves
        }

    def step(self):
        self.__step += 1
        proposals = {}
        for i, j in self.elves:
            elf_indices = self.elf_indices(i, j)
            if not elf_indices:
                continue
            for indices, di, dj in self.directions:
                if not indices & elf_indices:
                    new_pos = (i + di, j + dj)
                    if new_pos in proposals:
                        del proposals[new_pos]
                    else:
                        proposals[new_pos] = (i, j)
                    break
        moved = False
        for next_pos, elf in proposals.items():
            self.elves.add(next_pos)
            self.elves.remove(elf)
            moved = True
        self.directions.rotate(-1)
        return moved

    def solve(self, target_step=10):
        ans1 = None
        while self.step():
            if ans1 is None and self.__step == target_step:
                ans1 = self.empty_area()
        return ans1, self.__step


def solve(data):
    elves = {
        (i, j)
        for i, line in enumerate(data)
        for j, c in enumerate(line)
        if c == "#"
    }
    return GameOfElf(elves).solve()


def main():
    with open(sys.argv[1]) as fp:
        data = fp.read().splitlines()
    part1, part2 = solve(data)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")


if __name__ == "__main__":
    main()

