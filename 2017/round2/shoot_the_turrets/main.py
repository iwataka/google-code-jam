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
        path = find_alternating_path(graph, connections)
        if path:
            for i in range(len(path)):
                changed = True
                if i % 2 == 0:
                    connections[path[i]] = path[i + 1]
                elif i + 1 < len(path):
                    connections[path[i + 1]] = -1
        if not changed:
            break

    maxbpm = [[0] * len(graph[0]) for _ in graph]
    for d, s in enumerate(connections):
        if s >= 0:
            maxbpm[s][d] = 1

    return maxbpm


def find_alternating_path(graph, connections):
    not_adj_dests = []
    for i, adj in enumerate(connections):
        if adj < 0:
            not_adj_dests.append(i)

    queue = []

    for i_d in not_adj_dests:
        for i_s in range(len(graph)):
            if graph[i_s][i_d] == 1:
                queue.append([i_d, i_s])

    while True:
        try:
            path = queue.pop()
        except IndexError:
            break

        try:
            d_appended = connections.index(path[-1])
        except ValueError:
            if len(path) >= 3:
                return path
            else:
                continue

        path.append(d_appended)

        for i_s, row in enumerate(graph):
            if row[d_appended] == 1 and connections[d_appended] != i_s:
                if i_s not in path[1::2]:
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

    bp_graph = [[0] * len(turrets) for _ in soldiers]

    shootable_turrets_list = []
    visited_cache = [[None] * C for _ in range(R)]

    for i_s, soldier in enumerate(soldiers):
        x, y = soldier
        shootable_turrets = get_shootable_turrets(
            x, y, M, C, R, field, turrets, visited_cache)
        shootable_turrets_list.append(shootable_turrets)
        for ts in shootable_turrets:
            for i_t in ts:
                bp_graph[i_s][i_t] = 1

    maxbpm = calc_maxbpm(bp_graph)

    for row in maxbpm:
        if not 0 <= sum(row) <= 1:
            raise Exception(maxbpm)

    while True:
        maxbpm, changed1 = correct(maxbpm, shootable_turrets_list, turrets)
        maxbpm, changed2 = resolve_deadlocks(maxbpm, shootable_turrets_list, turrets)
        if not changed1 and not changed2:
            break

    pairs = []
    for i_r, row in enumerate(maxbpm):
        for i_c, num in enumerate(row):
            if num == 1:
                pairs.append((i_r, i_c))

    pairs = sort_answer(pairs, shootable_turrets_list)
    return len(pairs), pairs


def sort_answer(pairs, shootable_turrets_lists):
    ps = list(pairs)
    shooted_turrets = []
    result = []

    while ps:
        exist = False
        for pair in ps:
            soldier, turret = pair
            shootable_turrets_list = shootable_turrets_lists[soldier]
            first_noempty_turrets = next(ts for ts in shootable_turrets_list if ts and not all(x in shooted_turrets for x in ts))
            if turret in first_noempty_turrets:
                shooted_turrets.append(turret)
                ps.remove(pair)
                result.append(pair)
                exist = True
                break
        if not exist:
            for soldier, shootable_turrets_list in enumerate(shootable_turrets_lists):
                print(soldier + 1, [list(map(lambda x: x + 1, [t for t in ts if t not in shooted_turrets])) for ts in shootable_turrets_list])
            for soldier, turret in ps:
                print(soldier + 1, turret + 1)
            raise AssertionError

    return result


def correct(maxbpm, shootable_turrets_list, turrets):
    shooted_turrets = set()
    for _, row in enumerate(maxbpm):
        for i_t, adj in enumerate(row):
            if adj == 1:
                shooted_turrets.add(i_t)
                break

    changed = False
    for i_s, row in enumerate(maxbpm):
        for i_t, adj in enumerate(row):
            if adj == 1:
                for shootable_turrets in shootable_turrets_list[i_s]:
                    if i_t in shootable_turrets:
                        break
                    exit = False
                    for i_turret in shootable_turrets - shooted_turrets:
                        maxbpm[i_s][i_turret] = 1
                        maxbpm[i_s][i_t] = 0
                        changed = True
                        exit = True
                        shooted_turrets.remove(i_t)
                        shooted_turrets.add(i_turret)
                        break
                    if exit:
                        break
    return maxbpm, changed


def resolve_deadlocks(bpm, shootable_turrets_list, turrets):
    changed = False
    while True:
        deadlock = get_deadlock(bpm, shootable_turrets_list, turrets)
        if deadlock:
            for i, pair in enumerate(deadlock):
                i_s, i_t = pair
                _, another_i_t = deadlock[i - 1]
                bpm[i_s][i_t] = 0
                bpm[i_s][another_i_t] = 1
                changed = True
        else:
            break
    return bpm, changed


def get_deadlock(bpm, shootable_turrets_list, turrets):
    queue = []

    for i_s, row in enumerate(bpm):
        try:
            i_t = row.index(1)
        except Exception:
            continue

        first_nonempty_ts = next(
            ts for ts in shootable_turrets_list[i_s] if len(ts) > 0)
        if turrets[i_t] not in first_nonempty_ts:
            queue.append([(i_s, i_t)])

    while True:
        try:
            path = queue.pop()
            i_s, i_t = path[-1]
        except Exception:
            break

        for another_i_s, another_shootable_turrets in enumerate(shootable_turrets_list):
            if i_s == another_i_s:
                continue

            try:
                another_i_t = bpm[another_i_s].index(1)
            except Exception:
                continue

            another_i_list = next(i for i, ts in enumerate(
                another_shootable_turrets) if another_i_t in ts)
            if any(ts for ts in another_shootable_turrets[:another_i_list] if i_t in ts):
                try:
                    return path[path.index((another_i_s, another_i_t)):]
                except Exception:
                    pass
                queue.append(path + [(another_i_s, another_i_t)])


def get_shootable_turrets(x, y, max_M, C, R, field, turrets, visited_cache=None, visited=None):
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
                x, y, C, R, field, -1, 0, turrets))
            ts.update(get_shootable_turrets_without_move(
                x, y, C, R, field, 1, 0, turrets))
            ts.update(get_shootable_turrets_without_move(
                x, y, C, R, field, 0, -1, turrets))
            ts.update(get_shootable_turrets_without_move(
                x, y, C, R, field, 0, 1, turrets))
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


def get_shootable_turrets_without_move(x, y, C, R, field, dx, dy, turrets):
    x = x + dx
    y = y + dy
    result = set()
    while x >= 0 and y >= 0 and x <= R - 1 and y <= C - 1:
        cell = field[x][y]
        if cell == '#':
            break
        if cell == 'T':
            result.add(turrets.index((x, y)))
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
