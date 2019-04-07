#!/usr/bin/env python

import string


def factor(n):
    for i in range(2, n):
        if n % i == 0:
            return i, n // i


def startpos(nums):
    for i, n in enumerate(nums):
        if n != nums[i + 1]:
            return i


def decrypt(ns):
    copied = list(set(ns))
    copied.sort()
    n2c = {}
    alphas = string.ascii_uppercase
    for i, n in enumerate(copied):
        n2c[n] = alphas[i]
    result = []
    for n in ns:
        result.append(n2c[n])
    return result


def solve(N, L, nums):
    ns = []
    start = startpos(nums)

    a, b = factor(nums[start])
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
