import copy
from functools import cache
from math import prod
from support.timers import timeit
import string
from itertools import combinations
from collections import defaultdict


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = [l.strip() for l in text_file.readlines()]
    return int(all_lines[0]), [c for c in all_lines[1].split(",")]


@timeit
def part1(input_file):
    start_time, busses = get_input(input_file)

    active_busses = [int(c) for c in busses if c != "x"]

    time_after = [
        (b, abs(start_time - (((start_time // b) + 1) * b))) for b in active_busses
    ]

    minimum = min(time_after, key=lambda t: t[1])
    print(minimum)
    return minimum[0] * minimum[1]


@timeit
def part2(input_file):
    start_time, busses = get_input(input_file)

    return -1


print("Part 1")
print(part1("day13/example.txt"))
print(part1("day13/input.txt"))

# print("Part 2")
# print(part2("day13/example.txt"))
# print(part2("day13/input.txt"))
