# @author: Ezedin Fedlu
# @date: 2022-12-16
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 16

import sys
import re
from collections import defaultdict

def parse_input(file_path):
    valves = {}
    with open(file_path) as f:
        for line in f:
            groups = re.match(r'Valve (\w+) has flow rate=(\d+); tunnels lead to valves (.*)', line)
            if not groups:
                groups = re.match(r'Valve (\w+) has flow rate=(\d+); tunnel leads to valve (.*)', line)
            name, flow, children = groups.groups()
            valves[name] = {
                'flow': int(flow),
                'tunnels': children.split(', '),
                'paths': {}
            }
    return valves

def bfs(valves, frontier, end):
    depth = 1
    while True:
        next_frontier = set()
        for x in frontier:
            if x == end:
                return depth
            if x not in valves.keys():
                continue
            for y in valves[x]['tunnels']:
                next_frontier.add(y)
        frontier = next_frontier
        depth += 1


def part1(valves):
    best = 0
    def search(opened, flowed, current_room, depth_to_go):
        nonlocal best
        if flowed > best:
            best = flowed

        if depth_to_go <= 0:
            return

        if current_room not in opened:
            search(opened.union([current_room]), flowed + valves[current_room]['flow'] * depth_to_go, current_room, depth_to_go - 1)
        else:
            for k in [x for x in valves[current_room]['paths'].keys() if x not in opened]:
                search(opened, flowed, k, depth_to_go - valves[current_room]['paths'][k])

    search(set(['AA']), 0, 'AA', 29)
    return best

def part2(valves):
    best = 0
    def search(opened, flowed, current_room, depth_to_go, elephants_turn):
        nonlocal best
        if flowed > best:
            best = flowed

        if depth_to_go <= 0:
            return

        if current_room not in opened:
            search(opened.union([current_room]), flowed + valves[current_room]['flow'] * depth_to_go, current_room, depth_to_go - 1, elephants_turn)
            if not elephants_turn:
                search(set([current_room]).union(opened), flowed + valves[current_room]['flow'] * depth_to_go, 'AA', 25, True)
        else:
            for k in [x for x in valves[current_room]['paths'].keys() if x not in opened]:
                search(opened, flowed, k, depth_to_go - valves[current_room]['paths'][k], elephants_turn)

    search(set(['AA']), 0, 'AA', 25, False)
    return best

def main():
    valves = parse_input(sys.argv[1])
    keys = sorted([x for x in list(valves.keys()) if valves[x]['flow'] != 0])
    for k in keys + ['AA']:
        for k2 in keys:
            if k2 != k:
                valves[k]['paths'][k2] = bfs(valves, valves[k]['tunnels'], k2)
    print(f"Part 1: {part1(valves)}")
    print(f"Part 2: {part2(valves)}")

if __name__ == '__main__':
    main()