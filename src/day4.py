from typing import List
from support.timers import timeit


def get_input(filename) -> dict[tuple[int, int], bool]:
    text_file = open(filename, "r")
    all_lines = text_file.readlines()
    all_lines = [l.strip() for l in all_lines]

    roll_map = {}
    for y, line in enumerate(all_lines):
        for x, field in enumerate(line):
            roll_map[(x, y)] = field == "@"

    return roll_map


@timeit
def part1(input_file: str):
    total = 0
    inputs = get_input(input_file)

    print(inputs)

    return total


@timeit
def part2(input_file: str):
    total = 0
    inputs = get_input(input_file)

    return total


print("Part 1")
print(part1("day4/example.txt"))
# print(part1("day4/input.txt"))

print("Part 2")
# print(part2("day4/example.txt"))
# print(part2("day4/input.txt"))
