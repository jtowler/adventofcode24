from itertools import product

with open('resources/day7.txt') as f:
    data = [i.strip() for i in f.readlines()]

add = lambda x, y: x + y
mult = lambda x, y: x * y
concat = lambda x, y: int(str(x) + str(y))
operators = [add, mult]
operators2 = [add, mult, concat]


def is_valid(res, vals, operators):
    for ops in product(operators, repeat=(len(vals) - 1)):
        t = vals[0]
        for i in range(len(vals) - 1):
            t = ops[i](t, vals[i + 1])
        if t == res:
            return True
    return False


def part1(s, ops):
    t = 0
    for ss in s:
        ss = ss.split(': ')
        result = int(ss[0])
        vals = list(map(int, ss[1].split(' ')))
        if is_valid(result, vals, ops):
            t += result
    return t


print(part1(data, [add, mult]))  # 7710205485870
print(part1(data, [add, mult, concat]))  # 4719
