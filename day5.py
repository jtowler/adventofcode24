from functools import reduce

with open('resources/day5.txt') as f:
    ins, ords = ''.join(f.readlines()).split('\n\n')

ins = [i.split('|') for i in ins.split('\n')]
ins = [(int(i[0]), int(i[1])) for i in ins]

ords = [i.split(',') for i in ords.split('\n')]
ords = [[int(i) for i in o] for o in ords]


def is_ordered(order):
    for i in range(len(order)):
        o = order[i]
        o_ins = [t for f, t in ins if f == o]

        for oi in o_ins:
            if oi in order and order.index(oi) < i:
                return False
    return True


def reorder(order):
    lens = [(i, len([x for x, y in ins if x == i and y in order])) for i in order]
    return sorted(lens, key=lambda x: x[1], reverse=True)[len(order) // 2][0]


def part1(orders):
    to_count = filter(is_ordered, orders)
    return reduce(lambda a, o: a + o[len(o) // 2], to_count, 0)


def part2(orders):
    to_reorder = filter(lambda x: not is_ordered(x), orders)
    return reduce(lambda a, o: a + reorder(o), to_reorder, 0)


print(part1(ords))  # 5964
print(part2(ords))  # 4719
