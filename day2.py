from functools import reduce

with open('resources/day2.txt') as f:
    s = f.readlines()

data = [[int(i) for i in l.split()] for l in s]


def is_safe(ls):
    diffs = []
    for i1, i2 in zip(ls[:-1], ls[1:]):
        d = i1 - i2
        if abs(d) > 3:
            return False
        diffs.append(i1 - i2)
    return all(map(lambda x: x > 0, diffs)) or all(map(lambda x: x < 0, diffs))


def is_safe_dampener(ls):
    for i in range(len(ls)):
        if is_safe(ls[:i] + ls[i + 1:]):
            return True
    return False


def part1(ls):
    return reduce(lambda x, y: x + (1 if is_safe(y) else 0), ls, 0)


def part2(ls):
    return reduce(lambda x, y: x + (1 if is_safe_dampener(y) else 0), ls, 0)


print(part1(data))  # 379
print(part2(data))  # 430
