def solve(maxPossibleDamage, orders):
    nShoots = orders.count(1)
    if nShoots > maxPossibleDamage:
        return None

    nTurns = 0
    while True:
        orders, damage = calcDamage(orders)
        if damage <= maxPossibleDamage:
            return nTurns
        lastValidCharge = len(orders) - 1 - orders[::-1].index(2)
        orders[lastValidCharge + 1], orders[lastValidCharge] = orders[lastValidCharge], orders[lastValidCharge + 1]
        nTurns += 1

def calcDamage(orders):
    damage = 1
    totalDamage = 0
    lastShootTurn = 0
    for i, order in enumerate(orders):
        if order == 1:
            totalDamage += damage
            lastShootTurn = i
        else:
            damage *= 2
    orders = orders[0:(lastShootTurn + 1)]
    return orders, totalDamage

nTests = int(input())
for i in range(nTests):
    maxPossibleDamage, orderStr = input().split()
    maxPossibleDamage = int(maxPossibleDamage)
    orders = []
    for c in orderStr:
        if c == "S":
            orders.append(1)
        elif c == "C":
            orders.append(2)
    ans = solve(maxPossibleDamage, orders)
    if ans == None:
        print("Case #%d: %s" % (i + 1, "IMPOSSIBLE"))
    else:
        print("Case #%d: %d" % (i + 1, ans))
