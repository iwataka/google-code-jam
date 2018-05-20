#!/usr/bin/env python

def solve(N, layout):
    rowwise_dups = set()
    for i_row, row in enumerate(layout):
        nums = set()
        for i, j, n in find_duplicate(row):
            rowwise_dups.add((i_row, i, n))
            rowwise_dups.add((i_row, j, n))

    colwise_dups = set()
    for i_col, col in enumerate(transpose(layout)):
        nums = set()
        for i, j, n in find_duplicate(col):
            colwise_dups.add((i, i_col, n))
            colwise_dups.add((j, i_col, n))

    rowwise_count = 0
    for i_row in range(len(layout)):
        duplicated = True
        for n in range(-N, N + 1):
            if n == 0:
                continue
            exists = False
            for _, i_col, _ in filter(lambda x: x[0] == i_row and x[2] == n, rowwise_dups):
                exists = True
                if not (i_row, i_col, n) in colwise_dups:
                    duplicated = False
                    break
            if exists:
                rowwise_count += 0.5 if duplicated else 1

    colwise_count = 0
    for i_col in range(len(layout[0])):
        duplicated = True
        for n in range(-N, N + 1):
            if n == 0:
                continue
            exists = False
            for i_row, _, _ in filter(lambda x: x[1] == i_col and x[2] == n, colwise_dups):
                exists = True
                if not (i_row, i_col, n) in rowwise_dups:
                    duplicated = False
                    break
            if exists:
                colwise_count += 0.5 if duplicated else 1

    total_dups = set()
    total_dups.update(rowwise_dups)
    total_dups.update(colwise_dups)

    return len(total_dups) - int(rowwise_count + colwise_count)

def find_duplicate(row):
    for i, n1 in enumerate(row):
        for j, n2 in enumerate(row[i+1:], i + 1):
            if n1 == n2:
                yield i, j, n1

def transpose(layout):
    result = []
    for i in range(len(layout[0])):
        col = []
        for row in layout:
            col.append(row[i])
        result.append(col)
    return result

if __name__ == '__main__':
    n_tests = int(input())
    for i in range(n_tests):
        N = int(input())
        layout = []
        for _ in range(N):
            layout.append([int(x) for x in input().split()])
        ans = solve(N, layout)
        print("Case #%d: %d" % (i + 1, ans))
