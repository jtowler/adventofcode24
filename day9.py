with open('resources/day9.txt') as f:
    data = f.readline().strip()


def decompress(s):
    ints = [int(i) for i in list(s)]
    new_s = []
    file_id = 0
    for i in range(len(ints)):
        if i % 2 == 0:
            new_s += [file_id] * ints[i]
            file_id += 1
        else:
            new_s += [None] * ints[i]
    return new_s


def strip_tail(ls):
    if ls[-1] is not None:
        return ls
    i = 0
    while ls[-(i + 1)] is None:
        i += 1
    return ls[:-i]


def defrag(ls):
    while None in ls:
        last = ls[-1]
        space = ls.index(None)
        ls = ls[:-1]
        ls[space] = last
        ls = strip_tail(ls)

    return ls


def defrag2(ls):
    max_file_id = max([i for i in ls if i])
    for file_id in range(max_file_id, -1, -1):
        file_ids = [i for i, a in enumerate(ls) if a == file_id]
        none_ids = None
        ind = 0
        while ind < len(ls) - len(file_ids):
            if all(ls[ind + i] is None for i in range(len(file_ids))):
                none_ids = [ind + i for i in range(len(file_ids))]
                break
            ind += 1
        if none_ids and none_ids[0] < file_ids[0]:
            for i in none_ids:
                ls[i] = file_id
            for i in file_ids:
                ls[i] = None
    return ls


def check_sum(ls):
    return sum([i * a for i, a in enumerate(ls) if a])


def part1(s):
    return check_sum(defrag(decompress(s)))


def part2(s):
    return check_sum(defrag2(decompress(s)))


print(part1(data))  # 6356833654075
print(part2(data))  # 6389911791746
