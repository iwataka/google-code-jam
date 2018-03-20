def solve(mat):
    R, C = len(mat), len(mat[0])
    already_checked_chars = []
    for r in range(R):
        row = mat[r]
        for c in range(C):
            char = mat[r][c]
            if char == "?":
                continue
            if char in already_checked_chars:
                continue
            min, max = extendsHorizontally(row, c)
            top, bottom = extendsVertically(mat, r, min, max)
            # Assign values
            for _r in range(top, bottom + 1):
                for _c in range(min, max + 1):
                    mat[_r][_c] = char
            already_checked_chars.append(char)

def extendsHorizontally(row, i):
    min = i
    max = i
    for c in range(i - 1, -1, -1):
        if row[c] == "?":
            min = c
        else:
            break
    for c in range(i + 1, len(row)):
        if row[c] == "?":
            max = c
        else:
            break
    return min, max

def extendsVertically(mat, i, min, max):
    top = i
    bottom = i
    for r in range(i - 1, -1, -1):
        ok = True
        for c in range(min, max + 1):
            if mat[r][c] != "?":
                ok = False
        if ok:
            top = r
        else:
            break
    for r in range(i + 1, len(mat)):
        ok = True
        for c in range(min, max + 1):
            if mat[r][c] != "?":
                ok = False
        if ok:
            bottom = r
        else:
            break
    return top, bottom

T = int(input())

for i in range(T):
    R, C = input().split(' ')
    R, C = int(R), int(C)
    mat = [[c for c in input()] for j in range(R)]
    print("Case #%d:" % (i + 1))
    solve(mat)
    for row in mat:
        print("".join(row))
