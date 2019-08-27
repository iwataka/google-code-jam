def solve(arr):
    evenArr = [x for i, x in enumerate(arr) if i % 2 == 0]
    oddArr = [x for i, x in enumerate(arr) if i % 2 == 1]
    evenArr = sorted(evenArr)
    oddArr = sorted(oddArr)
    for i in range(len(arr) - 1):
        if i % 2 == 0:
            even = i // 2
            odd = i // 2
            if evenArr[even] > oddArr[odd]:
                return i
        elif i % 2 == 1:
            odd = (i - 1) // 2
            even = (i + 1) // 2
            if oddArr[odd] > evenArr[even]:
                return i
    return None

nTests = int(input())
for i in range(nTests):
    lenArr = input()
    arr = [int(x) for x in input().split()]
    ans = solve(arr)
    if ans == None:
        print("Case #%d: OK" % (i + 1))
    else:
        print("Case #%d: %d" % (i + 1, ans))
