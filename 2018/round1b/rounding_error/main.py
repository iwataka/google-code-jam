#!/usr/bin/env python

from heapq import heappush, heappop

def solve():
    sum_cs = sum(cs)
    remaining = n - sum_cs
    calc(remaining)
    return calc_result()


def calc(remaining):
    pq = []
    for i, c in enumerate(cs):
        gap = gap_until_roundup(c, remaining + 1)
        if gap:
            heappush(pq, (gap, i))
    while remaining > 0 and pq:
        gap, i = heappop(pq)
        assignment = min(remaining, gap)
        cs[i] += assignment
        remaining -= assignment


def calc_result():
    return sum(map(lambda x: round_num(x * 100 / n), cs))


def gap_until_roundup(c, m):
    count = 0
    while not can_roundup(c + count) and count < m:
        count += 1
    return count


def can_roundup(c):
    num = c * 100 / n
    return round_num(num) > num


def round_num(num):
    i_num = int(num)
    if num >= i_num + 0.5:
        return i_num + 1
    return i_num


if __name__ == '__main__':
    N_TESTS = int(input())
    for i_tests in range(N_TESTS):
        n, l = map(int, input().split())
        cs = list(map(int, input().split()))
        cs.extend([0] * (n - len(cs)))
        ans = solve()
        print("Case #%d: %d" % (i_tests + 1, ans))
