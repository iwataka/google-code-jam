import operator

def solve(ps):
    ordered_members = [chr(65 + x) for x in order_party_members(ps)]
    members_count = len(ordered_members)
    if members_count == 1:
        return ordered_members[0]
    elif members_count == 2:
        return ordered_members[0] + ordered_members[1]
    elif members_count == 3:
        return "%s %s%s" % (ordered_members[0], ordered_members[1], ordered_members[2])
    else:
        result = []
        for i in range(0, members_count, 2):
            remaining_count = members_count - i
            if remaining_count == 3:
                result.append(ordered_members[i])
                result.append(ordered_members[i + 1] + ordered_members[i + 2])
                break
            else:
                result.append(ordered_members[i] + ordered_members[i + 1])
        return ' '.join(result)
    return result

def order_party_members(ps):
    result = []
    while True:
        max_i, max_v = max(enumerate(ps), key=operator.itemgetter(1))
        if max_v == 0:
            break
        result.append(max_i)
        ps[max_i] = max_v - 1
    return result

t = int(input())
for i in range(t):
    n = int(input())
    ps = [int(x) for x in input().split()]
    ans = solve(ps)
    print("Case #%d: %s" % (i + 1, ans))
