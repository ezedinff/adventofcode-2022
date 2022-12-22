#!/usr/bin/python3
import sys
import re
from collections import deque


def parse_input(file_path):
    with open(file_path) as f:
        return { int(numbers[0]): tuple(int(n) for n in numbers[1:]) for line in f for numbers in [re.findall(r'\d+', line)]}


def get_max_geodes(blueprints, duration, is_part2=False):
    max_geodes = 0 if not is_part2 else 1
    for index, blueprint in enumerate(blueprints):
        ore_cost, clay_cost, obsidian_cost_ore, obsidian_cost_clay, geodes_cost_ore, geodes_cost_obsidian = blueprints[
            blueprint]
        best = 0
        state = (0, 0, 0, 0, 1, 0, 0, 0, duration)
        queue = deque([state])
        seen = set()
        while queue:
            o, c, ob, g, r1, r2, r3, r4, t = queue.popleft()
            best = max(best, g)
            if t == 0:
                continue

            core = max(
                [ore_cost, clay_cost, obsidian_cost_ore, geodes_cost_ore])
            r1, r2, r3 = min(r1, core), min(
                r2, obsidian_cost_clay), min(r3, geodes_cost_obsidian)
            o, c, ob = min(o, t * core - r1 * (t - 1)), min(c, t * obsidian_cost_clay -
                                                            r2 * (t - 1)), min(ob, t * geodes_cost_obsidian - r3 * (t - 1))
            state = (o, c, ob, g, r1, r2, r3, r4, t)

            if state in seen:
                continue
            seen.add(state)

            queue.append((o + r1, c + r2, ob + r3, g +
                         r4, r1, r2, r3, r4, t - 1))
            if o >= ore_cost:
                queue.append((o - ore_cost + r1, c + r2, ob + r3,
                             g + r4, r1 + 1, r2, r3, r4, t - 1))
            if o >= clay_cost:
                queue.append((o - clay_cost + r1, c + r2, ob + r3,
                             g + r4, r1, r2 + 1, r3, r4, t - 1))
            if o >= obsidian_cost_ore and c >= obsidian_cost_clay:
                queue.append((o - obsidian_cost_ore + r1, c - obsidian_cost_clay +
                             r2, ob + r3, g + r4, r1, r2, r3 + 1, r4, t - 1))
            if o >= geodes_cost_ore and ob >= geodes_cost_obsidian:
                queue.append((o - geodes_cost_ore + r1, c + r2, ob -
                             geodes_cost_obsidian + r3, g + r4, r1, r2, r3, r4 + 1, t - 1))

        if is_part2:
            if index < 3:
                max_geodes *= best
            else:
                break
        else:
            max_geodes += (blueprint * best)

    return max_geodes


def main():
    blueprints = parse_input(sys.argv[1])
    print(f"Part 1: {get_max_geodes(blueprints, 24)}")
    print(f"Part 2: {get_max_geodes(blueprints, 32, True)}")


if __name__ == '__main__':
    main()
