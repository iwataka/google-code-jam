#!/usr/bin/env python

def solve(C, ball_counts):
    if ball_counts[0] == 0 or ball_counts[-1] == 0:
        return None, []
    column_results = [0] * C
    used_column = -1
    for c, ball_count in enumerate(ball_counts):
        if ball_count == 0:
            continue
        used_column += 1
        for _c in range(used_column, used_column + ball_count):
            column_results[_c] = c - _c
            used_column = _c
    row_count = abs(max(column_results, key=abs)) + 1
    layout = [["."] * C for _ in range(row_count)]
    for c, column_result in enumerate(column_results):
        if column_result == 0:
            continue
        dx = column_result // abs(column_result)
        for i in range(abs(column_result)):
            layout[i][c + dx * i] = "/" if dx < 0 else "\\"
    return row_count, layout

if __name__ == '__main__':
    n_tests = int(input())
    for i in range(n_tests):
        C = int(input())
        ball_counts = [int(x) for x in input().split()]
        row_count, layout = solve(C, ball_counts)
        if row_count is None:
            print("Case #%d: IMPOSSIBLE" % (i + 1))
        else:
            print("Case #%d: %d" % (i + 1, row_count))
            for row in layout:
                print("".join(row))
