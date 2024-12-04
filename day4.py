from itertools import product

with open('resources/day4.txt') as f:
    data = [i.strip() for i in f.readlines()]


def get_dir(x, y, ix, iy):
    s = ''
    for i in range(4):
        nx, ny = x + (i * ix), y + (i * iy)
        if ny >= len(data) or nx >= len(data[0]) or nx < 0 or ny < 0:
            return False
        s += data[ny][nx]
    return s == 'XMAS'


def get_mas(x, y):
    l1 = data[y - 1][x - 1] + data[y][x] + data[y + 1][x + 1]
    l2 = data[y + 1][x - 1] + data[y][x] + data[y - 1][x + 1]
    return (l1 in ['MAS', 'SAM']) and (l2 in ['MAS', 'SAM'])


def part1(s):
    t = 0

    for y in range(len(s)):
        for x in range(len(s[0])):

            for ix, iy in product([-1, 0, 1], [-1, 0, 1]):
                if ix == iy == 0:
                    continue
                if get_dir(x, y, ix, iy):
                    t += 1
    return t


def part2(s):
    t = 0
    for y in range(1, len(s) - 1):
        for x in range(1, len(s[0]) - 1):
            if get_mas(x, y):
                t += 1
    return t


print(part1(data))  # 2567
print(part2(data))  # 2029
