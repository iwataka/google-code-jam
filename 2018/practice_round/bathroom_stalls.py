import math

def solve(n_stalls, n_persons):
    max = n_stalls
    larger_count = 1
    smaller_count = 0
    while n_persons > larger_count + smaller_count:
        n_persons -= larger_count
        n_persons -= smaller_count
        max, larger_count, smaller_count = divideAll(max, larger_count, smaller_count)
    return divide(max, larger_count, smaller_count, n_persons)

def divideAll(max, larger_count, smaller_count):
    if max % 2 == 0:
        return math.floor(max / 2), larger_count, larger_count + smaller_count * 2
    else:
        return math.floor((max - 1) / 2), larger_count * 2 + smaller_count, smaller_count

def divide(max, larger_count, smaller_count, n_persons):
    if n_persons <= larger_count:
        if max % 2 == 0:
            return math.floor(max / 2), math.floor(max / 2) - 1
        else:
            return math.floor((max - 1) / 2), math.floor((max - 1) / 2)
    else:
        if max % 2 == 0:
            return math.floor(max / 2) - 1, math.floor(max / 2) - 1
        else:
            return math.floor((max - 1) / 2), math.floor((max - 1) / 2) - 1

t = int(input())
for i in range(t):
    n, k = [int(x) for x in input().split()]
    max, min = solve(n, k)
    print("Case #%d: %d %d" % (i + 1, max, min))
