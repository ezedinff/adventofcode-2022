
# @author: Ezedin Fedlu
# @date: 2022-12-12
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 12


import sys
from collections import deque

def parse_input():
    with open(sys.argv[1]) as f:
        return [line.strip() for line in f.readlines()]


def main():
    lines = parse_input()
    G = []
    for line in lines:
        G.append(line)
    R = len(G)
    C = len(G[0])

    E = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if G[r][c] == 'S':
                E[r][c] = 1
            elif G[r][c] == 'E':
                E[r][c] = 26
            else:
                E[r][c] = ord(G[r][c])-ord('a')+1

    print(f"Part 1: {bfs(1, G, E, R, C)}")
    print(f"Part 2: {bfs(2, G, E, R, C)}")


def bfs(part, G, E, R, C):
    Q = deque()
    for r in range(R):
        for c in range(C):
            if (part == 1 and G[r][c] == 'S') or (part == 2 and E[r][c] == 1):
                Q.append(((r, c), 0))

    S = set()
    while Q:
        (r, c), d = Q.popleft()
        if (r, c) in S:
            continue
        S.add((r, c))
        if G[r][c] == 'E':
            return d
        for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            rr = r+dr
            cc = c+dc
            if 0 <= rr < R and 0 <= cc < C and E[rr][cc] <= 1+E[r][c]:
                Q.append(((rr, cc), d+1))


if __name__ == '__main__':
    main()
