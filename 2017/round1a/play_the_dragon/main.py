import math

def solve_recursively(Hd, Ad, Hk, Ak, B, D, Hd_orig, already_attack = False, already_buff = False, cure_one_time_before = False):
    if Hk <= 0:
        return 0
    if Hd <= 0:
        return None
    if Ad == 0:
        return None
    if Hk <= Ad:
        return 1

    list_n_turns = []
    # Attack
    list_n_turns.append(solve_recursively(Hd - Ak, Ad, Hk - Ad, Ak, B, D, Hd_orig, True, already_buff, False))
    # Cure
    if Hd <= Ak and not cure_one_time_before:
        list_n_turns.append(solve_recursively(Hd_orig - Ak, Ad, Hk, Ak, B, D, Hd_orig, already_attack, already_buff, True))
    # Buff
    if not already_attack and Ad < Hk and B > 0:
        list_n_turns.append(solve_recursively(Hd - Ak, Ad + B, Hk, Ak, B, D, Hd_orig, already_attack, True, False))
    # Debuff
    if not already_attack and not already_buff and Ak > 0 and D > 0:
        Ak = max(0, Ak - D)
        list_n_turns.append(solve_recursively(Hd - Ak, Ad, Hk, Ak, B, D, Hd_orig, already_attack, already_buff, False))
    list_n_turns = [x + 1 for x in list_n_turns if x != None]
    if len(list_n_turns) == 0:
        return None
    return min(list_n_turns)

def solve(Hd, Ad, Hk, Ak, B, D):
    if Ad == 0:
        return None
    if Hk <= Ad:
        return 1
    if Hd <= Ak - D:
        return None
    if Hk <= 2 * Ad or Hk <= Ad + B:
        return 2
    if Hd <= 2 * Ak - 3 * D:
        return None

    n_turns_for_attacks_and_buffs = optimize_attacks_and_buffs(Ad, Hk, B)
    return optimize(Hd, Ak, D, n_turns_for_attacks_and_buffs)

def optimize(Hd, Ak, D, n_turns_for_attacks_and_buffs):
    if D == 0:
        return optimize_cures(Hd, Hd, Ak, n_turns_for_attacks_and_buffs)

    Hd_orig = Hd
    n_turns = 0
    max_interval = 0
    min_n_turns = math.pow(10, 9) * 2

    while True:
        if n_turns > n_turns_for_attacks_and_buffs:
            break

        if Ak == 0:
            nts = n_turns + n_turns_for_attacks_and_buffs
            return min(min_n_turns, nts)

        interval = math.ceil(Hd_orig / Ak) - 2
        if interval > max_interval:
            nts = n_turns + optimize_cures(Hd, Hd_orig, Ak, n_turns_for_attacks_and_buffs)
            min_n_turns = min(min_n_turns, nts)
            max_interval = interval

            while Hd > Ak - D and Ak > 0:
                Ak = max(0, Ak - D)
                Hd -= Ak
                n_turns += 1

            if Ak == 0:
                continue

            next_interval = interval + 1
            next_Ak = math.ceil(Hd_orig / (next_interval + 2))
            n_debuffs = math.floor((Ak - next_Ak) / D)
            # n_debuffs = min(n_debuffs, math.ceil(Ak / D))
            n_cures = math.floor(n_debuffs / interval)
            n_turns += n_cures * (interval + 1) + 1
            Ak = max(0, Ak - D * n_cures * interval)
            Hd = Hd_orig - Ak

        else:
            if Hd <= Ak - D:
                Hd = Hd_orig - Ak
                n_turns += 1

        Ak = max(0, Ak - D)
        Hd -= Ak
        n_turns += 1

    return min_n_turns

def optimize_cures(Hd, Hd_orig, Ak, n_turns_for_attacks_and_buffs):
    n_turns_first_attacks = math.ceil(Hd / Ak) - 1
    if n_turns_first_attacks + 1 >= n_turns_for_attacks_and_buffs:
        return n_turns_for_attacks_and_buffs
    interval = math.ceil(Hd_orig / Ak) - 2
    if interval == 0:
        return math.pow(10, 9) * 2
    n_intervals = math.floor((n_turns_for_attacks_and_buffs - n_turns_first_attacks) / interval)
    if interval == 1:
        return n_turns_first_attacks + (interval + 1) * (n_intervals - 1) + 1
    mod = (n_turns_for_attacks_and_buffs - n_turns_first_attacks) % interval
    if mod == 1:
        return n_turns_first_attacks + (interval + 1) * n_intervals + 1
    elif mod == 0:
        return n_turns_first_attacks + (interval + 1) * n_intervals
    else:
        return n_turns_first_attacks + (interval + 1) * n_intervals + 1 + mod

def optimize_attacks_and_buffs(Ad, Hk, B):
    n_buffs = 0
    n_turns = None
    while True:
        nts = n_buffs + math.ceil(Hk / (Ad + B * n_buffs))
        if n_turns == None or n_turns > nts:
            n_turns = nts
        else:
            break
        n_buffs += 1
    return n_turns

if __name__ == '__main__':
    for i in range(int(input())):
        Hd, Ad, Hk, Ak, B, D = [int(x) for x in input().split(" ")]
        ans = solve(Hd, Ad, Hk, Ak, B, D)
        # ans = solve_recursively(Hd, Ad, Hk, Ak, B, D, Hd)
        if ans == None:
            print("Case #%d: %s" % (i + 1, "IMPOSSIBLE"))
        else:
            print("Case #%d: %d" % (i + 1, ans))
