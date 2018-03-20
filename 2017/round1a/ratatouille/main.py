import math

def solve(N, P, Rs, Qs):
    count = 0
    r0 = Rs[0]
    for p in range(P):
        q0 = Qs[0][p]
        min = math.ceil(float(q0)  / 1.1 / float(r0))
        max = math.floor(float(q0) / 0.9 / float(r0))
        pickedup = pickup5(Qs, min, max, Rs, N)
        if pickedup != None:
            count += 1
            for i in range(1, N):
                del Qs[i][pickedup[i - 1]]
    return count

def pickup5(Qs, min, max, Rs, N):
    for mul in range(min, max + 1):
        pickedup = pickup4(Qs, Rs, mul, N)
        if pickedup != None:
            return pickedup
    return None

def pickup4(Qs, Rs, mul, N):
    indices = []
    for i in range(1, len(Qs)):
        Qs_row = Qs[i]
        pickedup = pickup2(Qs_row, Rs[i] * mul)
        if pickedup == None:
            return None
        else:
            indices.append(pickedup)
    return indices

def pickup2(Qs_row, req_mul):
    for i, q in enumerate(Qs_row):
        if float(req_mul) * 0.9 <= float(q) and float(q) <= float(req_mul) * 1.1:
            return i
    return None

T = int(input())

for i in range(T):
    N, P = [int(x) for x in input().split(" ")]
    Rs = [int(x) for x in input().split(" ")]
    Qs = []
    for j in range(N):
        Qs.append(sorted([int(x) for x in input().split(" ")]))
    line = "%s %s" % (Rs, Qs)
    ans = solve(N, P, Rs, Qs)
    print("Case #%d: %d" % (i + 1, ans))
