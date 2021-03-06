import math

def solve(Hd, Ad, Hk, Ak, B, D):
    """Calculates the minimum number of turns to beat the knight.

    Args:
        Hd: the dragon's health.
        Ad: the dragon's attack.
        Hk: the knight's health.
        Ak: the knight's attack.
        B: buff value.
        D: debuff value.
    
    Returns:
        The minimum number of turns to beat the knight.

        None if the dragon can't beat the knight.
    """
    # The dragon can't beat the knight because the dragon's attack is 0.
    if Ad == 0:
        return None
    # The dragon can beat the knight in just 1 turn.
    if Hk <= Ad:
        return 1
    # The dragon will be beaten in just 1 turn even if debuffing the knight.
    if Hd <= Ak - D:
        return None
    #
    if Hk <= 2 * Ad or Hk <= Ad + B:
        return 2
    #
    if Hd <= 2 * Ak - 3 * D:
        return None

    n_turns_for_attacks_and_buffs = optimize_attacks_and_buffs(Ad, Hk, B)
    return optimize(Hd, Ak, D, n_turns_for_attacks_and_buffs)

def optimize_attacks_and_buffs(Ad, Hk, B):
    """Calculates the minimum numbers of turns taken only for attacks and buffs.

    It is known that the number of turns taken for attacks and buffs decreases
    in proportion to the number of buffs until certain point and then increases.

    Args:
        Ad: the dragon's attack.
        Hk: the knight's health.
        B: buff value

    Returns:
        The minimum number of turns taken only for attacks and buffs
        until the knight's health drops to 0.
    """
    n_buffs = 0
    min_n_turns = None
    while True:
        Ad_after_buffs = Ad + B * n_buffs
        n_attacks = math.ceil(Hk / Ad_after_buffs)
        n_turns = n_buffs + n_attacks
        if min_n_turns == None or min_n_turns > n_turns:
            min_n_turns = n_turns
        else:
            break
        n_buffs += 1
    return min_n_turns

def optimize(Hd, Ak, D, n_turns_for_attacks_and_buffs):
    """Calculates the minimum number of turns taken to beat the knight.

    Args:
        Hd: the dragon's health.
        Ak: the knight's attack.
        D: debuff value.
        n_turns_for_attacks_and_buffs: the minimum number of turns taken for attacks and buffs.

    Returns:
        The minimum number of turns taken to beat the knight
    """
    # No meanings to debuff at all.
    if D == 0:
        return optimize_cures(Hd, Hd, Ak, n_turns_for_attacks_and_buffs)

    Hd_orig = Hd
    n_turns_for_debuffs_and_cures = 0
    max_interval_between_cures = 0
    min_n_turns = math.pow(10, 9) * 2

    # TODO: Make this loop more performant
    while True:
        # No meanings to debuff any more.
        if Ak == 0:
            n_turns = n_turns_for_debuffs_and_cures + n_turns_for_attacks_and_buffs
            return min(min_n_turns, n_turns)

        interval_between_cures = math.ceil(Hd_orig / Ak) - 2
        # Calculates the total number of turns if required.
        if interval_between_cures > max_interval_between_cures:
            max_interval_between_cures = interval_between_cures
            n_turns = n_turns_for_debuffs_and_cures + optimize_cures(Hd, Hd_orig, Ak, n_turns_for_attacks_and_buffs)
            min_n_turns = min(min_n_turns, n_turns)

        # Cure if needed.
        if Hd <= Ak - D:
            Hd = Hd_orig - Ak
            n_turns_for_debuffs_and_cures += 1

        # Debuff.
        Ak = max(0, Ak - D)
        Hd -= Ak
        n_turns_for_debuffs_and_cures += 1

    return min_n_turns

def optimize_cures(Hd, Hd_orig, Ak, n_turns_for_attacks_and_buffs):
    """
    Args:
        Hd: the current dragon's health
        Hd_orig: the original dragon's health
        Ak: the knight's attack
        n_turns_for_attacks_and_buffs: the minimum number of turns taken for attacks and buffs
    """
    n_turns_until_first_attacks = math.ceil(Hd / Ak) - 1
    if n_turns_until_first_attacks + 1 >= n_turns_for_attacks_and_buffs:
        return n_turns_for_attacks_and_buffs
    interval = math.ceil(Hd_orig / Ak) - 2
    if interval == 0:
        return math.pow(10, 9) * 2
    n_intervals = math.floor((n_turns_for_attacks_and_buffs - n_turns_until_first_attacks) / interval)
    if interval == 1:
        return n_turns_until_first_attacks + (interval + 1) * (n_intervals - 1) + 1
    mod = (n_turns_for_attacks_and_buffs - n_turns_until_first_attacks) % interval
    if mod == 1:
        return n_turns_until_first_attacks + (interval + 1) * n_intervals + 1
    elif mod == 0:
        return n_turns_until_first_attacks + (interval + 1) * n_intervals
    else:
        return n_turns_until_first_attacks + (interval + 1) * n_intervals + 1 + mod

if __name__ == '__main__':
    for i in range(int(input())):
        Hd, Ad, Hk, Ak, B, D = [int(x) for x in input().split(" ")]
        ans = solve(Hd, Ad, Hk, Ak, B, D)
        if ans == None:
            print("Case #%d: %s" % (i + 1, "IMPOSSIBLE"))
        else:
            print("Case #%d: %d" % (i + 1, ans))
