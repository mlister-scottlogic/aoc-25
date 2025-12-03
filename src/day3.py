from typing import List
from support.timers import timeit


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = text_file.readlines()
    all_lines = [l.strip() for l in all_lines]

    return [[int(c) for c in l] for l in all_lines]


def joltage(batteries: List[int]):
    if len(batteries) == 2:
        return (batteries[0], batteries[1])

    current_best = joltage(batteries[1:])
    if batteries[0] >= current_best[0]:
        if current_best[0] > current_best[1]:
            return (batteries[0], current_best[0])
        else:
            return (batteries[0], current_best[1])

    return current_best


@timeit
def part1(input_file: str):
    total = 0
    inputs = get_input(input_file)

    # print(inputs)

    for i in inputs:
        best_value = joltage(i)
        jolt = best_value[0] * 10 + best_value[1]
        # print(f"------ {i} --- {best_value} --- {jolt} ------")
        total += jolt

    return total


@timeit
def part2(input_file: str):
    inputs = get_input(input_file)
    # print(inputs)
    count = 0


print("Part 1")
# print(part1("day3/example.txt"))
print(part1("day3/input.txt"))

print("Part 2")
# print(part2("day3/example.txt"))
# print(part2("day3/input.txt"))
