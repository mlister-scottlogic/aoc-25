from support.timers import timeit
from collections import Counter


def get_input(filename):
    text_file = open(filename, "r")
    all_lines = text_file.readlines()

    split_lines = [l.strip().split(" ") for l in all_lines]

    return [(l[0].split("-"), l[1][0], l[2]) for l in split_lines]


@timeit
def part1(input_file):
    input = get_input(input_file)
    total = 0

    for i in input:
        password = i[2]
        c = i[1]
        r = i[0]

        count = password.count(c)

        if count in range(int(r[0]), int(r[1]) + 1):
            total += 1

    return total


@timeit
def part2(input_file):
    input = get_input(input_file)

    total = 0

    for i in input:
        password = i[2]
        c = i[1]
        p1 = password[int(i[0][0]) - 1]
        p2 = password[int(i[0][1]) - 1]

        if (p1 == c) != (p2 == c):
            total += 1

    return total


# print("Part 1")
# print(part1("day2/example.txt"))
# print(part1("day2/input.txt"))

print("Part 2")
print(part2("day2/example.txt"))
print(part2("day2/input.txt"))
