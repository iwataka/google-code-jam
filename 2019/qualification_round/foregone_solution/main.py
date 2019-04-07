#!/usr/bin/env python

def solve(N):
    left = ''
    right = ''
    for n in reversed(N):
        i = int(n)
        if i == 4:
            left = '2' + left
            right = '2' + right
        else:
            left = '0' + left
            right = str(i) + right
    return int(left.lstrip('0')), int(right.lstrip('0'))


def solve_all():
    N_TESTS = int(input())
    for i in range(N_TESTS):
        N = input()
        a, b = solve(N)
        print('Case #%d: %d %d' % (i + 1, a, b))


if __name__ == '__main__':
    solve_all()
