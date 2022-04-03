import itertools

T = int(input())
for t in range(T):
    N = int(input())
    Fs = list(map(int, input().split()))
    Ps = list(map(lambda i: i - 1, map(int, input().split())))
    initiaters = []
    for i in range(N):
        if i not in Ps:
            initiaters.append(i)
    perms = itertools.permutations(initiaters)
    result = 0
    for perm in perms:
        available = list(range(N))
        total_fun = 0
        for i in perm:
            max_fun = 0
            index = i
            while True:
                if index not in available:
                    break
                fun = Fs[index]
                max_fun = max(max_fun, fun)
                available.remove(index)
                if Ps[index] != -1:
                    index = Ps[index]
                else:
                    break
            total_fun += max_fun
        result = max(result, total_fun)
    print(f"Case #{t + 1}: {result}")
