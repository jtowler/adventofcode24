from functools import reduce

with open('resources/day1.txt') as f:
    s = [i.split() for i in f.readlines()]

list0 = [int(i[0]) for i in s]
list1 = [int(i[1]) for i in s]


def day1(l0, l1):
    return reduce(lambda x, y: x + abs(y[0] - y[1]), zip(sorted(l0), sorted(l1)), 0)


def day2(l0, l1):
    return reduce(lambda x, y: x + l1.count(y) * y, l0, 0)


print(day1(list0, list1))  # 1651298
print(day2(list0, list1))  # 21306195
