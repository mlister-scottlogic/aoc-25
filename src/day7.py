import math
import re
from typing import List
from support.timers import timeit


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = text_file.readlines()

    start_position = all_lines[0].index("S")
    splitters = [
        [i for i, val in enumerate(line) if val == "^"] for line in all_lines[1:]
    ]

    return start_position, splitters


@timeit
def part1(input_file: str):
    total = 0
    start_position, splitters = get_input(input_file)

    current_rays = set([start_position])

    for l in splitters:
        # print(current_rays, l, total)

        new_rays = set([*current_rays])
        for ray in current_rays:
            if ray in l:
                new_rays.remove(ray)
                new_rays.add(ray + 1)
                new_rays.add(ray + -1)
                total += 1

        current_rays = new_rays

    return total


@timeit
def part2(input_file: str):
    inputs = get_input(input_file)
    total = 0

    return total


print("Part 1")
# print(part1("day7/example.txt"))
print(part1("day7/input.txt"))

print("Part 2")
# print(part2("day7/example.txt"))
# print(part2("day7/input.txt"))
