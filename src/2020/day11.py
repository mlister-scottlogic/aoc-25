import copy
from functools import cache
from math import prod
from support.timers import timeit
import string
from itertools import combinations
from collections import defaultdict


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = [l.strip() for l in text_file.readlines()]

    m = {}

    for y, line in enumerate(all_lines):
        for x, c in enumerate(line):
            if c == "L":
                m[(x, y)] = 0

    return m


@timeit
def part1(input_file):
    input_map = get_input(input_file)

    changing = True
    count = 0
    new_input_map = copy.deepcopy(input_map)

    while changing:
        # print(count)
        # print(input_map)
        changing = False
        for k, v in input_map.items():
            x, y = k

            close_by = 0
            for x_delta in range(-1, 2):
                for y_delta in range(-1, 2):
                    if not (x_delta == 0 and y_delta == 0):
                        close_by += input_map.get((x + x_delta, y + y_delta), 0)

            if close_by == 0:
                new_input_map[k] = 1
                if v != 1:
                    changing = True
            elif close_by >= 4:
                new_input_map[k] = 0
                if v != 0:
                    changing = True

        input_map = copy.deepcopy(new_input_map)
        count += 1

    return sum(input_map.values())


@timeit
def part2(input_file):
    input_map = get_input(input_file)

    changing = True
    count = 0
    new_input_map = copy.deepcopy(input_map)

    max_x = max([l[0] for l in new_input_map.keys()])
    max_y = max([l[1] for l in new_input_map.keys()])

    while changing:
        # print(count)
        # print(input_map)
        changing = False
        for k, v in input_map.items():
            x, y = k

            close_by = 0
            for x_delta in range(-1, 2):
                for y_delta in range(-1, 2):
                    if not (x_delta == 0 and y_delta == 0):
                        for multi in range(1, max(max_x, max_y)):
                            target_x = x + (x_delta * multi)
                            target_y = y + (y_delta * multi)

                            seat = input_map.get((target_x, target_y), None)

                            if seat is not None:
                                close_by += seat
                                break

                            if target_x > max_x or target_y > max_y:
                                break

            if close_by == 0:
                new_input_map[k] = 1
                if v != 1:
                    changing = True
            elif close_by >= 5:
                new_input_map[k] = 0
                if v != 0:
                    changing = True

        input_map = copy.deepcopy(new_input_map)
        count += 1
    print("count", count)
    return sum(input_map.values())


print("Part 1")
# print(part1("day11/example.txt"))
# print(part1("day11/input.txt"))

print("Part 2")
# print(part2("day11/example.txt"))
print(part2("day11/input.txt"))
