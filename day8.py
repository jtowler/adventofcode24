import itertools
from itertools import product

with open('resources/day8.txt') as f:
    data = [i.strip() for i in f.readlines()]

nodes = {}
for i in range(len(data)):
    for j in range(len(data[0])):
        c = data[i][j]
        if c != '.':
            nodes[(i, j)] = c
unique_nodes = set(nodes.values())


def check(y, x):
    return 0 <= y < len(data) and 0 <= x < len(data[0])


def create_antinodes(n1, n2):
    def create_antinode(ind, dist):
        if n1[ind] < n2[ind]:
            return n1[ind] - dist, n2[ind] + dist
        else:
            return n1[ind] + dist, n2[ind] - dist

    a1_y, a2_y = create_antinode(0, abs(n1[0] - n2[0]))
    a1_x, a2_x = create_antinode(1, abs(n1[1] - n2[1]))
    return (a1_y, a1_x), (a2_y, a2_x)


def horiz(n1, n2):
    if n1[1] < n2[1]:
        left, right = n1, n2
    else:
        left, right = n2, n1
    dist = right[1] - left[1]

    antinodes = set()

    n = right[1]
    while n < len(data[0]):
        antinodes.add((n1[0], n))
        n += dist

    n = left[1]
    while n >= 0:
        antinodes.add((n1[0], n))
        n -= dist

    return antinodes


def vert(n1, n2):
    if n1[0] < n2[0]:
        up, down = n1, n2
    else:
        up, down = n2, n1
    dist = down[0] - up[0]

    antinodes = set()

    n = down[1]
    while n < len(data):
        antinodes.add((n, n1[1]))
        n += dist

    n = up[1]
    while n >= 0:
        antinodes.add((n, n1[1]))
        n -= dist

    return antinodes


def diag_ul_lr(n1, n2):
    if n1[0] < n2[0]:
        ul, lr = n1, n2
    else:
        ul, lr = n2, n1
    ydist = lr[0] - ul[0]
    xdist = lr[1] - ul[1]

    antinodes = set()

    y, x = lr
    while y < len(data) and x < len(data[0]):
        antinodes.add((y, x))
        y += ydist
        x += xdist

    y, x = ul
    while y >= 0 and x >= 0:
        antinodes.add((y, x))
        y -= ydist
        x -= xdist

    return antinodes


def diag_ll_ur(n1, n2):
    if n1[0] > n2[0]:
        ll, ur = n1, n2
    else:
        ll, ur = n2, n1
    ydist = ll[0] - ur[0]
    xdist = ur[1] - ll[1]

    antinodes = set()

    y, x = ll
    while y < len(data) and x >= 0:
        antinodes.add((y, x))
        y += ydist
        x -= xdist

    y, x = ur
    while y >= 0 and x < len(data[0]):
        antinodes.add((y, x))
        y -= ydist
        x += xdist

    return antinodes


def create_antinodes2(n1, n2):
    if n1[0] == n2[0]:
        return horiz(n1, n2)
    elif n1[1] == n2[1]:
        return vert(n1, n2)
    elif n1[0] > n2[0] and n1[1] > n1[1]:
        return diag_ul_lr(n1, n2)
    else:
        return diag_ll_ur(n1, n2)


def get_antinodes(node, f=create_antinodes):
    return {an for n1, n2 in itertools.combinations([k for k, v in nodes.items() if v == node], 2)
            for an in f(n1, n2)}


def part1():
    return len({an for node in unique_nodes for an in get_antinodes(node) if check(*an)})


def part2():
    return len({an for node in unique_nodes
                for an in get_antinodes(node, create_antinodes2) if check(*an)})


print(part1())  # 313
print(part2())  # 1064
