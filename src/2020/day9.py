import copy
from support.timers import timeit
import string
from itertools import combinations


def get_input(filename):
    text_file = open(filename, "r")
    return [int(l.strip()) for l in text_file.readlines()]


@timeit
def part1(input_file, preamble_size):
    inputs = get_input(input_file)

    for i, current_value in enumerate(inputs[preamble_size:], preamble_size):
        # print(i, current_value)
        previous_values = inputs[i - preamble_size : i]
        # print(previous_values)

        combos = combinations(previous_values, 2)
        sums = [sum(c) for c in combos]

        if current_value not in sums:
            return current_value

    return -1


@timeit
def part2(input_file, target):
    inputs = get_input(input_file)

    for i, small_value in enumerate(inputs):
        current_total = small_value
        j = 1
        while current_total < target:
            current_total += inputs[i + j]

            if current_total == target:
                # print(inputs[i : i + j + 1])
                return max(inputs[i : i + j + 1]) + min(inputs[i : i + j + 1])

            j += 1

    return -1


print("Part 1")
print(part1("day9/example.txt", 5))
print(part1("day9/input.txt", 25))

# print("Part 2")
# print(part2("day9/example.txt", 127))
# print(part2("day9/input.txt", 10884537))
