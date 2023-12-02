# @author: Ezedin Fedlu
# @date: 2022-12-22
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 22


import sys
import re

# right, down, left, up
directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def get_direction(position, direction):
    if position == "L":
        return (direction - 1) % 4
    if position == "R":
        return (direction + 1) % 4

def solve(grid, path, part1):
    mx, my = min(x for x, y in grid if y == 0), 0
    d = 0
    for p in path:
        if p == "L" or p == "R":
            d = get_direction(p, d)
            continue

        for _ in range(int(p)):
            dx, dy = directions[d]
            n = nx, ny = mx + dx, my + dy
            nd = d
            if n not in grid:  
                if dx < 0:
                    if part1:
                        nx = max(x for x, y in grid if y == my)
                    elif my < 50:
                        nx, ny, nd = 0, 149 - my, 0
                    elif my < 100:
                        nx, ny, nd = my - 50, 100, 1
                    elif my < 150:
                        nx, ny, nd = 50, 49 - (my - 100), 0
                    else:
                        nx, ny, nd = 50 + my - 150, 0, 1
                if dx > 0:
                    if part1:
                        nx = min(x for x, y in grid if y == my)
                    elif my < 50:
                        nx, ny, nd = 99, 149 - my, 2
                    elif my < 100:
                        nx, ny, nd = 100 + my - 50, 49, 3
                    elif my < 150:
                        nx, ny, nd = 149, 49 - (my - 100), 2
                    else:
                        nx, ny, nd = 50 + my - 150, 149, 3
                if dy < 0:
                    if part1:
                        ny = max(y for x, y in grid if x == mx)
                    elif my == 0:
                        if 50 <= mx < 100:
                            nx, ny, nd = 0, 150 + mx - 50, 0
                        elif 100 <= mx:
                            nx, ny = mx - 100, 199
                        else:
                            assert False
                    else:
                        assert my == 100
                        nx, ny, nd = 50, mx + 50, 0
                if dy > 0:
                    if part1:
                        ny = min(y for x, y in grid if x == mx)
                    elif my == 199:
                        nx, ny, nd = mx + 100, 0, 1
                    elif my == 149:
                        nx, ny, nd = 49, mx - 50 + 150, 2
                    else:
                        assert my == 49
                        nx, ny, nd = 99, mx - 100 + 50, 2
                n = nx, ny
            if grid[n] == "#":
                break
            mx, my, d = nx, ny, nd

    return (my + 1) * 1000 + 4 * (mx + 1) + d

def parse_input(file_path):
    with open(file_path) as f:
        lines = f.read().splitlines()
        path = re.findall(r"(\d+|L|R)", lines[-1])
        grid = {}
        for y, line in enumerate(lines[:-2]):
            for x, c in enumerate(line):
                if c != " ":
                    grid[(x, y)] = c
        return grid, path


def main():
    grid, path = parse_input(sys.argv[1])
    print("Part 1:", solve(grid, path, True))
    print("Part 2:", solve(grid, path, False))

if __name__ == "__main__":
    main()