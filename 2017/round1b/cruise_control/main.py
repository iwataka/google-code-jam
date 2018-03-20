def solve(D, horses):
    return D / max([(D - p) / s for p, s in horses])
    # horses = sorted(horses, key=lambda h: h[0])
    # time = 0
    # pos = horses[0][0]
    # speed = horses[0][1]
    # for i in range(1, len(horses)):
    #     p, s = horses[i]
    #     if speed <= s:
    #         continue
    #     spent_time = (p - pos) / (speed - s)
    #     reached_pos = pos + spent_time * speed
    #     if reached_pos >= D:
    #         time += (D - pos) / speed
    #         pos = D
    #         break
    #     else:
    #         time += spent_time
    #         pos = reached_pos
    #         speed = s
    # if pos < D:
    #     time += (D - pos) / speed
    #     pos = D
    # return D / time

for i in range(int(input())):
    D, N = [int(x) for x in input().split(" ")]
    horses = []
    for j in range(N):
        horses.append([int(x) for x in input().split(" ")])
    ans = solve(D, horses)
    print("Case #%d: %.6f" % (i + 1, ans))
