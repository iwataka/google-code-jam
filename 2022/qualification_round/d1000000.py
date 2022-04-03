T = int(input())
for t in range(T):
    N = int(input())
    Ss = list(sorted(map(int, input().split())))
    result = 0
    curlen = 0
    for i, s in enumerate(Ss):
        curlen = min(i + 1, s, curlen + 1)
        result = max(result, curlen)
    print(f"Case #{t + 1}: {result}")
