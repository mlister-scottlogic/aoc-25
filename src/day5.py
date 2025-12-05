from typing import List
from support.timers import timeit


def get_input(filename) -> tuple[List[tuple[int, int]], List[int]]:
    text_file = open(filename, "r")
    all_lines = text_file.readlines()
    all_lines = [l.strip() for l in all_lines]

    space_index = all_lines.index("")

    ranges = [
        (int(r.split("-")[0]), int(r.split("-")[1])) for r in all_lines[0:space_index]
    ]

    ids = [int(id) for id in all_lines[space_index + 1 :]]

    return ranges, ids


@timeit
def part1(input_file: str):
    ranges, ids = get_input(input_file)

    total = 0

    for id in ids:
        for range in ranges:
            if id >= range[0] and id <= range[1]:
                total += 1
                # print(id)
                break

    return total


@timeit
def part2(input_file: str):
    inputs = get_input(input_file)


print("Part 1")
# print(part1("day5/example.txt"))
print(part1("day5/input.txt"))

print("Part 2")
# print(part2("day5/example.txt"))
# print(part2("day5/input.txt"))
