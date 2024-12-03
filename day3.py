import re
from functools import reduce

with open('resources/day3.txt') as f:
    data = ''.join(f.readlines())


def part1(s):
    muls = re.findall('(mul\(\d+,\d+\))', s)
    t = 0
    for m in muls:
        v1, v2 = m[4:-1].split(',')
        t += int(v1) * int(v2)
    return t


def part2(s):
    dos = [i for i in range(len(s) - 4) if s[i:i + 4] == 'do()']
    donts = [i for i in range(len(s) - 7) if s[i:i + 7] == "don't()"]

    do_dont = []
    current_do = 0

    is_do = True

    for i in range(len(s)):

        if is_do and i in donts:
            do_dont.append((current_do, i))
            is_do = False
        elif not is_do and i in dos:
            current_do = i
            is_do = True

    if is_do:
        do_dont.append((current_do, i))

    return reduce(lambda x, y: part1(s[y[0]:y[1]]) + x, do_dont, 0)


print(part1(data))  # 189600467
print(part2(data))  # 107069718
