import math


def solve(pancakes, stack_size):
    max_surface_area = 0
    for i, head in enumerate(pancakes):
        rest_pancakes = pancakes[i + 1:]
        if len(rest_pancakes) < stack_size - 1:
            break
        top_surface_area = math.pi * head[0] ** 2
        rest_pancakes.sort(key=lambda x: x[2], reverse=True)
        side_surface_area = head[2] + sum([x[2] for x in rest_pancakes[0:stack_size - 1]])
        surface_area = top_surface_area + side_surface_area
        if surface_area > max_surface_area:
            max_surface_area = surface_area
    return max_surface_area


n_tests = int(input())

for i in range(n_tests):
    n_pancakes, stack_size = [int(x) for x in input().split()]
    pancakes = []
    for j in range(n_pancakes):
        pancake = [int(x) for x in input().split()]
        pancake.append(2 * math.pi * pancake[0] * pancake[1])
        pancakes.append(pancake)
    pancakes.sort(key=lambda x: x[0], reverse=True)
    max_surface_area = solve(pancakes, stack_size)
    print("Case #%d: %.9f" % (i + 1, max_surface_area))
