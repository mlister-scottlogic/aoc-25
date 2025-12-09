import math
import re
from typing import List
from support.timers import timeit


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = text_file.readlines()

    rex = re.compile(r"\s+")
    all_lines = [rex.sub(" ", l.strip()).split(" ") for l in all_lines]

    return all_lines


@timeit
def part1(input_file: str):
    total = 0
    inputs = get_input(input_file)

    # print(inputs)

    for index, operator in enumerate(inputs[-1]):
        numbers = []

        for i in range(0, len(inputs) - 1):
            # print(i)
            numbers.append(int(inputs[i][index]))

        # print(index, operator, numbers)

        if operator == "+":
            s = sum(numbers)
            # print(s)
            total += s

        if operator == "*":
            p = math.prod(numbers)
            # print(p)
            total += p

    return total


@timeit
def part2(input_file: str):
    inputs = get_input(input_file)


print("Part 1")
print(part1("day6/example.txt"))
print(part1("day6/input.txt"))

print("Part 2")
# print(part2("day6/example.txt"))
# print(part2("day6/input.txt"))
