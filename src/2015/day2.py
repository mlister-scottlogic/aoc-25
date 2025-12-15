from support.timers import timeit
from collections import Counter


def get_input(filename):
    text_file = open(filename, "r")
    return [[int(c) for c in l.split("x")] for l in text_file.readlines()]


@timeit
def part1(input_file):
    inputs = get_input(input_file)

    total = 0

    for i in inputs:
        l = i[0]
        w = i[1]
        h = i[2]

        area1 = l * w
        area2 = w * h
        area3 = h * l
        slack = min(area1, area2, area3)
        surface = 2 * area1 + 2 * area2 + 2 * area3

        # print(surface, slack, surface + slack)

        total += surface + slack

    return total


@timeit
def part2(input_file):
    inputs = get_input(input_file)

    total = 0

    for i in inputs:
        l = i[0]
        w = i[1]
        h = i[2]

        volume = l * w * h
        side1 = 2 * l + 2 * w
        side2 = 2 * w + 2 * h
        side3 = 2 * h + 2 * l

        smallest = min(side1, side2, side3)

        # print(smallest, volume, smallest + volume)

        total += smallest + volume

    return total


print("Part 1")
print(part1("day2/input.txt"))

print("Part 2")
print(part2("day2/input.txt"))
