import sys

def parse_input():
    with open(sys.argv[1]) as f:
        return [group for group in f.read().strip().split("\n\n")]

def part1(groups):
    monkeys = []

    for group in groups:
        lines = group.splitlines()
        monkey = []
        monkey.append(list(map(int, lines[1].split(": ")[1].split(", "))))
        monkey.append(eval("lambda old:" + lines[2].split("=")[1]))
        for line in lines[3:]:
            monkey.append(int(line.split()[-1]))
        monkeys.append(monkey)

    counts = [0] * len(monkeys)

    for _ in range(20):
        for index, monkey in enumerate(monkeys):
            for item in monkey[0]:
                item = monkey[1](item)
                item //= 3
                if item % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(item)
                else:
                    monkeys[monkey[4]][0].append(item)
            counts[index] += len(monkey[0])
            monkey[0] = []

    counts.sort()
    return counts[-1] * counts[-2]

def part2(groups):
    monkeys = []
    for group in groups:
        lines = group.splitlines()
        monkey = []
        monkey.append(list(map(int, lines[1].split(": ")[1].split(", "))))
        monkey.append(eval("lambda old:" + lines[2].split("=")[1]))
        for line in lines[3:]:
            monkey.append(int(line.split()[-1]))
        monkeys.append(monkey)

    counts = [0] * len(monkeys)

    mod = 1
    for monkey in monkeys:
        mod *= monkey[2]

    for _ in range(10000):
        for index, monkey in enumerate(monkeys):
            for item in monkey[0]:
                item = monkey[1](item)
                item %= mod
                if item % monkey[2] == 0:
                    monkeys[monkey[3]][0].append(item)
                else:
                    monkeys[monkey[4]][0].append(item)
            counts[index] += len(monkey[0])
            monkey[0] = []

    counts.sort()
    return counts[-1] * counts[-2]

def main():
    groups = parse_input()
    print(f"Part 1: {part1(groups)}")
    print(f"Part 2: {part2(groups)}")

if __name__ == "__main__":
    main()