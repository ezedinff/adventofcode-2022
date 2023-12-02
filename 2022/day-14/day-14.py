#!/usr/bin/python3

# @author: Ezedin Fedlu
# @date: 2022-12-14
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 14

import sys

def read_input(file_name):
    data = open(file_name).read().strip()
    lines = [x for x in data.split('\n')]
    return lines

def create_set_of_points(lines):
    R = set()
    for line in lines:
        prev = None
        for point in line.split('->'):
            x,y = point.split(',')
            x,y = int(x),int(y)
            if prev is not None:
                dx = x-prev[0]
                dy = y-prev[1]
                len_ = max(abs(dx),abs(dy))
                for i in range(len_+1):
                    xx = prev[0]+i*(1 if dx>0 else (-1 if dx<0 else 0))
                    yy = prev[1]+i*(1 if dy>0 else (-1 if dy<0 else 0))
                    R.add((xx,yy))
            prev = (x,y)
    return R

def extend_set_of_points(R, floor):
    lo_x = min(r[0] for r in R)-1000
    hi_x = max(r[0] for r in R)+1000
    for x in range(lo_x, hi_x):
        R.add((x,floor))
    return R

def solve(R, floor):
    did_p1 = False
    for t in range(1000000):
        rock = (500,0)
        while True:
            if rock[1]+1>=floor and (not did_p1):
                did_p1 = True
                print(f"Part 1: {t}")
            if (rock[0],rock[1]+1) not in R:
                rock = (rock[0],rock[1]+1)
            elif (rock[0]-1,rock[1]+1) not in R:
                rock = (rock[0]-1, rock[1]+1)
            elif (rock[0]+1, rock[1]+1) not in R:
                rock = (rock[0]+1, rock[1]+1)
            else:
                break
        if rock == (500,0):
            print(f"Part 2: {t+1}")
            break
        R.add(rock)

if __name__ == '__main__':
    lines = read_input(sys.argv[1])
    R = create_set_of_points(lines)
    floor = 2+max(r[1] for r in R)
    R = extend_set_of_points(R, floor)
    solve(R, floor)