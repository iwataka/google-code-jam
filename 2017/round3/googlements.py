import itertools
import math

def solve(vals):
    count = 1
    if not is_valid_googlement(vals):
        return count

    anums = generate_ancestor_nums(vals)
    if not is_valid_googlement(anums):
        return count + just_count(vals)

    for perm in set(itertools.permutations(anums)):
        plist = list(perm)
        if not vals == plist:
            count += solve(plist)
    return count

def is_valid_googlement(vals):
    return len(vals) >= sum(vals)

def just_count(vals):
    f = math.factorial
    rem = len(vals)
    count = 1
    for i, val in enumerate(vals):
        count *= f(rem) / f(val) / f(rem - val)
        rem -= val
    return count

def generate_ancestor_nums(vals):
    result = []
    for i, val in enumerate(vals):
        for j in range(val):
            result.append(i + 1)
    s = sum(vals)
    l = len(vals)
    if l > s:
        for i in range(l - s):
            result.append(0)
    return result

T = int(raw_input())

for t in range(T):
    vals = [int(d) for d in raw_input()]
    count = solve(vals)
    print("Case #%d: %d" % (t + 1, count))
