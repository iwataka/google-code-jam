#!/usr/bin/env python

import math


def solve(n_seats, n_customers, tickets):
    n_rides = 0
    for i in range(1, n_seats + 1):
        tmp_n_rides = math.ceil(sum([t[0] <= i for t in tickets]) / i)
        if n_rides < tmp_n_rides:
            n_rides = tmp_n_rides
    for i in range(1, n_customers + 1):
        tmp_n_rides = sum([t[1] == i for t in tickets])
        if n_rides < tmp_n_rides:
            n_rides = tmp_n_rides
    n_promotions = 0
    for i in range(1, n_seats + 1):
        n_promotions += max(sum([t[0] == i for t in tickets]) - n_rides, 0)
    return n_rides, n_promotions

if __name__ == '__main__':
    n_tests = int(input())
    for i in range(n_tests):
        n, c, m = map(int, input().split())
        tickets = []
        for _ in range(m):
            tickets.append([int(x) for x in input().split()])
        y, z = solve(n, c, tickets)
        print("Case #%d: %d %d" % (i + 1, y, z))
