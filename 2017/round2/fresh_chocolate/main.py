#!/usr/bin/env python

def solve(n_people_of_each_group, n_pieces_per_pack):
    zero_count = len([x for x in n_people_of_each_group if x % n_pieces_per_pack == 0])
    one_count = len([x for x in n_people_of_each_group if x % n_pieces_per_pack == 1])
    if n_pieces_per_pack == 2:
        return zero_count + (one_count // n_pieces_per_pack + (one_count % n_pieces_per_pack != 0))
    elif n_pieces_per_pack == 3:
        two_count = len([x for x in n_people_of_each_group if x % n_pieces_per_pack == 2])
        min_count = min(one_count, two_count)
        max_count = max(one_count, two_count)
        return zero_count + min_count + ((max_count - min_count) // n_pieces_per_pack + ((max_count - min_count) % n_pieces_per_pack != 0))
    elif n_pieces_per_pack == 4:
        two_count = len([x for x in n_people_of_each_group if x % n_pieces_per_pack == 2])
        three_count = len([x for x in n_people_of_each_group if x % n_pieces_per_pack == 3])
        min_count = min(one_count, three_count)
        max_count = max(one_count, three_count)
        extra_count = 2 if two_count % 2 == 1 else 0
        return zero_count + (two_count // 2) + min_count + ((max_count - min_count + extra_count) // n_pieces_per_pack + ((max_count - min_count + extra_count) % n_pieces_per_pack != 0))
    return 0

if __name__ == '__main__':
    n_tests = int(input())
    for i in range(n_tests):
        n_groups, n_pieces_per_pack = [int(x) for x in input().split()]
        n_people_of_each_group = [int(x) for x in input().split()]
        ans = solve(n_people_of_each_group, n_pieces_per_pack)
        print("Case #%d: %d" % (i + 1, ans))
