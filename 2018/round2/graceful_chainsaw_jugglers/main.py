#!/usr/bin/env python

def solve(R, B):
    sum_of_chainsaws = 1
    n_varieties = 0
    while True:
        cands = [(sum_of_chainsaws - i, i) for i in range(sum_of_chainsaws + 1)]
        rate = R / B if B != 0 else 501
        cands.sort(key=lambda x: abs((x[0] / x[1] if x[1] != 0 else 501) - rate))
        for r, b in cands:
            if R >= r and B >= b:
                R -= r
                B -= b
                n_varieties += 1
        # dr = -1 if R > B else 1
        # db = 1 if R > B else -1
        # r = sum_of_chainsaws if dr == -1 else 0
        # b = sum_of_chainsaws if db == -1 else 0 
        # while r >= 0 and b >= 0:
        #     if R >= r and B >= b:
        #         R -= r
        #         B -= b
        #         n_varieties += 1
        #         print(r, b)
        #     r += dr
        #     b += db
        sum_of_chainsaws += 1
        if R + B < sum_of_chainsaws:
            break
    return n_varieties

if __name__ == '__main__':
    n_tests = int(input())
    for i in range(n_tests):
        R, B = map(int, input().split())
        ans = solve(R, B)
        print("Case #%d: %d" % (i + 1, ans))
