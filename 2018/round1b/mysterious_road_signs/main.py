#!/usr/bin/env python

import itertools


def reverse_sign(sign):
    return (sign[0], sign[2], sign[1])


def span_contiguous_signs(signs):
    m = signs[0][1]
    contiguous_signs, rest_signs = span(lambda s: s[1] == m, signs)
    if rest_signs:
        n = rest_signs[0][2]
        contiguous_signs += list(itertools.takewhile(lambda s: s[1] == m or s[2] == n, rest_signs))
    return contiguous_signs, rest_signs


def span(pred, itr):
    front = []
    rear = []
    append_front = True
    for x in itr:
        if not pred(x):
            append_front = False
        if append_front:
            front.append(x)
        else:
            rear.append(x)
    return front, rear


def to_range(contiguous_signs):
    return (contiguous_signs[0][0], contiguous_signs[-1][0])


def signs_to_contiguous_ranges(signs):
    rest_signs = signs
    ranges = []
    while (rest_signs):
        contiguous_signs, rest_signs = span_contiguous_signs(rest_signs)
        ranges.append(to_range(contiguous_signs))
    return ranges


def size(rng):
    return rng[1] - rng[0] + 1


nTests = int(input())
for i in range(nTests):
    nSigns = int(input())
    signs = []
    for j in range(nSigns):
        d, a, b = map(int, input().split())
        signs.append((j, d + a, d - b))
    contiguous_ranges = signs_to_contiguous_ranges(signs) + signs_to_contiguous_ranges(list(map(reverse_sign, signs)))
    max_size = max(map(size, contiguous_ranges))
    count = len(set(filter(lambda r: size(r) == max_size, contiguous_ranges)))
    print("Case #%d: %d %d" % (i + 1, max_size, count))
