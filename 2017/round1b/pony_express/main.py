import math

def solve(horses, admat, routes):
    return [solve_for_one_route(horses, admat, u, v) for u, v in routes]

def solve_for_one_route(horses, admat, u, v, speed = 0, max_total_dist = 0, already_reached = [], threshold = math.pow(10, 9) * 100):
    if u == v:
        return 0
    e, s = horses[u]
    ads = admat[u]
    spent_time_list = []
    for i, dist in enumerate(ads):
        if dist == -1 or i in already_reached:
            continue
        ar = [x for x in already_reached]
        ar.append(i)
        # Not change horse
        if dist <= max_total_dist and not (max_total_dist < e and speed < s):
            extra_time = solve_for_one_route(horses, admat, i, v, speed, max_total_dist - dist, ar)
            if extra_time != None:
                spent_time_list.append(dist / speed + extra_time)
        # Change horse
        if dist <= e and not (e < max_total_dist and s < speed):
            extra_time = solve_for_one_route(horses, admat, i, v, s, e - dist, ar)
            if extra_time != None:
                spent_time_list.append(dist / s + extra_time)
    if len(spent_time_list) == 0:
        return None
    return min(spent_time_list)

for i in range(int(input())):
    N, Q = [int(x) for x in input().split(" ")]
    horses = []
    for j in range(N):
        e, s = [int(x) for x in input().split(" ")]
        horses.append((e, s))
    admat = []
    for j in range(N):
        admat.append([int(x) for x in input().split(" ")])
    routes = []
    for j in range(Q):
        u, v = [int(x) for x in input().split(" ")]
        routes.append((u - 1, v - 1))
    ans = solve(horses, admat, routes)
    print("Case #%d: %s" % (i + 1, " ".join(["%.9g" % x for x in ans])))
