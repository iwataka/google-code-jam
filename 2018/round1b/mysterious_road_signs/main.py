#!/usr/bin/env python

import collections


Subseq = collections.namedtuple('Subseq', ('start', 'end', 'M', 'N'))


def solve(signs):
    queue = [(0, len(signs) - 1)]
    max_size = 0
    max_count = 0
    # TODO: priority queue
    while queue:
        start_i, end_i = queue.pop()
        if end_i - start_i + 1 < max_size:
            continue
        size, count = longetst_path_from_center(signs, start_i, end_i)
        max_size, max_count = append_size(max_size, max_count, size, count)
        mid_i = (start_i + end_i) // 2
        if start_i <= mid_i - 1:
            queue.append((start_i, mid_i - 1))
        if mid_i + 1 <= end_i:
            queue.append((mid_i + 1, end_i))
    return max_size, max_count


def longetst_path_from_center(signs, s, e):
    mid_i = (s + e) // 2
    subseq_list = []
    subseq_list.append(walkthrough(signs, mid_i, s, 0))
    subseq_list.append(walkthrough(signs, mid_i, e, 0))
    subseq_list.append(walkthrough(signs, mid_i, s, 1))
    subseq_list.append(walkthrough(signs, mid_i, e, 1))
    nums2range = {}
    for M, N, start, end in subseq_list:
        if not (M, N) in nums2range:
            nums2range[(M, N)] = (start, end)
        else:
            cur_start, cur_end = nums2range[(M, N)]
            new_start = start if start < cur_start else cur_start
            new_end = end if end > cur_end else cur_end
            nums2range[(M, N)] = (new_start, new_end)

    sizes = map(lambda x: x[1] - x[0] + 1, set(nums2range.values()))
    
    max_size = 0
    max_count = 0
    for size in sizes:
        max_size, max_count = append_size(max_size, max_count, size, 1)
    return max_size, max_count


def append_size(cur_max_size, cur_max_count, size, count):
    if size > cur_max_size:
        return size, count
    elif size == cur_max_size:
        return size, cur_max_count + count
    else:
        return cur_max_size, cur_max_count


def walkthrough(signs, i_start, i_end, i_fix):
    i_not_fix = 0 if i_fix else 1
    if i_start == i_end:
        return signs[i_start][0], signs[i_start][1], i_start, i_start
    fix_val = signs[i_start][i_fix]
    not_fix_val = None
    i_subseq_end = None
    direction = 1 if i_end > i_start else -1

    for i in range(i_start + direction, i_end + direction, direction):
        i_subseq_end = i
        sign = signs[i]
        if sign[i_fix] == fix_val:
            continue
        if not_fix_val is None:
            not_fix_val = sign[i_not_fix]
            continue
        if sign[i_not_fix] == not_fix_val:
            continue
        i_subseq_end = i - direction
        break
    if not_fix_val is None:
        not_fix_val = signs[i_start][i_not_fix]

    if i_fix == 0:
        M = fix_val
        N = not_fix_val
    else:
        M = not_fix_val
        N = fix_val
    if i_start < i_subseq_end:
        start = i_start
        end = i_subseq_end
    else:
        start = i_subseq_end
        end = i_start
    return M, N, start, end


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
