tolerance = 1e-12

def solve(core_success_possibilities, min_n_cores_to_success, n_training_units):
    core_success_possibilities.sort()
    while n_training_units > tolerance:
        first_index = len(core_success_possibilities) - min_n_cores_to_success
        smallest_possibility = core_success_possibilities[first_index]
        if abs(smallest_possibility - 1.0) < tolerance:
            return 1.0
        second_smallest_index = len(core_success_possibilities)
        second_smallest_possib = 1.0
        for i in range(first_index + 1, len(core_success_possibilities)):
            possib = core_success_possibilities[i]
            if possib != smallest_possibility:
                second_smallest_index = i
                second_smallest_possib = possib
                break
        count = second_smallest_index - first_index
        diff = second_smallest_possib - smallest_possibility
        if diff * count > n_training_units:
            diff = n_training_units / count
        for j in range(first_index, second_smallest_index):
            core_success_possibilities[j] += diff
        n_training_units -= diff * count

    total_possib = 0.0
    for n_cores_to_success in range(min_n_cores_to_success, len(core_success_possibilities) + 1):
        total_possib += calc_total_possibility(core_success_possibilities, n_cores_to_success)
    return total_possib


def calc_total_possibility(core_success_possibilities, n_cores_to_success, pointer=None, cache=None):
    if cache is None:
        cache = {}
    if pointer is None:
        pointer = 0

    key = (n_cores_to_success, pointer)
    if key in cache:
        return cache[key]
    if pointer >= len(core_success_possibilities):
        return 1

    cur_possib = core_success_possibilities[pointer]
    n_remainings = len(core_success_possibilities) - pointer
    total_possib = 0
    if n_cores_to_success > 0:
        total_possib += cur_possib * calc_total_possibility(core_success_possibilities, n_cores_to_success - 1, pointer + 1, cache)
    if n_remainings > n_cores_to_success:
        total_possib += (1 - cur_possib) * calc_total_possibility(core_success_possibilities, n_cores_to_success, pointer + 1, cache)

    cache[key] = total_possib
    return total_possib


if __name__ == '__main__':
    n_tests = int(input())
    for i in range(n_tests):
        n_total_cores, min_n_cores_to_success = [int(x) for x in input().split()]
        n_training_units = float(input())
        core_success_possibilities = [float(x) for x in input().split()]
        ans = solve(core_success_possibilities, min_n_cores_to_success, n_training_units)
        print("Case #%d: %0.10f" % (i + 1, ans))
