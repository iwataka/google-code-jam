#!/usr/bin/env python


def calc_maxbpm(graph):
    connections = [-1] * len(graph[0])
    for i_s, src in enumerate(graph):
        for i_d, adj in enumerate(src):
            if adj == 1 and connections[i_d] == -1:
                connections[i_d] = i_s
                break

    while True:
        changed = False
        for path in find_alternating_path(graph, connections):
            for i in range(len(path)):
                if i % 2 == 0:
                    connections[path[i]] = path[i + 1]
                    changed = True
                else:
                    connections[path[i + 1]] = -1
        if not changed:
            break

    maxbpm = [[0] * len(graph[0]) for _ in graph]
    for d, s in enumerate(connections):
        if s != -1:
            maxbpm[s][d] = 1

    return maxbpm

def find_alternating_path(graph, connections):
    not_adj_dests = []
    for i, adj in enumerate(connections):
        if adj != -1:
            break
        not_adj_dests.append(i)

    queue = []

    for i_d in not_adj_dests:
        for i_s, row in enumerate(graph):
            if row[i_d] == 1 and connections[i_d] != i_s:
                queue.append(([i_d, i_s]))

    while True:
        try:
            path = queue.pop(0)
        except IndexError:
            break

        try:
            i1 = connections.index(path[-1])
        except ValueError:
            if len(path) >= 3:
                yield path
            else:
                continue

        path.append(i1)

        for i_s, row in enumerate(graph):
            if row[i1] == 1 and connections[i1] != i_s:
                queue.append((path + [i_s]))


def solve(C, R, M, field):
    soldiers = []
    turrets = []
    for r, row in enumerate(field):
        for c, cell in enumerate(row):
            if cell == 'S':
                soldiers.append((r, c))
            elif cell == 'T':
                turrets.append((r, c))
    bp_graph = []
    for i_s in range(len(soldiers)):
        bp_graph.append([0] * len(turrets))
    shootable_turrets_list = []
    visited_cache = [[None] * C for _ in range(R)]
    for i_s, soldier in enumerate(soldiers):
        x, y = soldier
        shootable_turrets = get_shootable_turrets(
            x, y, M, C, R, field, visited_cache)
        shootable_turrets_list.append(shootable_turrets)
        for ts in shootable_turrets:
            for t in ts:
                i_t = turrets.index(t)
                bp_graph[i_s][i_t] = 1
    max_bpm = calc_maxbpm(bp_graph)
    while True:
        max_bpm, corrected = correct(max_bpm, shootable_turrets_list, turrets)
        if not corrected:
            break
    pairs = []
    for i_r, row in enumerate(max_bpm):
        for i_c, num in enumerate(row):
            if num == 1:
                pairs.append((i_r, i_c))
    return len(pairs), pairs


def correct(max_bpm, shootable_turrets_list, turrets):
    corrected = False
    shooted_turrets = set()
    for i_s, row in enumerate(max_bpm):
        for i_t, cell in enumerate(row):
            if cell == 1:
                shooted_turrets.add(turrets[i_t])
                break
    for i_s, row in enumerate(max_bpm):
        for i_t, cell in enumerate(row):
            if cell == 1:
                for shootable_turrets in shootable_turrets_list[i_s]:
                    cur_turret = turrets[i_t]
                    if cur_turret in shootable_turrets:
                        break
                    exit = False
                    for turret in shootable_turrets - shooted_turrets:
                        max_bpm[i_s][turrets.index(turret)] = 1
                        max_bpm[i_s][i_t] = 0
                        exit = True
                        corrected = True
                        shooted_turrets.remove(cur_turret)
                        shooted_turrets.add(turret)
                        break
                    if exit:
                        break
    return max_bpm, corrected


def get_shootable_turrets(x, y, max_M, C, R, field, visited_cache=None, visited=None):
    if visited is None:
        visited = [[False] * C for _ in range(R)]

    queue = [(x, y, max_M)]
    result = [set() for _ in range(max_M + 1)]

    while True:
        try:
            x, y, M = queue.pop(0)
        except IndexError:
            break

        if x < 0 or y < 0 or x >= R or y >= C or field[x][y] == '#':
            continue

        if visited[x][y]:
            continue

        if visited_cache is None or visited_cache[x][y] is None:
            ts = set()
            ts.update(get_shootable_turrets_without_move(
                x, y, C, R, field, -1, 0))
            ts.update(get_shootable_turrets_without_move(
                x, y, C, R, field, 1, 0))
            ts.update(get_shootable_turrets_without_move(
                x, y, C, R, field, 0, -1))
            ts.update(get_shootable_turrets_without_move(
                x, y, C, R, field, 0, 1))
            if visited_cache is not None:
                visited_cache[x][y] = ts
        else:
            ts = visited_cache[x][y]
        result[max_M - M].update(ts)

        visited[x][y] = True

        if M > 0:
            queue.append((x - 1, y, M - 1))
            queue.append((x + 1, y, M - 1))
            queue.append((x, y - 1, M - 1))
            queue.append((x, y + 1, M - 1))

    for i, r in enumerate(result):
        for j in range(i):
            r -= result[j]
    return result


def get_shootable_turrets_without_move(x, y, C, R, field, dx, dy):
    x = x + dx
    y = y + dy
    result = set()
    while x >= 0 and y >= 0 and x <= R - 1 and y <= C - 1:
        cell = field[x][y]
        if cell == '#':
            break
        if cell == 'T':
            result.add((x, y))
        x += dx
        y += dy
    return result


if __name__ == '__main__':
    n_tests = int(input())
    for i in range(n_tests):
        C, R, M = map(int, input().split())
        field = []
        for _ in range(R):
            row = [x for x in input()]
            field.append(row)
        ans, pairs = solve(C, R, M, field)
        print("Case #%d: %d" % (i + 1, ans))
        for pair in pairs:
            print("%d %d" % (pair[0] + 1, pair[1] + 1))
