import copy
from functools import cache
from math import prod
from support.timers import timeit
import string
from itertools import combinations
from collections import defaultdict


def get_input(filename):
    text_file = open(filename, "r")
    return [int(l.strip()) for l in text_file.readlines()]


@timeit
def part1(input_file):
    inputs = get_input(input_file)

    sorted_inputs = sorted(inputs)

    differences = []

    current_jolt = 0

    for i in sorted_inputs:
        differences.append(i - current_jolt)
        current_jolt = i

    # print(differences)
    ones = differences.count(1)
    # Count for final adapter
    threes = differences.count(3) + 1

    print("1s: ", ones, " 3s: ", threes)

    return ones * threes


@cache
def traverse(inputs, current_value):
    if current_value == 0:
        return 1

    next_values = [i for i in range(current_value - 3, current_value) if i in inputs]

    return sum([traverse(inputs, v) for v in next_values])


@timeit
def part2(input_file):
    inputs = get_input(input_file)
    sorted_inputs = frozenset([max(inputs) + 3, *inputs, 0])

    return traverse(sorted_inputs, max(inputs))


# print("Part 1")
# print(part1("day10/example.txt"))
# print(part1("day10/input.txt"))

print("Part 2")
# print(part2("day10/example1.txt"))
# print(part2("day10/example2.txt"))
print(part2("day10/input.txt"))
