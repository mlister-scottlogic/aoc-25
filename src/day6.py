import math
import re
from typing import List
from support.timers import timeit


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = text_file.readlines()

    return all_lines


@timeit
def part1(input_file: str):
    total = 0
    inputs = get_input(input_file)

    rex = re.compile(r"\s+")
    inputs = [rex.sub(" ", l.strip()).split(" ") for l in inputs]

    # print(inputs)

    for index, operator in enumerate(inputs[-1]):
        numbers = []

        for i in range(0, len(inputs) - 1):
            # print(i)
            numbers.append(int(inputs[i][index]))

        # print(row, operator, numbers)

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
    total = 0

    current_operator = " "
    numbers = []

    for i in range(len(inputs[-1]) - 1, -1, -1):
        current_operator = inputs[-1][i]

        temp_num = ""
        for row in inputs[:-1]:
            temp_num += row[i]

        if temp_num.strip() != "":
            numbers.append(int(temp_num))

        if current_operator != " ":
            # print(current_operator, numbers)

            if current_operator == "+":
                s = sum(numbers)
                # print(s)
                total += s

            if current_operator == "*":
                p = math.prod(numbers)
                # print(p)
                total += p

            # New problem starting after operator has been applied so reset numbers
            numbers = []

    return total


print("Part 1")
# print(part1("day6/example.txt"))
# print(part1("day6/input.txt"))

print("Part 2")
# print(part2("day6/example.txt"))
print(part2("day6/input.txt"))
