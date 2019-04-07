#!/usr/bin/env python

import sys


def state(N, interval, debug=False):
    count = 0
    result = ''
    c = '1'
    num = 0
    intervaled = True
    for _ in range(N):
        result += c
        count += 1
        if intervaled:
            num += 1
            intervaled = False
        if count == interval:
            count = 0
            if c == '1':
                c = '0'
            else:
                c = '1'
            intervaled = True
    if debug:
        raise Exception(str(result))
    print(result)
    sys.stdout.flush()
    return num


def analyze_first_response(response, state_num):
    c = '1'
    i = 0
    result = []
    while True:
        response = response[i:]
        c = '0' if c == '1' else '1'
        i = response.find(c)
        if i == -1:
            result.append(len(response))
            break
        else:
            result.append(i)
    return result


def answer(ub_nums, debug=False):
    result = []
    for i, n in enumerate(ub_nums):
        if n == 0:
            result.append(str(i))
    if debug:
        raise Exception(str(result))
    print(' '.join(result))
    sys.stdout.flush()

def analyze_response(response, ub_nums, state_num):
    result = []
    first = 0
    for n_unbroken in ub_nums:
        taken = response[first:first+n_unbroken]
        result.append(taken.count('1'))
        if len(result) == state_num:
            break
        result.append(taken.count('0'))
        if len(result) == state_num:
            break
        first = first+n_unbroken
    return result


if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        N, B, F = map(int, input().split())
        state_num = state(N, 16)
        first_response = input()
        unbroken_nums = analyze_first_response(first_response, state_num)
        # if i == 2:
        #     raise Exception(str(N) + ':' + str(unbroken_nums))

        state_num = state(N, 8)
        response = input()
        # if i == 2:
        #     raise Exception(str(N) + ':' + str(response))
        unbroken_nums = analyze_response(response, unbroken_nums, state_num)
        # if i == 2:
        #     raise Exception(str(N) + ':' + str(unbroken_nums))

        state_num = state(N, 4)
        response = input()
        # if i == 2:
        #     raise Exception(str(N) + ':' + str(response))
        unbroken_nums = analyze_response(response, unbroken_nums, state_num)
        # if i == 2:
        #     raise Exception(str(N) + ':' + str(unbroken_nums))

        state_num = state(N, 2)
        response = input()
        # if i == 1:
        #     raise Exception(str(N) + ':' + str(response))
        unbroken_nums = analyze_response(response, unbroken_nums, state_num)
        # if i == 2:
        #     raise Exception(str(N) + ':' + str(unbroken_nums))

        state_num = state(N, 1)
        response = input()
        unbroken_nums = analyze_response(response, unbroken_nums, state_num)
        # if i == 2:
        #     raise Exception(str(N) + ':' + str(unbroken_nums))

        answer(unbroken_nums)
        verdict = int(input())
        if verdict == -1:
            raise Exception('wrong')
