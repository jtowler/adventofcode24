import itertools
from itertools import product

with open('resources/day10.txt') as f:
    data = [i.strip() for i in f.readlines()]
    grid = [[int(i) for i in l] for l in data]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def score(trail, trails=[]):
    y, x = trail[-1]
    v = grid[y][x]
    if v == 9:
        trails.append(trail)
    else:
        dir_options = [(y + dy, x + dx) for dy, dx in dirs
                       if 0 <= (y + dy) < len(grid) and 0 <= (x + dx) < len(grid[0])
                       and grid[y + dy][x + dx] == (v + 1)]
        for dy, dx in dir_options:
            score(trail + [(dy, dx)], trails)


def part0(f):
    total = 0
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 0:
                trails = []
                score([(y, x)], trails=trails)
                uni_sinks = []
                for t in trails:
                    n = f(t)
                    if n not in uni_sinks:
                        uni_sinks.append(n)
                total += len(uni_sinks)
    return total


print(part0(lambda x: x[-1]))  # 550
print(part0(lambda x: x))  # 1255
