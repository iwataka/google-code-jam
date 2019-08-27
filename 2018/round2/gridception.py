#!/usr/bin/env python

def solve(a, b):
    return 0

if __name__ == '__main__':
    n_tests = int(input())
    for i in range(n_tests):
        a, b = map(int, input().split())
        ans = solve(a, b)
        print("Case #%d: %d" % (i + 1, ans))
