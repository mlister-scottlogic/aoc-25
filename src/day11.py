from typing import List
from support.timers import timeit
from functools import cache

from collections import defaultdict

from itertools import combinations
from functools import reduce


def get_input(filename) -> dict[str, List[str]]:
    text_file = open(filename, "r")
    all_lines = text_file.readlines()

    new_lines = {}

    for line in all_lines:
        split_line = line.strip().split(":")

        start = split_line[0]

        outputs = split_line[1].strip().split(" ")

        new_lines[start] = outputs

    return new_lines


def number_of_paths(node: str, all_nodes):
    if node == "out":
        return 1

    return sum([number_of_paths(n, all_nodes) for n in all_nodes[node]])


@timeit
def part1(input_file: str):
    total = 0

    input = get_input(input_file)

    return number_of_paths("you", input)


@timeit
def part2(input_file: str):
    return 0


print("Part 1")
# print(part1("day11/example.txt"))
print(part1("day11/input.txt"))

print("Part 2")
# print(part2("day11/example.txt"))
# print(part2("day11/input.txt"))
