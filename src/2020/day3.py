from support.timers import timeit
from collections import Counter
from itertools import combinations


def get_input(filename):
    text_file = open(filename, "r")
    return [[1 if t == "#" else 0 for t in i.strip()] for i in text_file.readlines()]


@timeit
def part1(input_file):
    input = get_input(input_file)
    trees = 0
    current_x = 0

    for level in input:
        # print(level, current_x, current_x % len(level))
        trees += level[current_x % len(level)]

        current_x += 3

    return trees


def traverse(input, right_traverse, down_traverse):
    trees = 0
    current_x = 0

    for i in range(0, len(input), down_traverse):
        level = input[i]
        # print(level, current_x, current_x % len(level))
        trees += level[current_x % len(level)]

        current_x += right_traverse

    return trees


@timeit
def part2(input_file):
    trees = 0
    input = get_input(input_file)

    right_1_down_1 = traverse(input, 1, 1)
    print(right_1_down_1)
    right_3_down_1 = traverse(input, 3, 1)
    print(right_3_down_1)
    right_5_down_1 = traverse(input, 5, 1)
    print(right_5_down_1)
    right_7_down_1 = traverse(input, 7, 1)
    print(right_7_down_1)
    right_1_down_2 = traverse(input, 1, 2)
    print(right_1_down_2)

    return (
        right_1_down_1
        * right_3_down_1
        * right_5_down_1
        * right_7_down_1
        * right_1_down_2
    )


# print("Part 1")
# print(part1("day3/example.txt"))
# print(part1("day3/input.txt"))

print("Part 2")
print(part2("day3/example.txt"))
print(part2("day3/input.txt"))
