from support.timers import timeit
from collections import Counter


def get_input(filename):
    text_file = open(filename, "r")
    return text_file.readline().strip()


@timeit
def part1(input_file):
    input = get_input(input_file)

    return 0


@timeit
def part2(input_file):
    input = get_input(input_file)

    return 0


print("Part 1")
print(part1("day1/example.txt"))
print(part1("day1/input.txt"))

print("Part 2")
print(part2("day1/example.txt"))
print(part2("day1/input.txt"))
