#!/usr/bin/env python

def solve(pancake_states, flipper_size):
    count = 0
    for i in range(len(pancake_states) - flipper_size + 1):
        if pancake_states[i]:
            continue
        for j in range(flipper_size):
            pancake_states[i+j] = not pancake_states[i+j]
        count += 1
    for state in reversed(pancake_states):
        if not state:
            return -1
    return count


def convert_string_to_initial_pancake_states(s):
    return list(map(lambda c: True if c == '+' else False, s))


if __name__ == '__main__':
    n_tests = int(input())
    for i_test in range(n_tests):
        pancake_states_str, flipper_size_str = input().split()
        flipper_size = int(flipper_size_str)
        pancake_states = convert_string_to_initial_pancake_states(pancake_states_str)
        ans = solve(pancake_states, flipper_size)
        print("Case #%d: %s" % (i_test + 1, str(ans) if ans >= 0 else 'IMPOSSIBLE'))
