from typing import List
from support.timers import timeit


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = text_file.readlines()

    return all_lines


@timeit
def part1(input_file: str):
    total = 0
    input = get_input(input_file)

    return total


@timeit
def part2(input_file: str):
    total = 0
    input = get_input(input_file)

    return total


print("Part 1")
# print(part1("day8/example.txt"))
# print(part1("day8/input.txt"))

print("Part 2")
# print(part2("day8/example.txt"))
# print(part2("day8/input.txt"))
