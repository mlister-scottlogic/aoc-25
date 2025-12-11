from typing import List
from support.timers import timeit

from collections import defaultdict


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = text_file.readlines()

    new_lines = []

    for line in all_lines:
        split_line = line.strip().split(" ")

        target = [0 if c == "." else 1 for c in split_line[0][1:-1]]
        buttons = [l[1:-1].split(",") for l in split_line[1:-1]]
        joltage = split_line[-1]

        new_lines.append((target, buttons, joltage))

    return new_lines


@timeit
def part1(input_file: str):
    total = 0

    input = get_input(input_file)
    print(input)

    return total


@timeit
def part2(input_file: str):
    return 0


print("Part 1")
print(part1("day10/example.txt"))
# print(part1("day10/input.txt"))

print("Part 2")
# print(part2("day10/example.txt"))
# print(part2("day10/input.txt"))
