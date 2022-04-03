T = int(input())
for t in range(T):
    first_printer = list(map(int, input().split()))
    second_printer = list(map(int, input().split()))
    third_printer = list(map(int, input().split()))
    least_printer = []
    for i in range(4):
        least_printer.append(min(first_printer[i], second_printer[i], third_printer[i]))
    if sum(least_printer) < 10**6:
        print(f"Case #{t+1}: IMPOSSIBLE")
    else:
        result = []
        total = 10**6
        for i in range(4):
            ans = min(least_printer[i], total)
            total -= ans
            result.append(ans)
        print(f"Case #{t+1}: {' '.join(map(str, result))}")
