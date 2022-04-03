T = int(input())
for t in range(T):
    R, C = map(int, input().split())
    print(f"Case #{t+1}:")
    print("..+" + "-+"*(C-1))
    for r in range(R):
        if r == 0:
            print("..|" + ".|"*(C-1))
        else:
            print("|" + ".|"*C)
        print("+" + "-+"*C)
