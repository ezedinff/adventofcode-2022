# @author: Ezedin Fedlu
# @date: 2022-12-21
# @version: 1.0.0
# @description: Advent of Code 2022 - Day 21

import sys

def parse_input(file_path):
    with open(file_path) as f:
        lines = [line.strip() for line in f.readlines()]
        return {line.split(':')[0]: line.split(':')[1].split() for line in lines}


def evaluate(monkeys, name, h):
    # If the monkey's name is "humn" and h is greater than or equal to 0, return h
    if name == 'humn' and h >= 0:
        return h

    # Try to convert the first element in the list of words associated with the monkey's name to an integer
    try:
        return int(monkeys[name][0])
    # If the conversion fails, assume that the monkey's job is an arithmetic operation and recursively evaluate the operands
    except ValueError:
        assert len(monkeys[name]) == 3
        e1 = evaluate(monkeys, monkeys[name][0], h)
        e2 = evaluate(monkeys, monkeys[name][2], h)
        if monkeys[name][1] == '+':
            return e1 + e2
        elif monkeys[name][1] == '-':
            return e1 - e2
        elif monkeys[name][1] == '*':
            return e1 * e2
        elif monkeys[name][1] == '/':
            return e1 / e2
        else:
            assert False, expr


def monkey_math(monkeys):
    # Call the evaluate function with the name "root" and the value of h
    p1 = monkeys['root'][0]
    p2 = monkeys['root'][2]

    if evaluate(monkeys, p2, 0) != evaluate(monkeys, p2, 1):
        p1, p2 = p2, p1
    assert evaluate(monkeys, p1, 0) != evaluate(monkeys, p1, 1)
    assert evaluate(monkeys, p2, 0) == evaluate(monkeys, p2, 1)
    target = evaluate(monkeys, p2, 0)

    # binary search
    lo = 0
    hi = int(1e20)
    while lo < hi:
        mid = (lo+hi)//2
        score = target - evaluate(monkeys, p1, mid)
        if score < 0:
            lo = mid
        elif score == 0:
            return mid
        else:
            hi = mid


def main():
    monkeys = parse_input(sys.argv[1])
    print(f"part 1: {int(evaluate(monkeys, 'root', -1))}")
    print(f"part 2: {monkey_math(monkeys)}")


if __name__ == '__main__':
    main()