T = int(input())
for t in range(T):
    N = int(input())
    Fs = list(map(int, input().split()))
    Ps = list(map(lambda i: i - 1, map(int, input().split())))
    initiaters = [i for i in range(N) if i not in Ps]
    module_count = {i: 0 for i in range(N)}
    for i in initiaters:
        module_count[i] += 1
    for i in Ps:
        if i != -1:
            module_count[i] += 1
    module_stack = initiaters[:]
    module_points = {i: [0] for i in initiaters}
    result = 0
    while module_stack:
        module = module_stack.pop()
        points = module_points[module]
        count = module_count[module]
        if count == len(points):
            min_point = min(points)
            result += sum(points) - min_point
            next_module = Ps[module]
            if next_module == -1:
                result += max(Fs[module], min_point)
            else:
                module_points.setdefault(next_module, []).append(max(Fs[module], min_point))
                module_stack.append(next_module)
    print(f"Case #{t + 1}: {result}")
