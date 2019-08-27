import math
import sys

# def check_end(soil, minRequiredPreparedCells):
#     rowwise_n_prepared = [x.count(1) for x in soil]
#     n_prepared = sum(rowwise_n_prepared)
#     if n_prepared < minRequiredPreparedCells:
#         return False

#     rowwise_prepared_flag = [x > 0 for x in rowwise_n_prepared]
#     top = rowwise_prepared_flag.index(True)
#     bottom = len(rowwise_prepared_flag) - 1 - rowwise_prepared_flag[::-1].index(True)
#     soil_trimmed = soil[top:bottom + 1]
#     if is_rectangle(soil_trimmed):
#         return n_prepared >= minRequiredPreparedCells
#     return False

# def is_rectangle(arr):
#     e = arr[0]
#     for i in range(1, len(arr)):
#         row = arr[i]
#         if e != row:
#             return False
#         left = row.index(True)
#         right = len(row) - 1 - row[::-1].index(True)
#         for prepared in row[left:right + 1]:
#             if not prepared:
#                 return False
#     return True

nTests = int(input())
for i in range(nTests):
    minRequiredPreparedCells = int(input())
    if minRequiredPreparedCells < 9:
        minRequiredPreparedCells = 9
    nRows = 3
    nCols = math.ceil(minRequiredPreparedCells / nRows)
    soil = []
    for j in range(nCols):
        soil.append([0] * nRows)
    while True:
        iRow = -1
        for i, col in enumerate(soil):
            isPrepared = True
            for cell in col:
                if cell == 0:
                    isPrepared = False
                    break
            if not isPrepared:
                iRow = i + 1
                if iRow > nCols - 2:
                    iRow = nCols - 2
                break

        if iRow == -1:
            break

        if minRequiredPreparedCells == 1:
            break
        elif minRequiredPreparedCells <= 9:
            if check_end(soil, minRequiredPreparedCells):
                break

        print(iRow + 1, 2)
        sys.stdout.flush()
        x, y = [int(x) for x in input().split()]
        if x == 0 and y == 0:
            break
        soil[x - 1][y - 1] = 1

        # try:
        #     x, y = [int(x) for x in input().split()]
        #     soil[x - 1][y - 1] = 1
        # except ValueError:
        #     with open('result.txt', 'w') as f:
        #         f.write(str(soil))
