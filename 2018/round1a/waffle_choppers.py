#!/usr/bin/env python

from functools import reduce


def solve(waffle_grid, h, v):
    n_pieces = (h + 1) * (v + 1)
    n_choco_chips = sum([sum(x) for x in waffle_grid])
    if n_choco_chips % n_pieces != 0:
        return False
    # Horiazontal
    n_each_pieces_h = n_choco_chips // (h + 1)
    sum_n_pieces_h = 0
    cuts_h = [-1]
    for i, row in enumerate(waffle_grid):
        sum_n_pieces_h += sum(row)
        if sum_n_pieces_h == n_each_pieces_h:
            sum_n_pieces_h = 0
            cuts_h.append(i)
        elif sum_n_pieces_h < n_each_pieces_h:
            continue
        else:
            return False

    cutted_waffle_grid = []
    for j in range(0, len(cuts_h) - 1):
        top = cuts_h[j] + 1
        bottom = cuts_h[j + 1]
        cutted_waffle_grid.append(waffle_grid[top:bottom + 1])

    n_each_pieces = n_choco_chips // n_pieces
    n_cols = len(waffle_grid[0])
    left = 0
    for i in range(0, n_cols):
        sums_choco_chips = []
        for cutted_waffle_row in cutted_waffle_grid:
            sums_choco_chips.append(
                sum([sum(x[left:i + 1]) for x in cutted_waffle_row]))
        cutted_properly = True
        max_chips = max(sums_choco_chips)
        for sum_chips in sums_choco_chips:
            if sum_chips != n_each_pieces:
                cutted_properly = False
                break
        if cutted_properly:
            left = i + 1
            continue
        elif max_chips <= n_each_pieces:
            continue
        else:
            return False

    return True


if __name__ == '__main__':
    n_tests = int(input())
    for i in range(n_tests):
        r, c, h, v = [int(x) for x in input().split()]
        waffle_grid = []
        for _ in range(r):
            waffle_grid.append([1 if x == '@' else 0 for x in input()])
        ans = solve(waffle_grid, h, v)
        print("Case #%d: %s" % (i + 1, "POSSIBLE" if ans else "IMPOSSIBLE"))
