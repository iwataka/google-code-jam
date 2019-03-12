#!/usr/bin/env python

def solve(signs):
    queue = [(0, len(signs) - 1)]
    max_size = 0
    max_count = 0
    while queue:
        start_i, end_i = queue.pop()
        if end_i - start_i + 1 < max_size:
            continue
        size, count = longetst_path_from_center(signs, start_i, end_i)
        if size > max_size:
            max_size = size
            max_count = count
        elif size == max_size:
            max_count += count
        mid_i = (start_i + end_i) // 2
        if start_i <= mid_i - 1:
            queue.append((start_i, mid_i - 1))
        if mid_i + 1 <= end_i:
            queue.append((mid_i + 1, end_i))
    return max_size, max_count


def longetst_path_from_center(signs, s, e):
    mid_i = (s + e) // 2
    n_low, i_n_low = walkthrough(signs, mid_i, s, 0)
    n_high, i_n_high = walkthrough(signs, mid_i, e, 0)
    m_low, i_m_low = walkthrough(signs, mid_i, s, 1)
    m_high, i_m_high = walkthrough(signs, mid_i, e, 1)
    fix_n = signs[mid_i][1]
    queue = []
    if n_low == n_high and n_low != fix_n:
        size = i_n_high - i_n_low + 1
        queue.append((size, i_n_low, i_n_high))
    else:
        if n_low != fix_n:
            queue.append((mid_i - i_n_low + 1, i_n_low, mid_i))
        if n_high != fix_n:
            queue.append((i_n_high - mid_i + 1, mid_i, i_n_high))
    if m_low == m_high:
        size = i_m_high - i_m_low + 1
        queue.append((size, i_m_low, i_m_high))
    else:
        queue.append((mid_i - i_m_low + 1, i_m_low, mid_i))
        queue.append((i_m_high - mid_i + 1, mid_i, i_m_high))
    max_size = 0
    queue = list(set(queue))
    for size, _, _ in queue:
        if size > max_size:
            max_size = size
            max_count = 1
        elif size == max_size:
            max_count += 1
    return max_size, max_count


def walkthrough(signs, start_i, end_i, fix_i):
    fix_val = signs[start_i][fix_i]
    another_i = 0 if fix_i else 1
    if start_i == end_i:
        return signs[start_i][another_i], start_i
    another_val = None
    term_i = None
    direction = (end_i - start_i) // abs(end_i - start_i)
    for i in range(start_i + direction, end_i + direction, direction):
        term_i = i
        sign = signs[i]
        if sign[fix_i] == fix_val:
            continue
        elif another_val is None:
            another_val = sign[another_i]
            continue
        elif sign[another_i] == another_val:
            continue
        else:
            term_i = i - direction
            break
    if another_val is None:
        another_val = signs[start_i][another_i]
    return another_val, term_i


def solve_all():
    n_tests = int(input())
    for i in range(n_tests):
        n_signs = int(input())
        signs = []
        for _ in range(n_signs):
            d, a, b = map(int, input().split())
            signs.append((d + a, d - b))
        max_num, max_size = solve(signs)
        print("Case #%d: %d %d" % (i + 1, max_num, max_size))


if __name__ == '__main__':
    solve_all()
