from support.timers import timeit
from collections import Counter
from itertools import combinations


def get_input(filename):
    text_file = open(filename, "r")
    return [int(i.strip()) for i in text_file.readlines()]


@timeit
def part1(input_file):
    input = get_input(input_file)

    current = 0

    for i in input:
        current = i

        for j in input[0:i] + input[i + 1 :]:
            if current + j == 2020:
                print(current, j)
                return current * j

    return -1


@timeit
def part2(input_file):
    input = get_input(input_file)

    combos = combinations(range(len(input)), 3)

    for c in combos:
        if sum([input[c[0]], input[c[1]], input[c[2]]]) == 2020:
            print(input[c[0]], input[c[1]], input[c[2]])
            return input[c[0]] * input[c[1]] * input[c[2]]

    return -1


# print("Part 1")
# print(part1("day1/example.txt"))
# print(part1("day1/input.txt"))

print("Part 2")
print(part2("day1/example.txt"))
print(part2("day1/input.txt"))
