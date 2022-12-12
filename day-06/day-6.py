# @author: Ezedin Fedlu
# @date: 2022-12-06
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 6

import sys

def part_1(content):
    marker, marker_count, marker_length, marker_found = 0, 0, 4, False
    marker_index, marker_list = 0, []
    for i in range(len(content)):
        if marker_found:
            break
        marker_list.append(content[i])
        if len(marker_list) == marker_length:
            if len(set(marker_list)) == marker_length:
                marker_found = True
                marker_index = i
                break
            marker_list.pop(0)
    return marker_index + 1

def part_2(content):
    marker, marker_count, marker_length, marker_found = 0, 0, 14, False
    marker_index, marker_list = 0, []
    for i in range(len(content)):
        if marker_found:
            break
        marker_list.append(content[i])
        if len(marker_list) == marker_length:
            if len(set(marker_list)) == marker_length:
                marker_found = True
                marker_index = i
                break
            marker_list.pop(0)
    return marker_index + 1

def main():
    with open(sys.argv[1]) as f:
        content = f.read().strip()
    print(f"Part 1: {part_1(content)}")
    print(f"Part 2: {part_2(content)}")

if __name__ == '__main__':
    main()


