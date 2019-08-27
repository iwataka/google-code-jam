#!/usr/bin/env python

import math

def solve(p, cookies):
    default_perimeter = sum([(x[0] + x[1]) * 2 for x in cookies])
    diag_lens = [[min(x[0], x[1]), math.sqrt(x[0]**2 + x[1]**2)] for x in cookies]
    sum_max_diag_lens = sum([x[1] * 2 for x in diag_lens])
    max_len = sum_max_diag_lens + default_perimeter
    if max_len < p:
        return max_len

    sum_min_diag_lens = sum([x[0] * 2 for x in diag_lens])
    min_len = sum_min_diag_lens + default_perimeter
    if min_len <= p <= max_len:
        return p

    result = calc(diag_lens, default_perimeter, default_perimeter, p)
    if result == -1:
        return p

    return result

def calc(diag_lens, min_val, max_val, p, pointer=None):
    if pointer is None:
        pointer = 0

    if min_val > p:
        return None
    if min_val <= p <= max_val:
        return -1
    if pointer == len(diag_lens):
        return max_val

    min_diag, max_diag = diag_lens[pointer]
    result_with_cut = calc(diag_lens, min_val + min_diag * 2, max_val + max_diag * 2, p, pointer + 1)
    if result_with_cut == -1:
        return -1
    result_without_cut = calc(diag_lens, min_val, max_val, p, pointer + 1)
    if result_without_cut == -1:
        return -1

    return max([x for x in [result_with_cut, result_without_cut] if x is not None])

if __name__ == '__main__':
    n_tests = int(input())
    for i in range(n_tests):
        n, p = [int(x) for x in input().split()]
        cookies = []
        for _ in range(n):
            cookies.append([int(x) for x in input().split()])
        ans = solve(p, cookies)
        print("Case #%d: %f" % (i + 1, ans))
