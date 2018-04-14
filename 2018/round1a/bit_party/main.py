#!/usr/bin/env python

import math

def solve(n_robots, n_bits, cashier_infos):
    max_spent_time = max([x[0] * x[1] + x[2] for x in cashier_infos])
    smallest_time = 0
    largetst_time = max_spent_time
    while smallest_time < largetst_time:
        time = (smallest_time + largetst_time) // 2
        if able_to_buy(n_robots, n_bits, cashier_infos, time):
            largetst_time = time
        else:
            smallest_time = time + 1
    return smallest_time

def able_to_buy(n_robots, n_bits, cashier_infos, time):
    capacities = [max(0, min(x[0], math.floor((time - x[2]))) / x[1]) for x in cashier_infos]
    return n_bits <= sum(capacities[0:n_robots + 1])

if __name__ == '__main__':
    n_tests = int(input())
    for i in range(n_tests):
        r, b, c = [int(x) for x in input().split()]
        cashier_infos = []
        for _ in range(c):
            cashier_infos.append([int(x) for x in input().split()])
        ans = solve(r, b, cashier_infos)
        print("Case #%d: %d" % (i + 1, ans))
