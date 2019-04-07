#!/usr/bin/env python

def revpath(c):
    if c == 'S':
        return 'E'
    else:
        return 'S'


def solve(N, P):
    head = P[0]
    tail = P[len(P) - 1]
    revhead = revpath(head)
    if tail != head:
        return revhead * (N - 1) + head * (N - 1)

    considx = P.find(revhead * 2)
    revcount = P[0:considx].count(revhead)
    return revhead * (revcount + 1) + head * (N - 1) + revhead * (N - 1 - revcount - 1)


def solve_all():
    N_TESTS = int(input())
    for i in range(N_TESTS):
        N = int(input())
        P = input()
        ans = solve(N, P)
        print("Case #%d: %s" % (i + 1, ans))


if __name__ == '__main__':
    solve_all()
