#!/usr/bin/env python

import string


def factor(n, N):
    if n % 2 == 0:
        return 2, n // 2

    min = 3
    # improve performance by this statements (but failed somewhy)
    # min = n // N
    # if min % 2 == 0:
    #     min += 1

    for i in range(min, N, 2):
        if n % i == 0:
            return i, n // i


def startpos(nums):
    for i, n in enumerate(nums):
        if n != nums[i + 1]:
            return i


def decrypt(ns):
    copied = sorted(list(set(ns)))
    alphas = string.ascii_uppercase
    n2c = {n: alphas[i] for i, n in enumerate(copied)}
    return [n2c[n] for n in ns]


def solve(N, L, nums):
    ns = []
    start = startpos(nums)

    a, b = factor(nums[start], N)
    nextn = nums[start + 1]
    if nextn % a == 0:
        ns.append(b)
        ns.append(a)
        now = nextn // a
        ns.append(now)
    else:
        ns.append(a)
        ns.append(b)
        now = nextn // b
        ns.append(now)

    for n in nums[start + 2:]:
        now = n // now
        ns.append(now)

    now = ns[0]
    for n in reversed(nums[0:start]):
        now = n // now
        ns.insert(0, now)

    return ''.join(decrypt(ns))


def solve_all():
    N_TESTS = int(input())
    for i in range(N_TESTS):
        N, L = map(int, input().split())
        nums = [int(x) for x in input().split()]
        ans = solve(N, L, nums)
        print("Case #%d: %s" % (i + 1, ans))


if __name__ == '__main__':
    solve_all()
