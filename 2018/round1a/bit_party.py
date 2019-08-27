#!/usr/bin/env python

def solve(n_robots, n_bits, cashier_infos):
    max_spent_time = max([x[0] * x[1] + x[2] for x in cashier_infos])
    smallest_time = 0
    largetst_time = max_spent_time
    while smallest_time < largetst_time:
        time = (smallest_time + largetst_time) // 2
        if is_purchasable(n_robots, n_bits, cashier_infos, time):
            largetst_time = time
        else:
            smallest_time = time + 1
    return smallest_time


def is_purchasable(n_robots, n_bits, cashier_infos, time):
    bit_capacities_per_cashier = []
    for cashier_info in cashier_infos:
        time_to_scan = time - cashier_info[2]
        n_scannable_items = time_to_scan // cashier_info[1]
        n_capable_items = cashier_info[0]
        bit_capacities_per_cashier.append(max(0, min(n_capable_items, n_scannable_items)))
    bit_capacities_per_cashier.sort(reverse=True)
    return n_bits <= sum(bit_capacities_per_cashier[0:n_robots])


if __name__ == '__main__':
    n_tests = int(input())
    for i in range(n_tests):
        r, b, c = [int(x) for x in input().split()]
        cashier_infos = []
        for _ in range(c):
            cashier_infos.append([int(x) for x in input().split()])
        ans = solve(r, b, cashier_infos)
        print("Case #%d: %d" % (i + 1, ans))
