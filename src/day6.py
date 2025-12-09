from typing import List
from support.timers import timeit


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = text_file.readlines()
    all_lines = [l.strip() for l in all_lines]


@timeit
def part1(input_file: str):
    inputs = get_input(input_file)


@timeit
def part2(input_file: str):
    inputs = get_input(input_file)


print("Part 1")
# print(part1("day6/example.txt"))
print(part1("day6/input.txt"))

print("Part 2")
# print(part2("day6/example.txt"))
print(part2("day6/input.txt"))
