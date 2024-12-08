with open('resources/day6.txt') as f:
    data = [i.strip() for i in f.readlines()]

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def get_loc(s):
    for y in range(len(s)):
        for x in range(len(s[0])):
            if s[y][x] not in ['.', '#']:
                return y, x


def check_off(y, x, ind, s):
    dy, dx = dirs[ind]
    nx = x + dx
    ny = y + dy
    return ny < 0 or ny >= len(s) or nx < 0 or nx >= len(s[0])


def move(y, x, ind, s):
    dy, dx = dirs[ind]
    if s[y + dy][x + dx] == '#':
        return y, x, (ind + 1) % len(dirs)
    else:
        return y + dy, x + dx, ind


def is_loop(grid):
    cur_ind = 0
    cur_y, cur_x = get_loc(grid)

    visited = {(cur_y, cur_x, cur_ind)}
    while not check_off(cur_y, cur_x, cur_ind, grid):
        cur_y, cur_x, cur_ind = move(cur_y, cur_x, cur_ind, grid)
        if (cur_y, cur_x, cur_ind) in visited:
            return True
        else:
            visited.add((cur_y, cur_x, cur_ind))
    return False


def update_grid(s, y, x):
    grid = []
    for i in range(len(s)):
        if i != y:
            grid.append(s[i])
        else:
            ln = list(s[i])
            ln[x] = '#'
            grid.append(''.join(ln))
    return grid


def part1(s):
    cur_ind = 0
    cur_y, cur_x = get_loc(s)

    visited = {(cur_y, cur_x)}
    while not check_off(cur_y, cur_x, cur_ind, s):
        cur_y, cur_x, cur_ind = move(cur_y, cur_x, cur_ind, s)
        visited.add((cur_y, cur_x))

    return len(visited)


def part2(s):
    t = 0
    for y in range(len(s)):
        for x in range(len(s[0])):
            if s[y][x] == '.':
                grid = update_grid(s, y, x)
                if is_loop(grid):
                    t += 1
    return t


print(part1(data))  # 5239
print(part2(data))  # 1753
